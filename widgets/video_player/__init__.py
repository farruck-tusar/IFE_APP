import sys

from PySide6.QtCore import Slot
from PySide6.QtMultimedia import (QAudioOutput,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QSlider)
from PySide6.QtWidgets import QWidget, QVBoxLayout

from widgets.video_player.ui_video_player import Ui_videoPlayer


class VideoPlayer(Ui_videoPlayer, QWidget):
    def __init__(self, video_path):
        super().__init__()
        self.ui = Ui_videoPlayer()
        self.ui.setupUi(self)

        self._playlist = []
        self._playlist_index = -1
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._player.errorOccurred.connect(self._player_error)
        self._player.setSource(video_path)
        self._playlist.append(video_path)
        self._playlist_index = len(self._playlist) - 1
        self._player.setSource(video_path)
        self._player.play()

        self._volume_slider = QSlider()
        self._volume_slider.setMinimum(0)
        self._volume_slider.setMaximum(100)
        available_width = self.screen().availableGeometry().width()
        self._volume_slider.setFixedWidth(available_width / 10)
        self._volume_slider.setValue(self._audio_output.volume())
        self._volume_slider.setTickInterval(10)
        self._volume_slider.setTickPosition(QSlider.TicksBelow)
        self._volume_slider.setToolTip("Volume")
        self._volume_slider.valueChanged.connect(self._audio_output.setVolume)

        self._play_action = self.ui.btn_play
        self._play_action.clicked.connect(self._player.play)
        self._stop_action = self.ui.btn_stop
        self._stop_action.clicked.connect(self._player.pause)

        self._video_widget = QVideoWidget()
        self._player.playbackStateChanged.connect(self.update_buttons)
        frame_player_layout = QVBoxLayout(self.ui.frame_player)
        frame_player_layout.addWidget(self._video_widget)

        self._player.setVideoOutput(self._video_widget)

        self.update_buttons(self._player.playbackState())

    def closeEvent(self, event):
        self._ensure_stopped()
        event.accept()

    @Slot()
    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()

    @Slot("QMediaPlayer::PlaybackState")
    def update_buttons(self, state):
        media_count = len(self._playlist)
        self._play_action.setEnabled(media_count > 0
                                     and state != QMediaPlayer.PlayingState)
        self._stop_action.setEnabled(state != QMediaPlayer.StoppedState)

    @Slot("QMediaPlayer::Error", str)
    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)
