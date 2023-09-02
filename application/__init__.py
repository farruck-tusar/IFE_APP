from PySide6.QtWidgets import QHeaderView

from application.app_settings import Settings
from mainwindow import Ui_MainWindow
from application.ui_beautify import UiBeautify
from application.ui_functions import UIFunctions
from application.app_functions import AppFunctions

from widgets import VideoLoader


class App(UiBeautify):

    def __init__(self):
        super().__init__()

    def launch(self):
        self.setupUi(self)

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = False

        # APP NAME
        title = "IFE Application"
        description = "IFE APPLICATION"

        # APPLY TEXTS
        self.setWindowTitle(title)
        self.titleRightInfo.setText(description)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.connect_events()

        # SHOW APP UI
        self.show()

        # SET CUSTOM THEME
        useCustomTheme = False
        themeFileLight = "resources/themes/theme_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFileLight, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        self.stackedWidget.setCurrentWidget(self.page_home)
        self.btn_home.setStyleSheet(UIFunctions.selectMenu(self.btn_home.styleSheet()))

    def connect_events(self):
        # TOGGLE MENU
        self.toggleButton.clicked.connect(lambda: UIFunctions.ex_toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # LEFT MENUS
        self.btn_home.clicked.connect(self.buttonClick)
        self.btn_widgets.clicked.connect(self.buttonClick)
        self.btn_load.clicked.connect(self.buttonClick)
        self.btn_exit.clicked.connect(lambda: self.close())

        # LOAD VIDEOS BUTTON CALL
        video_loader = VideoLoader(self)  # Create an instance of VideoLoader
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

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # BUTTONS CLICK
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