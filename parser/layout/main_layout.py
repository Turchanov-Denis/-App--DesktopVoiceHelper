# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firo_parser_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 682)
        MainWindow.setStyleSheet("background: #282828;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.serfing_button = QtWidgets.QPushButton(self.centralwidget)
        self.serfing_button.setGeometry(QtCore.QRect(0, 632, 452, 53))
        self.serfing_button.setMinimumSize(QtCore.QSize(452, 53))
        self.serfing_button.setMaximumSize(QtCore.QSize(452, 53))
        self.serfing_button.setStyleSheet("\n"
"font: 8pt \"NSimSun\";\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 24px;\n"
"line-height: 32px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"background: #101010;")
        self.serfing_button.setObjectName("serfing_button")
        self.sub_top_frame = QtWidgets.QFrame(self.centralwidget)
        self.sub_top_frame.setGeometry(QtCore.QRect(0, 25, 452, 86))
        self.sub_top_frame.setMinimumSize(QtCore.QSize(452, 86))
        self.sub_top_frame.setMaximumSize(QtCore.QSize(452, 86))
        self.sub_top_frame.setStyleSheet("background: #0C0C0C;")
        self.sub_top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sub_top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sub_top_frame.setObjectName("sub_top_frame")
        self.find_line = QtWidgets.QLineEdit(self.sub_top_frame)
        self.find_line.setGeometry(QtCore.QRect(10, 45, 420, 29))
        self.find_line.setStyleSheet("background: #2B2B2B;\n"
"border-radius: 4px;\n"
"font-family: \'Roboto Mono\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 18px;\n"
"\n"
"color: rgba(255, 255, 255, 0.8);\n"
"")
        self.find_line.setInputMask("")
        self.find_line.setText("")
        self.find_line.setPlaceholderText(" type to search")
        self.find_line.setObjectName("find_line")
        self.sorted_by_mark = QtWidgets.QComboBox(self.sub_top_frame)
        self.sorted_by_mark.setGeometry(QtCore.QRect(10, 10, 206, 29))
        self.sorted_by_mark.setStyleSheet("background: #2B2B2B;\n"
"border-radius: 2px;\n"
"font-family: \'Roboto Mono\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 18px;\n"
"\n"
"color: rgba(255, 255, 255, 0.8);\n"
"")
        self.sorted_by_mark.setDuplicatesEnabled(False)
        self.sorted_by_mark.setFrame(True)
        self.sorted_by_mark.setObjectName("sorted_by_mark")
        self.sorted_by_time = QtWidgets.QComboBox(self.sub_top_frame)
        self.sorted_by_time.setGeometry(QtCore.QRect(223, 10, 206, 29))
        self.sorted_by_time.setStyleSheet("background: #2B2B2B;\n"
"border-radius: 2px;\n"
"font-family: \'Roboto Mono\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 18px;\n"
"\n"
"color: rgba(255, 255, 255, 0.8);\n"
"")
        self.sorted_by_time.setDuplicatesEnabled(False)
        self.sorted_by_time.setFrame(True)
        self.sorted_by_time.setObjectName("sorted_by_time")
        self.button_clear_find = QtWidgets.QPushButton(self.sub_top_frame)
        self.button_clear_find.setGeometry(QtCore.QRect(393, 43, 31, 31))
        self.button_clear_find.setStyleSheet("color: rgba(255, 255, 255, 0.8);\n"
"background: rgba(199, 199, 199, 0.0);\n"
"font-size: 18px;\n"
"border-top:0px solid rgb(46, 46, 46);")
        self.button_clear_find.setObjectName("button_clear_find")
        self.topbar = QtWidgets.QFrame(self.centralwidget)
        self.topbar.setGeometry(QtCore.QRect(0, 0, 452, 25))
        self.topbar.setMinimumSize(QtCore.QSize(452, 25))
        self.topbar.setMaximumSize(QtCore.QSize(452, 25))
        self.topbar.setStyleSheet("background: #212226;")
        self.topbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topbar.setObjectName("topbar")
        self.button_X = QtWidgets.QPushButton(self.topbar)
        self.button_X.setGeometry(QtCore.QRect(419, 2, 31, 23))
        self.button_X.setStyleSheet("color: #FFFFFF;\n"
"background: rgba(199, 199, 199, 0.0);")
        self.button_X.setObjectName("button_X")
        self.button_swap_2 = QtWidgets.QPushButton(self.topbar)
        self.button_swap_2.setGeometry(QtCore.QRect(400, 2, 21, 23))
        self.button_swap_2.setStyleSheet("color: #FFFFFF;\n"
"background: rgba(199, 199, 199, 0.0);")
        self.button_swap_2.setObjectName("button_swap_2")
        self.button_setting = QtWidgets.QPushButton(self.topbar)
        self.button_setting.setGeometry(QtCore.QRect(360, 2, 21, 23))
        self.button_setting.setStyleSheet("color: #FFFFFF;\n"
"background: rgba(199, 199, 199, 0.0);")
        self.button_setting.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../DeKi-Project/library/lib_material/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_setting.setIcon(icon)
        self.button_setting.setObjectName("button_setting")
        self.tutorial_button = QtWidgets.QPushButton(self.topbar)
        self.tutorial_button.setGeometry(QtCore.QRect(380, 2, 21, 23))
        self.tutorial_button.setStyleSheet("color: #FFFFFF;\n"
"background: rgba(199, 199, 199, 0.0);")
        self.tutorial_button.setObjectName("tutorial_button")
        self.name_app = QtWidgets.QTextBrowser(self.topbar)
        self.name_app.setGeometry(QtCore.QRect(0, 0, 221, 21))
        self.name_app.setStyleSheet("font-family: \'Roboto Mono\';\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 13px;\n"
"line-height: 17px;\n"
"text-decoration-line: underline;\n"
"background: rgba(44, 40, 40, 0.0);\n"
"color: rgba(255, 255, 255, 0.8);\n"
"border: 0.5px solid rgba(167, 167, 167, 0.0);")
        self.name_app.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.name_app.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.name_app.setObjectName("name_app")
        self.frame_container_area = QtWidgets.QFrame(self.centralwidget)
        self.frame_container_area.setGeometry(QtCore.QRect(0, 110, 451, 519))
        self.frame_container_area.setMinimumSize(QtCore.QSize(451, 321))
        self.frame_container_area.setMaximumSize(QtCore.QSize(451, 521))
        self.frame_container_area.setStyleSheet("background: rgba(44, 40, 40, 0.0);")
        self.frame_container_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_container_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_container_area.setObjectName("frame_container_area")
        self.area_for_item = QtWidgets.QScrollArea(self.frame_container_area)
        self.area_for_item.setGeometry(QtCore.QRect(10, 20, 416, 501))
        self.area_for_item.setMinimumSize(QtCore.QSize(416, 300))
        self.area_for_item.setMaximumSize(QtCore.QSize(416, 501))
        self.area_for_item.setStyleSheet("background: rgba(44, 40, 40, 0.0);\n"
"border: 0.5px solid rgba(167, 167, 167, 0.0);")
        self.area_for_item.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_for_item.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_for_item.setWidgetResizable(True)
        self.area_for_item.setObjectName("area_for_item")
        self.area_for_item_container = QtWidgets.QWidget()
        self.area_for_item_container.setGeometry(QtCore.QRect(0, 0, 414, 499))
        self.area_for_item_container.setObjectName("area_for_item_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.area_for_item_container)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.area_for_item.setWidget(self.area_for_item_container)
        self.scroll_label = QtWidgets.QLabel(self.frame_container_area)
        self.scroll_label.setGeometry(QtCore.QRect(435, 20, 4, 450))
        self.scroll_label.setStyleSheet("background: #0C0C0C;")
        self.scroll_label.setObjectName("scroll_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.serfing_button.setText(_translate("MainWindow", "-- serfing --"))
        self.button_clear_find.setText(_translate("MainWindow", "X"))
        self.button_X.setText(_translate("MainWindow", "X"))
        self.button_swap_2.setText(_translate("MainWindow", "—"))
        self.tutorial_button.setText(_translate("MainWindow", "?"))
        self.name_app.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Mono\'; font-size:13px; font-weight:296; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Firo\'s parser</span></p></body></html>"))
        self.scroll_label.setText(_translate("MainWindow", "TextLabel"))

