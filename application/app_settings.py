import os


class Settings(object):

    APP_NAME = "IFE APPLICATION"

    ROOT_DIR = os.path.abspath(os.curdir)
    VENV_DIR = os.path.join(ROOT_DIR, 'venv')
    OUTPUT_DIR = os.path.expanduser("~/Documents")
    OUTPUT_FOLDER_NAME = "IFE_OUTPUT"
    YOLO_VERSION="yolov5"
    WEIGHT_FILE_NAME = "yolov5s.pt"
    YOLO_WEIGHT_DIR = os.path.join(OUTPUT_DIR, OUTPUT_FOLDER_NAME, WEIGHT_FILE_NAME)

    ENABLE_CUSTOM_THEME = False         # USE "True" FOR LIGHT THEME, "False" FOR DARK THEME
    ENABLE_CUSTOM_TITLE_BAR = False     # USE "True" FOR WINDOWS, "False" FOR MAC OR LINUX

    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500

    SUPPORTED_VIDEO_EXT = [".mp4", ".avi", ".mkv", ".mov", ".mpeg"]
    THEME_LIGHT_PATH = "resources/themes/theme_light.qss"

    # DEFAULT STYLESHEET
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"
    MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: rgb(40, 44, 52);
        """
