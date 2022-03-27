import subprocess
import sys
import webbrowser
import sqlite_Neko
from layout_file.main_frame import Ui_MainFrame
from layout_file.add_frame import Ui_AddFrame
from layout_file.setting_frame import Ui_SettingFrame
from layout_file.main_min_frame import Ui_MainMinFrame
from PyQt5.QtGui import QKeySequence, QWheelEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow, Ui_MainFrame, Ui_AddFrame, Ui_SettingFrame):
    def __init__(self):
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            self.names_character_list = sqlite_Neko.get_names_character(
                conn)  # получить имена всех доступных персонажей
            self.view_character, self.name_character, self.name_user, self.language, self.behavior, self.main_window_size = sqlite_Neko.get_global_name(
                conn)
            self.current_paths_character = sqlite_Neko.get_paths_character(conn, self.view_character)
        self.directory_list = []
        self.del_list = []
        super().__init__()
        MainWindow.setObjectName(self, "MainWindow")
        MainWindow.resize(self, 1366, 767)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        """hotkey"""
        self.shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        self.shortcut.activated.connect(self.hide_main_window)

        self.stackedWidget_sourse = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_sourse.setGeometry(QtCore.QRect(9, -1, 1311, 761))
        self.stackedWidget_sourse.setStyleSheet("")
        self.stackedWidget_sourse.setObjectName("stackedWidget_sourse")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.stackedWidget_sourse.addWidget(Ui_MainFrame.setup_Main_frame(self))
        self.stackedWidget_sourse.addWidget(Ui_AddFrame.setup_add_frame(self))
        self.stackedWidget_sourse.addWidget(Ui_SettingFrame.setup_settinf_frame(self))
        self.stackedWidget_sourse.addWidget(Ui_MainMinFrame.setup_main_min_frame(self))
        self.stackedWidget_sourse.setCurrentIndex(2)
        """button connect"""
        self.rule_button.clicked.connect(lambda: self.stackedWidget_sourse.setCurrentIndex(1))
        self.setting_button.clicked.connect(lambda: self.stackedWidget_sourse.setCurrentIndex(2))
        self.back_from_add_button.clicked.connect(lambda: self.stackedWidget_sourse.setCurrentIndex(0))
        self.back_fome_setting_button.clicked.connect(lambda: self.stackedWidget_sourse.setCurrentIndex(0))
        self.next_on_page_2_button.clicked.connect(lambda: self.stackedWidget_setting_page.setCurrentIndex(0))
        self.button_on_1_page.clicked.connect(lambda: self.stackedWidget_setting_page.setCurrentIndex(1))
        self.bread_button_2.clicked.connect(self.get_directory)
        self.save_command_button.clicked.connect(self.add_date_in_Neko_bd)
        self.delite_button.clicked.connect(self.del_command)
        self.show_update_item_in_area_delite_choice()
        """ setting """
        if self.main_window_size == "min":
            self.stackedWidget_sourse.setCurrentIndex(3)
        else:
            self.stackedWidget_sourse.setCurrentIndex(0)
        self.button_character_r.clicked.connect(self.Next_character)
        MainWindow.setCentralWidget(self, self.centralwidget)
        self.retranslateUi(MainWindow)
        self.button_window_r_2.clicked.connect(self.Next_main_window_size)
    """ setting """
    def Next_main_window_size(self):
        self.next_main_frame = False
        self.next_main_frame = not self.next_main_frame
        if self.next_main_frame:
            self.main_window_size = "min"
        else:
            self.main_window_size = "normal"
        self.label_normal_window_page_2.setText(self.main_window_size)
    def hide_main_window(self):
        self.showMinimized()
    def Next_character(self):
        """allows you to change the character in the settings
          param language_index: needed to determine the current character
          """
        character_index = self.names_character_list.index(self.view_character)
        print(character_index)
        character_index += 1
        if character_index > len(self.names_character_list) - 1:
            character_index = 0
        self.view_character = self.names_character_list[character_index]
        print(self.view_character)
        self.update_paths()
    def save_global_setting(self):
        """ stores global settings in database  """
        conn = sqlite_Neko.create_connection("Neko.db")
        get_user_name = self.Nickname_2.text()
        if get_user_name not in ["нике", "nickname"]:
            self.name_user = get_user_name
        get_character_name = self.Nickname_1.text()
        if get_character_name not in ["нике", "nickname"]:
            self.name_character = get_character_name
        print(get_user_name, self.name_user)
        with conn:
            sqlite_Neko.update_global_name(conn, (
                self.view_character, self.name_character, self.name_user, self.language, self.behavior,
               self.main_window_size))
        self.set_name_in_widget()
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(self, "MainWindow")
        self.dialog_character.setText("Семпай, надеюсь, ты меня не просто так позвал?")
        self.setting_button.setText("setting")
        self.rule_button.setText("ruling command")
        self.q_a_button.setText("q&&a")
        self.lineedit_command.setText("enter name command...")
        self.label_add_1.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:13px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Фиро: позволь помочь тебе с составлением команд</span></p></body></html>")
        self.label_add_4.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:13px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Фиро: так можно указать сайт!</span></p></body></html>")
        self.save_command_button.setText("save")
        self.label_add_click_1.setText("*клик*")
        self.label_29.setText("TextLabel")
        self.label_add_7.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:13px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">...</span></p></body></html>")
        self.lineedit_site.setText("set site")
        self.label_add_6.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:13px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">команде название.</span></p></body></html>")
        self.label_add_2.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:13px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Фиро: так можно выбрать файлы </span></p></body></html>")
        self.label_add_5.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:13px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Фиро: выбери что-то одно, затем укажи </span></p></body></html>")
        self.label_add_click_3.setText("*клик*")
        self.back_from_add_button.setText("back")
        self.label_add_click_2.setText("*клик*")
        self.label_add_click_4.setText("*клик*")
        self.label_add_8.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px;\">Фиро выполнит ваше поручение!</span></p></body></html>")
        self.label_add_3.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:13px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">или приложения!</span></p></body></html>")
        self.delite_button.setText("delite")
        self.label_about_delite.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px;\">кликни на те,которые хочешь удалить</span></p></body></html>")
        self.label_info_2.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Если хочешь быстрый доступ к сайту то вставь ссылку</span></p></body></html>")
        self.label_add_13.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Если хочешь добавить приложение в быстрый запуск то *кликни* на хлеб</span></p></body></html>")
        self.label_info_3.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Titillium Web\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Полагаю, у тебя есть приложения, которыми ты почти не пользуешься, но *вдруг понадобятся*, предлагаю хранить их под рукой</span></p></body></html>")
        self.label_setting_page_2.setText("setting")
        self.label_window_page_2.setText("main window")
        self.label_normal_window_page_2.setText("Normal size")
        self.label_page_2.setText("page 2")
        self.label_setting.setText("setting")
        self.label_setting_1.setText("Вайфу это твой выбор")
        self.label_setting_4.setText("язык")
        self.label_setting_5.setText("характер")
        self.label_setting_2.setText("Укажите  свой  ник")
        self.Nickname_2.setText("нике")
        self.label_setting_6.setText("русский")
        self.label_setting_7.setText("вайфу")
        self.button_save.setText("save")
        self.back_fome_setting_button.setText("back")
        self.label_setting_8.setText("Укажите  ник  персонажа")
        self.Nickname_1.setText("нике")
        self.label_10.setText("page 1")
        self.wrap_button.setText("wrap")
        self.label_dialog_min_frame.setText("Рада вас\n"
                                            " видеть\n"
                                            " хозяин")
    def update_paths(self):
        """associated with Next_character, according to the selected character, changes the paths to the pictures of the corresponding
         character, all frames use 4 different images of one character, stored in database """
        print("awd")
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            self.current_paths_character = sqlite_Neko.get_paths_character(conn, self.view_character)
            self.character_label.setPixmap(QtGui.QPixmap(self.current_paths_character[1]))
            self.character_add_label.setPixmap(QtGui.QPixmap(self.current_paths_character[2]))
            self.character_set.setPixmap(QtGui.QPixmap(self.current_paths_character[3]))
            self.character_s_min.setPixmap(QtGui.QPixmap(self.current_paths_character[4]))
    def set_name_in_widget(self):
        """ follows after save_global_setting(), applies resulting changes to unique variables
        self.view_character, self.name_character, self.name_user, self.language, self.behavior, self.work_table"""
        self.dialog_character.setText(f"          {self.name_user},надеюсь, ты меня не просто так позвал?")
        self.character_label.setPixmap(QtGui.QPixmap(self.current_paths_character[1]))
        self.character_add_label.setPixmap(QtGui.QPixmap(self.current_paths_character[2]))
        self.character_set.setPixmap(QtGui.QPixmap(self.current_paths_character[3]))
        self.character_s_min.setPixmap(QtGui.QPixmap(self.current_paths_character[4]))

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
