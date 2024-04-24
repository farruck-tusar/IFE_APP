import os

import cv2
from PySide6.QtCore import QDir, Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget, QFileDialog, QLabel

from application import Settings
from widgets.video_player import VideoPlayer


class VideoLoader(QWidget):
    def __init__(self, main_ui):
        super().__init__(main_ui)
        self.main_ui = main_ui
        self.selected_videos = []
        self.video_preview_grid = self.main_ui.video_preview

    def load_videos(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.ShowDirsOnly

        selected_folder = QFileDialog.getExistingDirectory(self, "Select Folder with Videos", QDir.homePath(),
                                                           options=options)
        if selected_folder:
            self.main_ui.load_directory.setText(selected_folder)
            video_files = [f for f in os.listdir(selected_folder) if
                           f.lower().endswith(tuple(Settings.SUPPORTED_VIDEO_EXT))]

            self.selected_videos = video_files
            self.update_video_preview_grid()

    def update_video_preview_grid(self):
        self.clear_video_preview_grid()

        if not self.selected_videos:
            no_videos_label = QLabel("No supported videos found in the selected folder")
            no_videos_label.setAlignment(Qt.AlignCenter)
            self.video_preview_grid.addWidget(no_videos_label)
            return

        for row, video_filename in enumerate(self.selected_videos):
            path = os.path.join(self.main_ui.load_directory.text(), video_filename)
            video_path = path.replace('\\', '/')  # supports path for different os
            capture = cv2.VideoCapture(video_path)

            if not capture.isOpened():
                print(f"Failed to open video: {video_path}")
                continue

            success, frame = capture.read()

            if success:
                thumbnail_widget = QLabel()
                thumbnail_widget.setMaximumSize(300, 300)  # Adjust size as needed

                # Convert OpenCV frame to QImage
                qimage = QImage(
                    frame.data,
                    frame.shape[1],
                    frame.shape[0],
                    frame.shape[1] * 3,
                    QImage.Format_RGB888)

                # Convert QImage to QPixmap for thumbnail display
                pixmap = QPixmap.fromImage(qimage).scaled(
                    thumbnail_widget.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation,
                )

                thumbnail_widget.setPixmap(pixmap)
                thumbnail_widget.setCursor(Qt.PointingHandCursor)
                thumbnail_widget.mousePressEvent = lambda event, path=video_path: self.open_video_player(path)
                thumbnail_widget.setStyleSheet("""
                       QLabel {
                           background-color: rgb(33, 37, 43);
                           padding: 10px;
                           margin: 10px;
                           margin-right: 0px;
                           border: 1px solid #ccc;
                           border-radius: 5px;
                       }
                   """)

                video_label = QLabel()
                total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
                fps = int(capture.get(cv2.CAP_PROP_FPS))
                video_length_seconds = total_frames / fps
                if video_length_seconds >= 60:
                    video_length_minutes = int(video_length_seconds // 60)
                    video_length_seconds = int(video_length_seconds % 60)
                    video_length_text = "{} minutes {} seconds".format(video_length_minutes, video_length_seconds)
                else:
                    video_length_text = "{} seconds".format(int(video_length_seconds))

                video_format = str(video_path.split('.')[-1])
                fourcc = int(capture.get(cv2.CAP_PROP_FOURCC))
                video_codec = "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])

                label_text = "File Name: {}\nLength: {}\nFPS: {}\nVideo format: {}\nVideo codec: {}".format(
                    video_filename, video_length_text, fps, video_format, video_codec)
                video_label.setText(label_text)
                video_label.setStyleSheet("""
                        QLabel {
                            background-color: rgb(33, 37, 43);
                            padding: 10px;
                            margin: 10px;
                            margin-left: 0px;
                            border: 1px solid #ccc;
                            border-radius: 5px;
                        }
                    """)

                self.video_preview_grid.addWidget(thumbnail_widget, row, 0)
                self.video_preview_grid.addWidget(video_label, row, 1)

            capture.release()

    def clear_video_preview_grid(self):
        for i in reversed(range(self.video_preview_grid.count())):
            item = self.video_preview_grid.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.hide()
                    self.video_preview_grid.removeItem(item)

    def open_video_player(self, video_path):
        player_widget = VideoPlayer(self.main_ui, video_path)
        self.main_ui.stackedWidget.addWidget(player_widget)
        self.main_ui.stackedWidget.setCurrentWidget(player_widget)
