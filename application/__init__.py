import logging
import os

from PySide6.QtWidgets import QHeaderView, QMessageBox

from mainwindow import Ui_MainWindow
from application.app_settings import Settings
from application.ui_beautify import UiBeautify
from application.ui_functions import UIFunctions
from application.app_functions import AppFunctions

from widgets import VideoLoader


class App(UiBeautify):

    def __init__(self):
        super().__init__()

    def launch(self):
        self.setupUi(self)

        # APPLY TEXTS
        self.setWindowTitle(Settings.APP_NAME)
        self.titleRightInfo.setText(Settings.APP_NAME)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.connect_events()
        self.logging()

        # SHOW APP UI
        self.showFullScreen()

        # SET CUSTOM THEME
        if Settings.ENABLE_CUSTOM_THEME:
            UIFunctions.theme(self, Settings.THEME_LIGHT_PATH, True)
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        self.stackedWidget.setCurrentWidget(self.page_home)
        self.btn_home.setStyleSheet(UIFunctions.selectMenu(self.btn_home.styleSheet()))

    def logging(self):
        log_format = "%(asctime)s [%(levelname)s] %(message)s"

        if not os.path.exists(Settings.OUTPUT_DIR):
            print("Output directory not found")
            return

        output_path = os.path.join(Settings.OUTPUT_DIR, Settings.OUTPUT_FOLDER_NAME)
        if not os.path.exists(output_path):
            print("Output folder not exist, creating..")
            os.mkdir(output_path)

        log_file = os.path.join(output_path,"log_file.log")
        if os.path.exists(log_file):
            print("log file already exist, recreating..")
            os.chmod(log_file, 0o777)
            os.remove(log_file)

        logging.basicConfig(
            level=logging.INFO,  # Set the desired log level (INFO, DEBUG, ERROR, etc.)
            format=log_format,
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

    def connect_events(self):
        # TOGGLE MENU
        self.toggleButton.clicked.connect(lambda: UIFunctions.ex_toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # LEFT MENUS
        self.btn_home.clicked.connect(self.buttonClick)
        self.btn_widgets.clicked.connect(self.buttonClick)
        self.btn_load.clicked.connect(self.buttonClick)
        self.btn_exit.clicked.connect(lambda: self.quitApplication())

        # LOAD VIDEOS BUTTON CALL
        video_loader = VideoLoader(self)
        self.btn_loadVideos.clicked.connect(lambda: video_loader.load_videos())

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.ex_toggleLeftBox(self, True)

        self.toggleLeftBox.clicked.connect(openCloseLeftBox)
        self.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.ex_toggleRightBox(self, True)

        self.settingsTopBtn.setVisible(False)
        self.settingsTopBtn.clicked.connect(openCloseRightBox)

        self.btn_widgets.setVisible(False)

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            self.stackedWidget.setCurrentWidget(self.page_home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            self.stackedWidget.setCurrentWidget(self.page_widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW LOAD VIDEO PAGE
        if btnName == "btn_load":
            self.stackedWidget.setCurrentWidget(self.page_loadVideos)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def quitApplication(self):
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Are you sure you want to quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.close()
