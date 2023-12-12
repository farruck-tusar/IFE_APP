import sys

from PySide6.QtCore import Slot, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QGraphicsVideoItem
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene

from widgets.video_player.ui_video_player import Ui_videoPlayer
from widgets.video_player.yolo_detection import YoloDetection


class VideoPlayer(Ui_videoPlayer, QWidget):
    def __init__(self, main_ui, video_path):
        super().__init__(main_ui)
        self.ui = Ui_videoPlayer()
        self.ui.setupUi(self)

        self.ui.btn_back.clicked.connect(lambda: main_ui.stackedWidget.setCurrentWidget(main_ui.page_loadVideos))
        self.ui.btn_process.clicked.connect(lambda: YoloDetection.yolov5_detect(video_path))

        self._video_view = QGraphicsView(self.ui.frame_player)
        layout = QVBoxLayout(self.ui.frame_player)
        layout.addWidget(self._video_view)

        self._player = QMediaPlayer()
        self._player.errorOccurred.connect(self._player_error)

        self._video_item = QGraphicsVideoItem()
        self._video_view.setScene(QGraphicsScene(self))
        self._video_view.scene().addItem(self._video_item)
        self._player.setVideoOutput(self._video_item)
        self._player.setSource(video_path)

        # Initialize icons
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

        # Zoom features
        self._zoom_factor = 1.0
        self.ui.slider_zoom.valueChanged.connect(self.update_zoom)

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
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds_remainder:03}"

    def update_zoom(self, value):
        self._zoom_factor = 1.0 + value / 100 * 2.0
        self._video_item.setScale(self._zoom_factor)
