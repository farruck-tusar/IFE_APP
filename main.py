import os
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

# IMPORT / GUI AND MODULES AND WIDGETS
from application import App

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
widgets = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("resources/icon.ico"))
    window = App()
    window.launch()
    sys.exit(app.exec())
