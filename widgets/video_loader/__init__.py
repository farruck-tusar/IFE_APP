import os
import cv2

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QDir
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget, QFileDialog, QVBoxLayout
from widgets.video_loader.dialog_videoSelection import VideoSelectionDialog
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
            video_files = [f for f in os.listdir(selected_folder) if f.lower().endswith(('.mp4', '.avi', '.mkv'))]

            dialog = VideoSelectionDialog(video_files, self)
            if dialog.exec():
                self.selected_videos = dialog.selected_videos
                self.update_video_preview_grid()

    def update_video_preview_grid(self):
        self.clear_video_preview_grid()
        thumbnail_container = QtWidgets.QWidget()
        thumbnail_layout = QVBoxLayout(thumbnail_container)
        thumbnail_container.setStyleSheet("border: 2px solid rgb(33, 37, 43); border-radius: 5px;")

        for video_filename in self.selected_videos:
            video_path = os.path.join(self.main_ui.load_directory.text(), video_filename)
            capture = cv2.VideoCapture(video_path)

            if not capture.isOpened():
                print(f"Failed to open video: {video_path}")
                continue

            success, frame = capture.read()

            if success:
                thumbnail_widget = QtWidgets.QLabel()
                thumbnail_widget.setMaximumSize(150, 150)  # Adjust size as needed

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
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation,
                )

                thumbnail_widget.setPixmap(pixmap)
                thumbnail_widget.mousePressEvent = lambda event, path=video_path: self.open_video_player(path)

                video_label = QtWidgets.QLabel()
                video_label.setText(video_filename)
                video_label.setMaximumSize(150, 30)

                thumbnail_layout.addWidget(video_label)
                thumbnail_layout.addWidget(thumbnail_widget)

            capture.release()

            self.video_preview_grid.addWidget(thumbnail_container)

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