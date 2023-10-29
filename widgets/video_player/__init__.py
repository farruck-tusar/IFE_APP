import subprocess
import sys
import os

from PySide6.QtCore import Slot, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout

from widgets.video_player.ui_video_player import Ui_videoPlayer


def run_yolov5_detection(video_path):
    # Replace the command with the actual YOLOv5 detection script command.
    # Here we assume 'detect.py' is in the same directory as the script.
    ROOT_DIR = os.path.abspath(os.curdir)
    print(ROOT_DIR)
    print(video_path)
    command = ["python", ROOT_DIR + "/yolov5/detect.py", "--source", video_path, "--weights", ROOT_DIR + "/yolov5/yolov5s.pt"]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    output, errors = process.communicate()

    if process.returncode == 0:
        print("YOLOv5 Detection Successful.")
    else:
        print("YOLOv5 Detection Failed.")
        print(errors)


class VideoPlayer(Ui_videoPlayer, QWidget):
    def __init__(self, main_ui, video_path):
        super().__init__(main_ui)
        self.ui = Ui_videoPlayer()
        self.ui.setupUi(self)

        self.ui.btn_back.clicked.connect(lambda: main_ui.stackedWidget.setCurrentWidget(main_ui.page_loadVideos))
        self.ui.btn_process.clicked.connect(lambda: run_yolov5_detection(video_path))

        self._video_widget = QVideoWidget()
        QVBoxLayout(self.ui.frame_player).addWidget(self._video_widget)

        self._player = QMediaPlayer()
        self._player.errorOccurred.connect(self._player_error)

        self._player.setVideoOutput(self._video_widget)
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
