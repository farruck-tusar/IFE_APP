from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QWidget
from widgets.video_player.ui_video_player import Ui_videoPlayer


class VideoPlayer(Ui_videoPlayer, QWidget):
    def __init__(self, video_path):
        super().__init__()
        self.ui = Ui_videoPlayer()
        self.ui.setupUi(self)

        self.video_path = video_path
        self.media_player = QMediaPlayer()

        # Set up the video display widget
        self.video_widget = self.ui.frame_player
        self.media_player.setVideoOutput(self.video_widget)

        # Connect the Play button to the play_video method
        self.ui.btn_play.clicked.connect(self.play_video)

    def play_video(self):
        # Add code to play the video using a video player library (e.g., OpenCV, PyQtMediaPlayer)
        pass
