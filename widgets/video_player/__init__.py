import sys
import ffmpeg
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from widgets.video_player.ui_video_player import Ui_videoPlayer


class VideoPlayer(Ui_videoPlayer, QWidget):
    def __init__(self, main_ui, video_path):
        super().__init__(main_ui)
        self.ui = Ui_videoPlayer()
        self.ui.setupUi(self)

        self.ui.btn_back.clicked.connect(lambda: main_ui.stackedWidget.setCurrentWidget(main_ui.page_loadVideos))

        self._video_widget = QVideoWidget()
        QVBoxLayout(self.ui.frame_player).addWidget(self._video_widget)

        self._player = QMediaPlayer()
        self._player.errorOccurred.connect(self._player_error)

        # Disable hardware acceleration
        self._player.setProperty("no-video-signal", True)

        self._player.setSource(video_path)
        self._player.setVideoOutput(self._video_widget)

        self._play_action = self.ui.btn_play
        self._play_action.clicked.connect(self._player.play)

        self._stop_action = self.ui.btn_stop
        self._stop_action.clicked.connect(self._player.stop)

        self._player.playbackStateChanged.connect(self.update_buttons)

    @Slot("QMediaPlayer::PlaybackState")
    def update_buttons(self, state):
        self._stop_action.setEnabled(state != QMediaPlayer.StoppedState)

        if state == QMediaPlayer.PlayingState:
            self._play_action.setText("Pause")
            self._play_action.setIcon(QIcon(":icons/icons/cil-media-pause.png"))
            self._play_action.clicked.disconnect()
            self._play_action.clicked.connect(self._player.pause)
        elif state == QMediaPlayer.PausedState:
            self._play_action.setText("Play")
            self._play_action.setIcon(QIcon(":icons/icons/cil-media-play.png"))
            self._play_action.clicked.disconnect()
            self._play_action.clicked.connect(self._player.play)
        elif state == QMediaPlayer.StoppedState:
            self._play_action.setText("Play")
            self._play_action.setIcon(QIcon(":icons/icons/cil-media-play.png"))
            self._play_action.clicked.disconnect()
            self._play_action.clicked.connect(self._player.play)

        duration = self._player.duration()
        position = self._player.position()
        formatted_position = self.format_time(position)
        formatted_duration = self.format_time(duration)
        self.ui.label_time.setText(f"{formatted_position}/{formatted_duration}")
        self.ui.slider_time.setValue(position)

    @Slot("QMediaPlayer::Error", str)
    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)

    def closeEvent(self, event):
        self._ensure_stopped()
        event.accept()

    @Slot()
    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()

    @Slot("qint64")
    def update_video_position(self, position):
        duration = self._player.duration()
        formatted_position = self.format_time(position)
        formatted_duration = self.format_time(duration)
        self.ui.label_time.setText(f"{formatted_position}/{formatted_duration}")
        self.ui.slider_time.setValue(position)

    def format_time(self, milliseconds):
        total_seconds = milliseconds // 1000
        milliseconds_remainder = milliseconds % 1000
        seconds = total_seconds % 60
        minutes = (total_seconds // 60) % 60
        hours = total_seconds // 3600
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds_remainder:03}"