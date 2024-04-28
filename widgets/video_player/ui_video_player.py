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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSpinBox,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import resources.resources_rc

class Ui_videoPlayer(object):
    def setupUi(self, videoPlayer):
        if not videoPlayer.objectName():
            videoPlayer.setObjectName(u"videoPlayer")
        videoPlayer.resize(1440, 787)
        videoPlayer.setStyleSheet(u"#videoPlayer QPushButton, QLineEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QComboBox {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding:5px;\n"
"}\n"
"#sidebar QPushButton {\n"
"	padding:0px;\n"
"}\n"
"#scrollArea {\n"
"	border: 0px;\n"
"}\n"
"#videoPlayer QPushButton:hover, QLineEdit:hover, QSpinBox:hover, QDoubleSpinBox:hover, QDateEdit:hover, QComboBox:hover {\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#videoPlayer QPushButton:pressed, QComboBox:pressed {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(videoPlayer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.player = QFrame(videoPlayer)
        self.player.setObjectName(u"player")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy)
        self.player.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.player.setFrameShape(QFrame.StyledPanel)
        self.player.setFrameShadow(QFrame.Raised)
        self.player.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.player)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_back = QPushButton(self.player)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy1)
        self.btn_back.setAutoFillBackground(False)
        self.btn_back.setStyleSheet(u"margin: 5px 5px 5px 5px;\n"
"padding: 5px;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setAutoDefault(False)

        self.verticalLayout.addWidget(self.btn_back)

        self.frame_video = QFrame(self.player)
        self.frame_video.setObjectName(u"frame_video")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.frame_video.sizePolicy().hasHeightForWidth())
        self.frame_video.setSizePolicy(sizePolicy2)
        self.frame_video.setFrameShape(QFrame.StyledPanel)
        self.frame_video.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_video)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_player = QFrame(self.frame_video)
        self.frame_player.setObjectName(u"frame_player")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_player.sizePolicy().hasHeightForWidth())
        self.frame_player.setSizePolicy(sizePolicy3)
        self.frame_player.setFrameShape(QFrame.StyledPanel)
        self.frame_player.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_player)

        self.frame_zoom = QFrame(self.frame_video)
        self.frame_zoom.setObjectName(u"frame_zoom")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_time_heatmap.sizePolicy().hasHeightForWidth())
        self.frame_time_heatmap.setSizePolicy(sizePolicy5)
        self.frame_time_heatmap.setFrameShape(QFrame.StyledPanel)
        self.frame_time_heatmap.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_time_heatmap)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_time = QFrame(self.frame_time_heatmap)
        self.frame_time.setObjectName(u"frame_time")
        self.frame_time.setAutoFillBackground(False)
        self.frame_time.setFrameShape(QFrame.StyledPanel)
        self.frame_time.setFrameShadow(QFrame.Raised)
        self.frame_time.setLineWidth(1)
        self.frame_time.setMidLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_time)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slider_time = QSlider(self.frame_time)
        self.slider_time.setObjectName(u"slider_time")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.slider_time.sizePolicy().hasHeightForWidth())
        self.slider_time.setSizePolicy(sizePolicy6)
        self.slider_time.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.slider_time)

        self.label_time = QLabel(self.frame_time)
        self.label_time.setObjectName(u"label_time")
        sizePolicy1.setHeightForWidth(self.label_time.sizePolicy().hasHeightForWidth())
        self.label_time.setSizePolicy(sizePolicy1)
        self.label_time.setMinimumSize(QSize(200, 0))

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
        sizePolicy1.setHeightForWidth(self.label_heatmap.sizePolicy().hasHeightForWidth())
        self.label_heatmap.setSizePolicy(sizePolicy1)
        self.label_heatmap.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_4.addWidget(self.label_heatmap, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_heatmap)


        self.verticalLayout.addWidget(self.frame_time_heatmap)

        self.frame_nav_buttons = QFrame(self.player)
        self.frame_nav_buttons.setObjectName(u"frame_nav_buttons")
        sizePolicy4.setHeightForWidth(self.frame_nav_buttons.sizePolicy().hasHeightForWidth())
        self.frame_nav_buttons.setSizePolicy(sizePolicy4)
        self.frame_nav_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_nav_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_nav_buttons)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 0, 12, 12)
        self.btn_play = QPushButton(self.frame_nav_buttons)
        self.btn_play.setObjectName(u"btn_play")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_play)

        self.btn_stop = QPushButton(self.frame_nav_buttons)
        self.btn_stop.setObjectName(u"btn_stop")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stop.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_stop)

        self.spin_speed = QDoubleSpinBox(self.frame_nav_buttons)
        self.spin_speed.setObjectName(u"spin_speed")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.spin_speed.sizePolicy().hasHeightForWidth())
        self.spin_speed.setSizePolicy(sizePolicy7)

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
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(3)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy8)
        self.sidebar.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.sidebar)
