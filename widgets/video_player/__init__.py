import sys

import ffmpeg

from PySide6.QtCore import Slot
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout
from widgets.video_player.ui_video_player import Ui_videoPlayer


class VideoPlayer(Ui_videoPlayer, QWidget):
    def __init__(self, main_ui, video_path):
        super().__init__(main_ui)

        self.main_ui = main_ui
        self.ui = Ui_videoPlayer()
        self.ui.setupUi(self)

        self.ui.btn_back.clicked.connect(lambda: self.main_ui.stackedWidget.setCurrentWidget(self.main_ui.page_loadVideos))

        # Use ffmpeg to probe the video file
        probe = ffmpeg.probe(video_path, v="error", select_streams="v:0", show_entries="stream=codec_name")
        video_codec = probe['streams'][0]['codec_name']

        # Check if the video codec is compatible with hardware acceleration
        supported_codecs = ['h264', 'hevc']  # Add more if needed
        if video_codec.lower() not in supported_codecs:
            print(f"Unsupported video codec: {video_codec}")
            return

        self._video_widget = QVideoWidget()
        frame_player_layout = QVBoxLayout(self.ui.frame_player)
        frame_player_layout.addWidget(self._video_widget)

        self._player = QMediaPlayer()
        self._player.errorOccurred.connect(self._player_error)

        # Disable hardware acceleration
        self._player.setProperty("no-video-signal", True)

        self._player.setSource(video_path)
        self._player.setVideoOutput(self._video_widget)

        self._audio_output = QAudioOutput()
        self._player.setAudioOutput(self._audio_output)

        self._play_action = self.ui.btn_play
        self._play_action.clicked.connect(self._player.play)

        self._stop_action = self.ui.btn_stop
        self._stop_action.clicked.connect(self._player.pause)

        self._player.playbackStateChanged.connect(self.update_buttons)

    @Slot("QMediaPlayer::PlaybackState")
    def update_buttons(self, state):
        self._play_action.setEnabled(state != QMediaPlayer.PlayingState)
        self._stop_action.setEnabled(state != QMediaPlayer.StoppedState)

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
