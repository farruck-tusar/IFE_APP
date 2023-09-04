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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_videoPlayer(object):
    def setupUi(self, videoPlayer):
        if not videoPlayer.objectName():
            videoPlayer.setObjectName(u"videoPlayer")
        videoPlayer.resize(1040, 575)
        self.horizontalLayout_2 = QHBoxLayout(videoPlayer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.player = QFrame(videoPlayer)
        self.player.setObjectName(u"player")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy)
        self.player.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.player.setFrameShape(QFrame.StyledPanel)
        self.player.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.player)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.player)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(7)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_player = QFrame(self.frame)
        self.frame_player.setObjectName(u"frame_player")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(9)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_player.sizePolicy().hasHeightForWidth())
        self.frame_player.setSizePolicy(sizePolicy2)
        self.frame_player.setFrameShape(QFrame.StyledPanel)
        self.frame_player.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_player)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSlider = QSlider(self.frame_7)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.verticalSlider, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.player)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSlider = QSlider(self.frame_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(8)
        sizePolicy5.setVerticalStretch(8)
        sizePolicy5.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy5)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(2)
        sizePolicy6.setVerticalStretch(2)
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSlider_2 = QSlider(self.frame_5)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        sizePolicy5.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy5)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.horizontalSlider_2)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.label_2, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.player)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy7)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_play = QPushButton(self.frame_3)
        self.btn_play.setObjectName(u"btn_play")

        self.horizontalLayout.addWidget(self.btn_play)

        self.btn_stop = QPushButton(self.frame_3)
        self.btn_stop.setObjectName(u"btn_stop")

        self.horizontalLayout.addWidget(self.btn_stop)

        self.spin_speed = QDoubleSpinBox(self.frame_3)
        self.spin_speed.setObjectName(u"spin_speed")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.spin_speed.sizePolicy().hasHeightForWidth())
        self.spin_speed.setSizePolicy(sizePolicy8)

        self.horizontalLayout.addWidget(self.spin_speed)

        self.combo_filter = QComboBox(self.frame_3)
        self.combo_filter.setObjectName(u"combo_filter")

        self.horizontalLayout.addWidget(self.combo_filter)

        self.btn_process = QPushButton(self.frame_3)
        self.btn_process.setObjectName(u"btn_process")

        self.horizontalLayout.addWidget(self.btn_process)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.player)

        self.sidebar = QFrame(videoPlayer)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(3)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy9)
        self.sidebar.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.sidebar)


        self.retranslateUi(videoPlayer)

        QMetaObject.connectSlotsByName(videoPlayer)
    # setupUi

    def retranslateUi(self, videoPlayer):
        videoPlayer.setWindowTitle(QCoreApplication.translate("videoPlayer", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("videoPlayer", u"1,0 x", None))
        self.label.setText(QCoreApplication.translate("videoPlayer", u"00:00:00.000/00:00:00.000", None))
        self.label_2.setText(QCoreApplication.translate("videoPlayer", u"Heat-map label", None))
        self.btn_play.setText(QCoreApplication.translate("videoPlayer", u"Play", None))
        self.btn_stop.setText(QCoreApplication.translate("videoPlayer", u"Stop", None))
        self.btn_process.setText(QCoreApplication.translate("videoPlayer", u"Process Video", None))
    # retranslateUi