#ifndef Q_OS_MAC
        self.verticalLayout_4.setSpacing(-1)
#endif
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.sidebar)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 318, 944))
        self.verticalLayout1 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout1.setSpacing(6)
        self.verticalLayout1.setObjectName(u"verticalLayout1")
        self.verticalLayout1.setContentsMargins(0, 0, 0, 0)
        self.groupBox_General = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_General.setObjectName(u"groupBox_General")
        font = QFont()
        font.setBold(False)
        self.groupBox_General.setFont(font)
        self.groupBox_General.setFlat(False)
        self.groupBox_General.setCheckable(False)
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_General)
        self.verticalLayout_31.setSpacing(3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(-1, 24, -1, -1)
        self.layout_G1 = QFormLayout()
        self.layout_G1.setObjectName(u"layout_G1")
        self.layout_G1.setHorizontalSpacing(9)
        self.layout_G1.setVerticalSpacing(3)
        self.label_file_name = QLabel(self.groupBox_General)
        self.label_file_name.setObjectName(u"label_file_name")

        self.layout_G1.setWidget(0, QFormLayout.LabelRole, self.label_file_name)

        self.label_file_name_value = QLabel(self.groupBox_General)
        self.label_file_name_value.setObjectName(u"label_file_name_value")
        self.label_file_name_value.setStyleSheet(u"padding: 5px;")

        self.layout_G1.setWidget(0, QFormLayout.FieldRole, self.label_file_name_value)

        self.label_record_date = QLabel(self.groupBox_General)
        self.label_record_date.setObjectName(u"label_record_date")
        sizePolicy4.setHeightForWidth(self.label_record_date.sizePolicy().hasHeightForWidth())
        self.label_record_date.setSizePolicy(sizePolicy4)
        self.label_record_date.setMinimumSize(QSize(0, 0))
        self.label_record_date.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(1, QFormLayout.LabelRole, self.label_record_date)

        self.dateEdit_record_date = QDateEdit(self.groupBox_General)
        self.dateEdit_record_date.setObjectName(u"dateEdit_record_date")
        sizePolicy4.setHeightForWidth(self.dateEdit_record_date.sizePolicy().hasHeightForWidth())
        self.dateEdit_record_date.setSizePolicy(sizePolicy4)
        self.dateEdit_record_date.setMinimumSize(QSize(0, 0))
        self.dateEdit_record_date.setMaximumSize(QSize(16777215, 16777215))
        self.dateEdit_record_date.setLocale(QLocale(QLocale.English, QLocale.World))

        self.layout_G1.setWidget(1, QFormLayout.FieldRole, self.dateEdit_record_date)

        self.label_com_name = QLabel(self.groupBox_General)
        self.label_com_name.setObjectName(u"label_com_name")
        sizePolicy4.setHeightForWidth(self.label_com_name.sizePolicy().hasHeightForWidth())
        self.label_com_name.setSizePolicy(sizePolicy4)
        self.label_com_name.setMinimumSize(QSize(0, 0))
        self.label_com_name.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(2, QFormLayout.LabelRole, self.label_com_name)

        self.lineEdit_com_name = QLineEdit(self.groupBox_General)
        self.lineEdit_com_name.setObjectName(u"lineEdit_com_name")
        sizePolicy4.setHeightForWidth(self.lineEdit_com_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_com_name.setSizePolicy(sizePolicy4)
        self.lineEdit_com_name.setMinimumSize(QSize(0, 0))
        self.lineEdit_com_name.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(2, QFormLayout.FieldRole, self.lineEdit_com_name)

        self.label_bra_name = QLabel(self.groupBox_General)
        self.label_bra_name.setObjectName(u"label_bra_name")
        sizePolicy4.setHeightForWidth(self.label_bra_name.sizePolicy().hasHeightForWidth())
        self.label_bra_name.setSizePolicy(sizePolicy4)
        self.label_bra_name.setMinimumSize(QSize(0, 0))
        self.label_bra_name.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(3, QFormLayout.LabelRole, self.label_bra_name)

        self.comboBox_bra_name = QComboBox(self.groupBox_General)
        self.comboBox_bra_name.setObjectName(u"comboBox_bra_name")
        sizePolicy4.setHeightForWidth(self.comboBox_bra_name.sizePolicy().hasHeightForWidth())
        self.comboBox_bra_name.setSizePolicy(sizePolicy4)
        self.comboBox_bra_name.setMinimumSize(QSize(0, 0))
        self.comboBox_bra_name.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(3, QFormLayout.FieldRole, self.comboBox_bra_name)

        self.label_pl_name = QLabel(self.groupBox_General)
        self.label_pl_name.setObjectName(u"label_pl_name")
        sizePolicy4.setHeightForWidth(self.label_pl_name.sizePolicy().hasHeightForWidth())
        self.label_pl_name.setSizePolicy(sizePolicy4)
        self.label_pl_name.setMinimumSize(QSize(0, 0))
        self.label_pl_name.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(4, QFormLayout.LabelRole, self.label_pl_name)

        self.lineEdit_pl_name = QLineEdit(self.groupBox_General)
        self.lineEdit_pl_name.setObjectName(u"lineEdit_pl_name")
        sizePolicy4.setHeightForWidth(self.lineEdit_pl_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_pl_name.setSizePolicy(sizePolicy4)
        self.lineEdit_pl_name.setMinimumSize(QSize(0, 0))
        self.lineEdit_pl_name.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(4, QFormLayout.FieldRole, self.lineEdit_pl_name)

        self.label_pp_num = QLabel(self.groupBox_General)
        self.label_pp_num.setObjectName(u"label_pp_num")
        sizePolicy4.setHeightForWidth(self.label_pp_num.sizePolicy().hasHeightForWidth())
        self.label_pp_num.setSizePolicy(sizePolicy4)
        self.label_pp_num.setMinimumSize(QSize(0, 0))
        self.label_pp_num.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(5, QFormLayout.LabelRole, self.label_pp_num)

        self.spinBox_pp_num = QSpinBox(self.groupBox_General)
        self.spinBox_pp_num.setObjectName(u"spinBox_pp_num")
        sizePolicy4.setHeightForWidth(self.spinBox_pp_num.sizePolicy().hasHeightForWidth())
        self.spinBox_pp_num.setSizePolicy(sizePolicy4)
        self.spinBox_pp_num.setMinimumSize(QSize(0, 0))
        self.spinBox_pp_num.setMaximumSize(QSize(16777215, 16777215))
        self.spinBox_pp_num.setMaximum(999)

        self.layout_G1.setWidget(5, QFormLayout.FieldRole, self.spinBox_pp_num)

        self.label_location_lon = QLabel(self.groupBox_General)
        self.label_location_lon.setObjectName(u"label_location_lon")
        sizePolicy4.setHeightForWidth(self.label_location_lon.sizePolicy().hasHeightForWidth())
        self.label_location_lon.setSizePolicy(sizePolicy4)
        self.label_location_lon.setMinimumSize(QSize(0, 0))
        self.label_location_lon.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(6, QFormLayout.LabelRole, self.label_location_lon)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lineEdit_location_lon = QLineEdit(self.groupBox_General)
        self.lineEdit_location_lon.setObjectName(u"lineEdit_location_lon")
        sizePolicy4.setHeightForWidth(self.lineEdit_location_lon.sizePolicy().hasHeightForWidth())
        self.lineEdit_location_lon.setSizePolicy(sizePolicy4)
        self.lineEdit_location_lon.setMinimumSize(QSize(0, 0))
        self.lineEdit_location_lon.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_13.addWidget(self.lineEdit_location_lon)

        self.lineEdit_location_lat = QLineEdit(self.groupBox_General)
        self.lineEdit_location_lat.setObjectName(u"lineEdit_location_lat")
        sizePolicy4.setHeightForWidth(self.lineEdit_location_lat.sizePolicy().hasHeightForWidth())
        self.lineEdit_location_lat.setSizePolicy(sizePolicy4)
        self.lineEdit_location_lat.setMinimumSize(QSize(0, 0))
        self.lineEdit_location_lat.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_13.addWidget(self.lineEdit_location_lat)


        self.layout_G1.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_13)

        self.label_pl_level = QLabel(self.groupBox_General)
        self.label_pl_level.setObjectName(u"label_pl_level")
        sizePolicy4.setHeightForWidth(self.label_pl_level.sizePolicy().hasHeightForWidth())
        self.label_pl_level.setSizePolicy(sizePolicy4)
        self.label_pl_level.setMinimumSize(QSize(0, 0))
        self.label_pl_level.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(7, QFormLayout.LabelRole, self.label_pl_level)

        self.comboBox_pl_level = QComboBox(self.groupBox_General)
        self.comboBox_pl_level.setObjectName(u"comboBox_pl_level")
        sizePolicy4.setHeightForWidth(self.comboBox_pl_level.sizePolicy().hasHeightForWidth())
        self.comboBox_pl_level.setSizePolicy(sizePolicy4)
        self.comboBox_pl_level.setMinimumSize(QSize(0, 0))
        self.comboBox_pl_level.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(7, QFormLayout.FieldRole, self.comboBox_pl_level)

        self.label_pl_cir_type = QLabel(self.groupBox_General)
        self.label_pl_cir_type.setObjectName(u"label_pl_cir_type")
        sizePolicy4.setHeightForWidth(self.label_pl_cir_type.sizePolicy().hasHeightForWidth())
        self.label_pl_cir_type.setSizePolicy(sizePolicy4)
        self.label_pl_cir_type.setMinimumSize(QSize(0, 0))
        self.label_pl_cir_type.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(8, QFormLayout.LabelRole, self.label_pl_cir_type)

        self.comboBox_pl_cir_type = QComboBox(self.groupBox_General)
        self.comboBox_pl_cir_type.setObjectName(u"comboBox_pl_cir_type")
        sizePolicy4.setHeightForWidth(self.comboBox_pl_cir_type.sizePolicy().hasHeightForWidth())
        self.comboBox_pl_cir_type.setSizePolicy(sizePolicy4)
        self.comboBox_pl_cir_type.setMinimumSize(QSize(0, 0))
        self.comboBox_pl_cir_type.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(8, QFormLayout.FieldRole, self.comboBox_pl_cir_type)

        self.label_pp_type = QLabel(self.groupBox_General)
        self.label_pp_type.setObjectName(u"label_pp_type")
        sizePolicy4.setHeightForWidth(self.label_pp_type.sizePolicy().hasHeightForWidth())
        self.label_pp_type.setSizePolicy(sizePolicy4)
        self.label_pp_type.setMinimumSize(QSize(0, 0))
        self.label_pp_type.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(9, QFormLayout.LabelRole, self.label_pp_type)

        self.comboBox_pp_type = QComboBox(self.groupBox_General)
        self.comboBox_pp_type.setObjectName(u"comboBox_pp_type")
        sizePolicy4.setHeightForWidth(self.comboBox_pp_type.sizePolicy().hasHeightForWidth())
        self.comboBox_pp_type.setSizePolicy(sizePolicy4)
        self.comboBox_pp_type.setMinimumSize(QSize(0, 0))
        self.comboBox_pp_type.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(9, QFormLayout.FieldRole, self.comboBox_pp_type)

        self.label_pp_model = QLabel(self.groupBox_General)
        self.label_pp_model.setObjectName(u"label_pp_model")
        sizePolicy4.setHeightForWidth(self.label_pp_model.sizePolicy().hasHeightForWidth())
        self.label_pp_model.setSizePolicy(sizePolicy4)
        self.label_pp_model.setMinimumSize(QSize(0, 0))
        self.label_pp_model.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(10, QFormLayout.LabelRole, self.label_pp_model)

        self.comboBox_pp_model = QComboBox(self.groupBox_General)
        self.comboBox_pp_model.setObjectName(u"comboBox_pp_model")
        sizePolicy4.setHeightForWidth(self.comboBox_pp_model.sizePolicy().hasHeightForWidth())
        self.comboBox_pp_model.setSizePolicy(sizePolicy4)
        self.comboBox_pp_model.setMinimumSize(QSize(0, 0))
        self.comboBox_pp_model.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(10, QFormLayout.FieldRole, self.comboBox_pp_model)

        self.label_num_inst_str = QLabel(self.groupBox_General)
        self.label_num_inst_str.setObjectName(u"label_num_inst_str")
        sizePolicy4.setHeightForWidth(self.label_num_inst_str.sizePolicy().hasHeightForWidth())
        self.label_num_inst_str.setSizePolicy(sizePolicy4)
        self.label_num_inst_str.setMinimumSize(QSize(0, 0))
        self.label_num_inst_str.setMaximumSize(QSize(16777215, 16777215))

        self.layout_G1.setWidget(11, QFormLayout.LabelRole, self.label_num_inst_str)

        self.spinBox_num_inst_str = QSpinBox(self.groupBox_General)
        self.spinBox_num_inst_str.setObjectName(u"spinBox_num_inst_str")
        sizePolicy4.setHeightForWidth(self.spinBox_num_inst_str.sizePolicy().hasHeightForWidth())
        self.spinBox_num_inst_str.setSizePolicy(sizePolicy4)
        self.spinBox_num_inst_str.setMinimumSize(QSize(0, 0))
        self.spinBox_num_inst_str.setMaximumSize(QSize(16777215, 16777215))
        self.spinBox_num_inst_str.setMaximum(30)

        self.layout_G1.setWidget(11, QFormLayout.FieldRole, self.spinBox_num_inst_str)


        self.verticalLayout_31.addLayout(self.layout_G1)

        self.layout_G2 = QHBoxLayout()
        self.layout_G2.setObjectName(u"layout_G2")
        self.pushButton_saveG = QPushButton(self.groupBox_General)
        self.pushButton_saveG.setObjectName(u"pushButton_saveG")
        sizePolicy4.setHeightForWidth(self.pushButton_saveG.sizePolicy().hasHeightForWidth())
        self.pushButton_saveG.setSizePolicy(sizePolicy4)
        self.pushButton_saveG.setMinimumSize(QSize(0, 23))
        self.pushButton_saveG.setMaximumSize(QSize(16777215, 23))

        self.layout_G2.addWidget(self.pushButton_saveG)


        self.verticalLayout_31.addLayout(self.layout_G2)


        self.verticalLayout1.addWidget(self.groupBox_General)

        self.groupBox_Damage = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_Damage.setObjectName(u"groupBox_Damage")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.groupBox_Damage.sizePolicy().hasHeightForWidth())
        self.groupBox_Damage.setSizePolicy(sizePolicy9)
        self.groupBox_Damage.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_Damage)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 24, -1, -1)
        self.layout_D1 = QFormLayout()
        self.layout_D1.setObjectName(u"layout_D1")
        self.layout_D1.setHorizontalSpacing(9)
        self.layout_D1.setVerticalSpacing(3)
        self.label_report_number = QLabel(self.groupBox_Damage)
        self.label_report_number.setObjectName(u"label_report_number")

        self.layout_D1.setWidget(0, QFormLayout.LabelRole, self.label_report_number)

        self.spinBox_report_number = QSpinBox(self.groupBox_Damage)
        self.spinBox_report_number.setObjectName(u"spinBox_report_number")

        self.layout_D1.setWidget(0, QFormLayout.FieldRole, self.spinBox_report_number)

        self.label_process_date = QLabel(self.groupBox_Damage)
        self.label_process_date.setObjectName(u"label_process_date")
        sizePolicy4.setHeightForWidth(self.label_process_date.sizePolicy().hasHeightForWidth())
        self.label_process_date.setSizePolicy(sizePolicy4)

        self.layout_D1.setWidget(1, QFormLayout.LabelRole, self.label_process_date)

        self.dateEdit_process_date = QDateEdit(self.groupBox_Damage)
        self.dateEdit_process_date.setObjectName(u"dateEdit_process_date")
        sizePolicy4.setHeightForWidth(self.dateEdit_process_date.sizePolicy().hasHeightForWidth())
        self.dateEdit_process_date.setSizePolicy(sizePolicy4)

        self.layout_D1.setWidget(1, QFormLayout.FieldRole, self.dateEdit_process_date)

        self.label_staff = QLabel(self.groupBox_Damage)
        self.label_staff.setObjectName(u"label_staff")

        self.layout_D1.setWidget(2, QFormLayout.LabelRole, self.label_staff)

        self.lineEdit_staff = QLineEdit(self.groupBox_Damage)
        self.lineEdit_staff.setObjectName(u"lineEdit_staff")

        self.layout_D1.setWidget(2, QFormLayout.FieldRole, self.lineEdit_staff)


        self.verticalLayout_6.addLayout(self.layout_D1)

        self.label_damage = QLabel(self.groupBox_Damage)
        self.label_damage.setObjectName(u"label_damage")

        self.verticalLayout_6.addWidget(self.label_damage)

        self.treeWidget = QTreeWidget(self.groupBox_Damage)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignLeading|Qt.AlignVCenter);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy6.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy6)

        self.verticalLayout_6.addWidget(self.treeWidget)

        self.layout_D2 = QHBoxLayout()
        self.layout_D2.setObjectName(u"layout_D2")
        self.label_pushbutton1 = QLabel(self.groupBox_Damage)
        self.label_pushbutton1.setObjectName(u"label_pushbutton1")

        self.layout_D2.addWidget(self.label_pushbutton1)

        self.pushButton_add_1 = QPushButton(self.groupBox_Damage)
        self.pushButton_add_1.setObjectName(u"pushButton_add_1")
        self.pushButton_add_1.setMinimumSize(QSize(23, 23))
        self.pushButton_add_1.setMaximumSize(QSize(23, 23))

        self.layout_D2.addWidget(self.pushButton_add_1)

        self.pushButton_sub_1 = QPushButton(self.groupBox_Damage)
        self.pushButton_sub_1.setObjectName(u"pushButton_sub_1")
        self.pushButton_sub_1.setMinimumSize(QSize(23, 23))
        self.pushButton_sub_1.setMaximumSize(QSize(23, 23))

        self.layout_D2.addWidget(self.pushButton_sub_1)

        self.line = QFrame(self.groupBox_Damage)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.layout_D2.addWidget(self.line)

        self.label_pushbutton2 = QLabel(self.groupBox_Damage)
        self.label_pushbutton2.setObjectName(u"label_pushbutton2")

        self.layout_D2.addWidget(self.label_pushbutton2)

        self.pushButton_add_2 = QPushButton(self.groupBox_Damage)
        self.pushButton_add_2.setObjectName(u"pushButton_add_2")
        self.pushButton_add_2.setMinimumSize(QSize(23, 23))
        self.pushButton_add_2.setMaximumSize(QSize(23, 23))

        self.layout_D2.addWidget(self.pushButton_add_2)

        self.pushButton_sub_2 = QPushButton(self.groupBox_Damage)
        self.pushButton_sub_2.setObjectName(u"pushButton_sub_2")
        self.pushButton_sub_2.setMinimumSize(QSize(23, 23))
        self.pushButton_sub_2.setMaximumSize(QSize(23, 23))

        self.layout_D2.addWidget(self.pushButton_sub_2)


        self.verticalLayout_6.addLayout(self.layout_D2)

        self.layout_D3 = QHBoxLayout()
        self.layout_D3.setObjectName(u"layout_D3")
        self.pushButton_openDirD = QPushButton(self.groupBox_Damage)
        self.pushButton_openDirD.setObjectName(u"pushButton_openDirD")
        sizePolicy4.setHeightForWidth(self.pushButton_openDirD.sizePolicy().hasHeightForWidth())
        self.pushButton_openDirD.setSizePolicy(sizePolicy4)
        self.pushButton_openDirD.setMinimumSize(QSize(40, 23))
        self.pushButton_openDirD.setMaximumSize(QSize(16777215, 23))

        self.layout_D3.addWidget(self.pushButton_openDirD)

        self.pushButton_saveD = QPushButton(self.groupBox_Damage)
        self.pushButton_saveD.setObjectName(u"pushButton_saveD")
        sizePolicy4.setHeightForWidth(self.pushButton_saveD.sizePolicy().hasHeightForWidth())
        self.pushButton_saveD.setSizePolicy(sizePolicy4)
        self.pushButton_saveD.setMinimumSize(QSize(40, 23))
        self.pushButton_saveD.setMaximumSize(QSize(16777215, 23))

        self.layout_D3.addWidget(self.pushButton_saveD)


        self.verticalLayout_6.addLayout(self.layout_D3)


        self.verticalLayout1.addWidget(self.groupBox_Damage)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea)


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
        self.groupBox_General.setTitle(QCoreApplication.translate("videoPlayer", u"[ General Information ]", None))
        self.label_file_name.setText(QCoreApplication.translate("videoPlayer", u"File name:", None))
        self.label_file_name_value.setText(QCoreApplication.translate("videoPlayer", u"noname", None))
        self.label_record_date.setText(QCoreApplication.translate("videoPlayer", u"Recorded date:", None))
        self.label_com_name.setText(QCoreApplication.translate("videoPlayer", u"Company name:", None))
        self.label_bra_name.setText(QCoreApplication.translate("videoPlayer", u"Branch name:", None))
        self.label_pl_name.setText(QCoreApplication.translate("videoPlayer", u"Power line name:", None))
        self.label_pp_num.setText(QCoreApplication.translate("videoPlayer", u"Power pole number:", None))
        self.label_location_lon.setText(QCoreApplication.translate("videoPlayer", u"Location [lon/lat]:", None))
        self.label_pl_level.setText(QCoreApplication.translate("videoPlayer", u"Voltage level [kV]:", None))
        self.label_pl_cir_type.setText(QCoreApplication.translate("videoPlayer", u"Power line circuit type:", None))
        self.label_pp_type.setText(QCoreApplication.translate("videoPlayer", u"Power pole type:", None))
        self.label_pp_model.setText(QCoreApplication.translate("videoPlayer", u"Power pole model:", None))
        self.label_num_inst_str.setText(QCoreApplication.translate("videoPlayer", u"Insulator count:", None))
        self.pushButton_saveG.setText(QCoreApplication.translate("videoPlayer", u"Save", None))
        self.groupBox_Damage.setTitle(QCoreApplication.translate("videoPlayer", u" [ Damage Assessment ]", None))
        self.label_report_number.setText(QCoreApplication.translate("videoPlayer", u"Report number:", None))
        self.label_process_date.setText(QCoreApplication.translate("videoPlayer", u"Assessment date:", None))
        self.label_staff.setText(QCoreApplication.translate("videoPlayer", u"TextLabel", None))
        self.label_damage.setText(QCoreApplication.translate("videoPlayer", u"Damages:", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("videoPlayer", u"Damage", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("videoPlayer", u"n", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("videoPlayer", u"Phase", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("videoPlayer", u"Insulator", None));
        self.label_pushbutton1.setText(QCoreApplication.translate("videoPlayer", u"Insulator:", None))
        self.pushButton_add_1.setText(QCoreApplication.translate("videoPlayer", u"+", None))
        self.pushButton_sub_1.setText(QCoreApplication.translate("videoPlayer", u"-", None))
        self.label_pushbutton2.setText(QCoreApplication.translate("videoPlayer", u"Element:", None))
        self.pushButton_add_2.setText(QCoreApplication.translate("videoPlayer", u"+", None))
        self.pushButton_sub_2.setText(QCoreApplication.translate("videoPlayer", u"-", None))
        self.pushButton_openDirD.setText(QCoreApplication.translate("videoPlayer", u"Open Dir", None))
#if QT_CONFIG(shortcut)
        self.pushButton_openDirD.setShortcut(QCoreApplication.translate("videoPlayer", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_saveD.setText(QCoreApplication.translate("videoPlayer", u"Save", None))
#if QT_CONFIG(shortcut)
        self.pushButton_saveD.setShortcut(QCoreApplication.translate("videoPlayer", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

