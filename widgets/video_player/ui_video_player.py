# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_video_player.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_videoPlayer(object):
    def setupUi(self, videoPlayer):
        if not videoPlayer.objectName():
            videoPlayer.setObjectName(u"videoPlayer")
        videoPlayer.resize(755, 506)
        self.verticalLayout_2 = QVBoxLayout(videoPlayer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(videoPlayer)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(videoPlayer)

        QMetaObject.connectSlotsByName(videoPlayer)
    # setupUi

    def retranslateUi(self, videoPlayer):
        videoPlayer.setWindowTitle(QCoreApplication.translate("videoPlayer", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("videoPlayer", u"Play Video", None))
    # retranslateUi

