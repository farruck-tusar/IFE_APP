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
import resources_rc

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
        self.btn_back = QPushButton(self.player)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy1)
        self.btn_back.setAutoFillBackground(False)
        self.btn_back.setStyleSheet(u"margin: 10px 0px 0px 10px;\n"
"padding: 5px;")
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon)

        self.verticalLayout.addWidget(self.btn_back)

        self.frame_video = QFrame(self.player)
        self.frame_video.setObjectName(u"frame_video")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(7)
        sizePolicy2.setHeightForWidth(self.frame_video.sizePolicy().hasHeightForWidth())
        self.frame_video.setSizePolicy(sizePolicy2)
        self.frame_video.setFrameShape(QFrame.StyledPanel)
        self.frame_video.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_video)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_player = QFrame(self.frame_video)
        self.frame_player.setObjectName(u"frame_player")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(9)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_player.sizePolicy().hasHeightForWidth())
        self.frame_player.setSizePolicy(sizePolicy3)
        self.frame_player.setFrameShape(QFrame.StyledPanel)
        self.frame_player.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_player)

        self.frame_zoom = QFrame(self.frame_video)
        self.frame_zoom.setObjectName(u"frame_zoom")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_zoom.sizePolicy().hasHeightForWidth())
        self.frame_zoom.setSizePolicy(sizePolicy4)
        self.frame_zoom.setFrameShape(QFrame.StyledPanel)
        self.frame_zoom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_zoom)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.slider_zoom = QSlider(self.frame_zoom)
        self.slider_zoom.setObjectName(u"slider_zoom")
        self.slider_zoom.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.slider_zoom, 0, Qt.AlignHCenter)

        self.label_zoom = QLabel(self.frame_zoom)
        self.label_zoom.setObjectName(u"label_zoom")

        self.verticalLayout_3.addWidget(self.label_zoom, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frame_zoom, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_video)

        self.frame_time_heatmap = QFrame(self.player)
        self.frame_time_heatmap.setObjectName(u"frame_time_heatmap")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.frame_time_heatmap.sizePolicy().hasHeightForWidth())
        self.frame_time_heatmap.setSizePolicy(sizePolicy5)
        self.frame_time_heatmap.setFrameShape(QFrame.StyledPanel)
        self.frame_time_heatmap.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_time_heatmap)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_time = QFrame(self.frame_time_heatmap)
        self.frame_time.setObjectName(u"frame_time")
        self.frame_time.setFrameShape(QFrame.StyledPanel)
        self.frame_time.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_time)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slider_time = QSlider(self.frame_time)
        self.slider_time.setObjectName(u"slider_time")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(8)
        sizePolicy6.setVerticalStretch(8)
        sizePolicy6.setHeightForWidth(self.slider_time.sizePolicy().hasHeightForWidth())
        self.slider_time.setSizePolicy(sizePolicy6)
        self.slider_time.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.slider_time)

        self.label_time = QLabel(self.frame_time)
        self.label_time.setObjectName(u"label_time")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(2)
        sizePolicy7.setVerticalStretch(2)
        sizePolicy7.setHeightForWidth(self.label_time.sizePolicy().hasHeightForWidth())
        self.label_time.setSizePolicy(sizePolicy7)

        self.horizontalLayout_3.addWidget(self.label_time, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_time)

        self.frame_heatmap = QFrame(self.frame_time_heatmap)
        self.frame_heatmap.setObjectName(u"frame_heatmap")
        self.frame_heatmap.setFrameShape(QFrame.StyledPanel)
        self.frame_heatmap.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_heatmap)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slider_heatmap = QSlider(self.frame_heatmap)
        self.slider_heatmap.setObjectName(u"slider_heatmap")
        sizePolicy6.setHeightForWidth(self.slider_heatmap.sizePolicy().hasHeightForWidth())
        self.slider_heatmap.setSizePolicy(sizePolicy6)
        self.slider_heatmap.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.slider_heatmap)

        self.label_heatmap = QLabel(self.frame_heatmap)
        self.label_heatmap.setObjectName(u"label_heatmap")
        sizePolicy7.setHeightForWidth(self.label_heatmap.sizePolicy().hasHeightForWidth())
        self.label_heatmap.setSizePolicy(sizePolicy7)

        self.horizontalLayout_4.addWidget(self.label_heatmap, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_heatmap)


        self.verticalLayout.addWidget(self.frame_time_heatmap)

        self.frame_nav_buttons = QFrame(self.player)
        self.frame_nav_buttons.setObjectName(u"frame_nav_buttons")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.frame_nav_buttons.sizePolicy().hasHeightForWidth())
        self.frame_nav_buttons.setSizePolicy(sizePolicy8)
        self.frame_nav_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_nav_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_nav_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_play = QPushButton(self.frame_nav_buttons)
        self.btn_play.setObjectName(u"btn_play")

        self.horizontalLayout.addWidget(self.btn_play)

        self.btn_stop = QPushButton(self.frame_nav_buttons)
        self.btn_stop.setObjectName(u"btn_stop")

        self.horizontalLayout.addWidget(self.btn_stop)

        self.spin_speed = QDoubleSpinBox(self.frame_nav_buttons)
        self.spin_speed.setObjectName(u"spin_speed")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.spin_speed.sizePolicy().hasHeightForWidth())
        self.spin_speed.setSizePolicy(sizePolicy9)

        self.horizontalLayout.addWidget(self.spin_speed)

        self.combo_filter = QComboBox(self.frame_nav_buttons)
        self.combo_filter.setObjectName(u"combo_filter")

        self.horizontalLayout.addWidget(self.combo_filter)

        self.btn_process = QPushButton(self.frame_nav_buttons)
        self.btn_process.setObjectName(u"btn_process")

        self.horizontalLayout.addWidget(self.btn_process)


        self.verticalLayout.addWidget(self.frame_nav_buttons)


        self.horizontalLayout_2.addWidget(self.player)

        self.sidebar = QFrame(videoPlayer)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(3)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy10)
        self.sidebar.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.sidebar)


        self.retranslateUi(videoPlayer)

        QMetaObject.connectSlotsByName(videoPlayer)
    # setupUi

    def retranslateUi(self, videoPlayer):
        videoPlayer.setWindowTitle(QCoreApplication.translate("videoPlayer", u"Form", None))
        self.btn_back.setText(QCoreApplication.translate("videoPlayer", u"Back", None))
        self.label_zoom.setText(QCoreApplication.translate("videoPlayer", u"1,0 x", None))
        self.label_time.setText(QCoreApplication.translate("videoPlayer", u"00:00:00.000/00:00:00.000", None))
        self.label_heatmap.setText(QCoreApplication.translate("videoPlayer", u"Heat-map label", None))
        self.btn_play.setText(QCoreApplication.translate("videoPlayer", u"Play", None))
        self.btn_stop.setText(QCoreApplication.translate("videoPlayer", u"Stop", None))
        self.btn_process.setText(QCoreApplication.translate("videoPlayer", u"Process Video", None))
    # retranslateUi

