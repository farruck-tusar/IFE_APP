import sys

from PySide6.QtCore import Slot, QTimer, Qt
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QGraphicsVideoItem
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QSizePolicy

from widgets.video_player.ui_video_player import Ui_videoPlayer
from widgets.models.yolo_detection import YoloDetection


class VideoGraphicsView(QGraphicsView):
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.scene() and len(self.scene().items()) > 0:
            self.fitInView(self.scene().items()[0], Qt.KeepAspectRatio)


class VideoPlayer(Ui_videoPlayer, QWidget):
    def __init__(self, main_ui, video_path):
        super().__init__(main_ui)
        self.ui = Ui_videoPlayer()
        self.ui.setupUi(self)
        self.ui.btn_back.clicked.connect(lambda: main_ui.stackedWidget.setCurrentWidget(main_ui.page_loadVideos))

        self.setup_ui_elements(video_path)
        self.setup_video_player(video_path)

    def setup_ui_elements(self, video_path):
        self.ui.slider_zoom.valueChanged.connect(self.update_zoom)
        self.ui.label_zoom.setText("1.00x")
        self.ui.combo_filter.addItems(["YOLOv5 Model", "YOLOv8 Model", "Burn Mark Detection"])
        self.ui.btn_process.clicked.connect(lambda: self.process_video_with_selected_filter(video_path))

    def setup_video_player(self, video_path):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.ui.frame_player.setLayout(layout)

        self._video_view = VideoGraphicsView(self.ui.frame_player)
        self._video_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._video_view.setAlignment(Qt.AlignCenter)
        self.ui.frame_player.layout().addWidget(self._video_view)

        self._video_item = QGraphicsVideoItem()
        self._video_item.setAspectRatioMode(Qt.IgnoreAspectRatio)
        self._video_view.fitInView(self._video_item, Qt.KeepAspectRatio)
        self._video_view.setScene(QGraphicsScene(self))
        self._video_view.scene().addItem(self._video_item)

        self._player = QMediaPlayer()
        self._player.errorOccurred.connect(self._player_error)
        self._player.setVideoOutput(self._video_item)
        self._player.setSource(video_path)

        self._play_icon = QIcon(":icons/icons/cil-media-play.png")
        self._pause_icon = QIcon(":icons/icons/cil-media-pause.png")
        self._play_action = self.ui.btn_play
        self._play_action.setIcon(self._play_icon)
        self._play_action.clicked.connect(self.toggle_play_pause)

        self._stop_action = self.ui.btn_stop
        self._stop_action.clicked.connect(self._player.stop)

        self._player.playbackStateChanged.connect(self.update_buttons)

        self._update_timer = QTimer(self)
        self._update_timer.timeout.connect(self.update_video_position)
        self._update_timer.start(100)

        self._zoom_factor = 1.0

    def process_video_with_selected_filter(self, video_path):
        selected_option = self.ui.combo_filter.currentText()
        print(f"Selected option: {selected_option}")
        try:
            if selected_option == "YOLOv5 Model":
                print(selected_option)
                YoloDetection.yolov5_detect(video_path)
            elif selected_option == "YOLOv8 Model":
                print(selected_option)
                YoloDetection.yolov8_detect(video_path)
            else:
                print("Burn Mark Detection")
        except Exception as e:
            print(f"Error processing video: {e}")

    @Slot("QMediaPlayer::PlaybackState")
    def update_buttons(self, state):
        self._stop_action.setEnabled(state != QMediaPlayer.StoppedState)
        if state == QMediaPlayer.PlayingState:
            self._play_action.setText("Pause")
            self._play_action.setIcon(self._pause_icon)
        else:
            self._play_action.setText("Play")
            self._play_action.setIcon(self._play_icon)

    @Slot("QMediaPlayer::Error", str)
    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)

    def toggle_play_pause(self):
        if self._player.playbackState() == QMediaPlayer.PlayingState:
            self._player.pause()
        else:
            self._player.play()

    def closeEvent(self, event):
        self._ensure_stopped()
        event.accept()

    @Slot()
    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()

    def update_video_position(self):
        if self._player.duration() > 0:
            position = self._player.position()
            duration = self._player.duration()
            formatted_position = self.format_time(position)
            formatted_duration = self.format_time(duration)
            self.ui.label_time.setText(f"{formatted_position}/{formatted_duration}")
            self.ui.slider_time.setMaximum(duration)
            self.ui.slider_time.setValue(position)

    @staticmethod
    def format_time(milliseconds):
        total_seconds = milliseconds // 1000
        milliseconds_remainder = milliseconds % 1000
        seconds = total_seconds % 60
        minutes = (total_seconds // 60) % 60
        hours = total_seconds // 3600
        return f"{minutes:02}:{seconds:02}.{milliseconds_remainder:03}"

    def update_zoom(self, value):
        new_zoom_factor = 1.0 + value / 100 * 2.0
        scale_factor = new_zoom_factor / self._zoom_factor
        self._zoom_factor = new_zoom_factor
        current_pos = self._video_item.pos()
        viewport_center = self._video_view.mapToScene(self._video_view.viewport().rect().center())
        offset = viewport_center - current_pos
        new_pos = viewport_center - offset * scale_factor
        self._video_item.setScale(self._zoom_factor)
        self._video_item.setPos(new_pos)
        self.ui.label_zoom.setText(f"{self._zoom_factor:.2f}x")
