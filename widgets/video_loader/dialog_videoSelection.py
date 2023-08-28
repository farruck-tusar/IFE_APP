from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QDialog, QVBoxLayout, QListWidget, QPushButton


class VideoSelectionDialog(QDialog):
    def __init__(self, video_files, parent=None):
        super().__init__(parent)
        self.selected_videos = []

        self.setWindowTitle("Select Videos")
        # Open dialog in the center of the screen
        self.setGeometry(0, 0, 400, 300)
        center = QGuiApplication.screens()[0].geometry().center()
        self.move(center - self.frameGeometry().center())

        layout = QVBoxLayout()

        self.video_list_widget = QListWidget()
        self.video_list_widget.setSelectionMode(QListWidget.MultiSelection)
        self.video_list_widget.addItems(video_files)
        layout.addWidget(self.video_list_widget)

        self.select_button = QPushButton("Select")
        self.select_button.clicked.connect(self.select_videos)
        layout.addWidget(self.select_button)

        self.setLayout(layout)

    def select_videos(self):
        selected_items = self.video_list_widget.selectedItems()
        self.selected_videos = [item.text() for item in selected_items]
        self.accept()
