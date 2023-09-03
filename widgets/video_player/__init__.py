from PySide6.QtWidgets import QWidget
from widgets.video_player.ui_video_player import Ui_videoPlayer


class VideoPlayer(Ui_videoPlayer, QWidget):
    def __init__(self, video_path):
        super().__init__()
        self.ui = Ui_videoPlayer()
        self.ui.setupUi(self)

        layout = self.ui.verticalLayout
        self.setLayout(layout)

    def play_video(self):
        # Add code to play the video using a video player library (e.g., OpenCV, PyQtMediaPlayer)
        pass
