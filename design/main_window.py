# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import design.resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 330)
        MainWindow.setMinimumSize(QtCore.QSize(510, 330))
        MainWindow.setMaximumSize(QtCore.QSize(510, 330))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 511, 341))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.next_button = QtWidgets.QPushButton(self.page_2)
        self.next_button.setGeometry(QtCore.QRect(350, 300, 75, 23))
        self.next_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_button.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #FFD0D1;\n"
                                       "}")
        self.next_button.setObjectName("next_button")
        self.cancel_button = QtWidgets.QPushButton(self.page_2)
        self.cancel_button.setGeometry(QtCore.QRect(430, 300, 75, 23))
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_button.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFD0D1;\n"
                                         "}")
        self.cancel_button.setObjectName("cancel_button")
        self.line = QtWidgets.QFrame(self.page_2)
        self.line.setGeometry(QtCore.QRect(190, 290, 331, 1))
        self.line.setStyleSheet("border-top: 1px solid black;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hello_msg = QtWidgets.QTextBrowser(self.page_2)
        self.hello_msg.setGeometry(QtCore.QRect(210, 10, 281, 71))
        self.hello_msg.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.hello_msg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hello_msg.setObjectName("hello_msg")
        self.hello2_msg = QtWidgets.QTextBrowser(self.page_2)
        self.hello2_msg.setGeometry(QtCore.QRect(210, 120, 281, 41))
        self.hello2_msg.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.hello2_msg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hello2_msg.setObjectName("hello2_msg")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(210, 170, 281, 41))
        self.textBrowser_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.listWidget_4 = QtWidgets.QListWidget(self.page_2)
        self.listWidget_4.setGeometry(QtCore.QRect(0, 0, 191, 291))
        self.listWidget_4.setStyleSheet("background-image: url(:/images/stallaris_ba (1).jpg);")
        self.listWidget_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_4.setObjectName("listWidget_4")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.line_3 = QtWidgets.QFrame(self.page_3)
        self.line_3.setGeometry(QtCore.QRect(190, 290, 331, 1))
        self.line_3.setStyleSheet("border-top: 1px solid black;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.next_button_3 = QtWidgets.QPushButton(self.page_3)
        self.next_button_3.setEnabled(False)
        self.next_button_3.setGeometry(QtCore.QRect(350, 300, 75, 23))
        self.next_button_3.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.next_button_3.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFD0D1;\n"
                                         "}")
        self.next_button_3.setObjectName("next_button_3")
        self.cancel_button_3 = QtWidgets.QPushButton(self.page_3)
        self.cancel_button_3.setGeometry(QtCore.QRect(430, 300, 75, 23))
        self.cancel_button_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_button_3.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: #FFD0D1;\n"
                                           "}")
        self.cancel_button_3.setObjectName("cancel_button_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.page_3)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 0, 191, 291))
        self.listWidget_3.setStyleSheet("background-image: url(:/images/stallaris_ba (1).jpg);")
        self.listWidget_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_3.setObjectName("listWidget_3")
        self.back_button_2 = QtWidgets.QPushButton(self.page_3)
        self.back_button_2.setGeometry(QtCore.QRect(270, 300, 75, 23))
        self.back_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_2.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFD0D1;\n"
                                         "}")
        self.back_button_2.setObjectName("back_button_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser.setGeometry(QtCore.QRect(210, 10, 281, 31))
        self.textBrowser.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser_2.setGeometry(QtCore.QRect(210, 40, 281, 41))
        self.textBrowser_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.line_4 = QtWidgets.QFrame(self.page_3)
        self.line_4.setGeometry(QtCore.QRect(190, 80, 331, 1))
        self.line_4.setStyleSheet("border-top: 1px solid black;")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(210, 90, 281, 121))
        self.textBrowser_4.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.eula_true = QtWidgets.QRadioButton(self.page_3)
        self.eula_true.setGeometry(QtCore.QRect(210, 240, 231, 21))
        self.eula_true.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eula_true.setObjectName("eula_true")
        self.eula = QtWidgets.QButtonGroup(MainWindow)
        self.eula.setObjectName("eula")
        self.eula.addButton(self.eula_true)
        self.eula_false = QtWidgets.QRadioButton(self.page_3)
        self.eula_false.setGeometry(QtCore.QRect(210, 260, 231, 21))
        self.eula_false.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eula_false.setAcceptDrops(False)
        self.eula_false.setChecked(True)
        self.eula_false.setObjectName("eula_false")
        self.eula.addButton(self.eula_false)
        self.eula_true1 = QtWidgets.QRadioButton(self.page_3)
        self.eula_true1.setGeometry(QtCore.QRect(210, 220, 231, 21))
        self.eula_true1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eula_true1.setAcceptDrops(False)
        self.eula_true1.setChecked(False)
        self.eula_true1.setObjectName("eula_true1")
        self.eula.addButton(self.eula_true1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.back_button_3 = QtWidgets.QPushButton(self.page_4)
        self.back_button_3.setGeometry(QtCore.QRect(270, 300, 75, 23))
        self.back_button_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_3.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFD0D1;\n"
                                         "}")
        self.back_button_3.setObjectName("back_button_3")
        self.line_5 = QtWidgets.QFrame(self.page_4)
        self.line_5.setGeometry(QtCore.QRect(190, 80, 331, 1))
        self.line_5.setStyleSheet("border-top: 1px solid black;")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.next_button_4 = QtWidgets.QPushButton(self.page_4)
        self.next_button_4.setGeometry(QtCore.QRect(350, 300, 75, 23))
        self.next_button_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_button_4.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFD0D1;\n"
                                         "}")
        self.next_button_4.setObjectName("next_button_4")
        self.line_6 = QtWidgets.QFrame(self.page_4)
        self.line_6.setGeometry(QtCore.QRect(190, 290, 331, 1))
        self.line_6.setStyleSheet("border-top: 1px solid black;")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_5.setGeometry(QtCore.QRect(210, 90, 281, 191))
        self.textBrowser_5.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                         "\n"
                                         "text-decoration: none;\n"
                                         "")
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.cancel_button_4 = QtWidgets.QPushButton(self.page_4)
        self.cancel_button_4.setGeometry(QtCore.QRect(430, 300, 75, 23))
        self.cancel_button_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_button_4.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: #FFD0D1;\n"
                                           "}")
        self.cancel_button_4.setObjectName("cancel_button_4")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_6.setGeometry(QtCore.QRect(210, 40, 281, 35))
        self.textBrowser_6.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_7.setGeometry(QtCore.QRect(210, 10, 281, 31))
        self.textBrowser_7.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.stackedWidget.addWidget(self.page_4)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.next_button_2 = QtWidgets.QPushButton(self.page)
        self.next_button_2.setGeometry(QtCore.QRect(350, 300, 75, 23))
        self.next_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_button_2.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFD0D1;\n"
                                         "}")
        self.next_button_2.setObjectName("next_button_2")
        self.cancel_button_2 = QtWidgets.QPushButton(self.page)
        self.cancel_button_2.setGeometry(QtCore.QRect(430, 300, 75, 23))
        self.cancel_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_button_2.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: #FFD0D1;\n"
                                           "}")
        self.cancel_button_2.setObjectName("cancel_button_2")
        self.path_place = QtWidgets.QTextEdit(self.page)
        self.path_place.setGeometry(QtCore.QRect(210, 150, 281, 25))
        self.path_place.setStyleSheet("")
        self.path_place.setFrameShape(QtWidgets.QFrame.Box)
        self.path_place.setObjectName("path_place")
        self.locate_folder = QtWidgets.QPushButton(self.page)
        self.locate_folder.setGeometry(QtCore.QRect(410, 180, 75, 23))
        self.locate_folder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.locate_folder.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFD0D1;\n"
                                         "}")
        self.locate_folder.setObjectName("locate_folder")
        self.back_button = QtWidgets.QPushButton(self.page)
        self.back_button.setGeometry(QtCore.QRect(270, 300, 75, 23))
        self.back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #FFD0D1;\n"
                                       "}")
        self.back_button.setObjectName("back_button")
        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(190, 290, 331, 1))
        self.line_2.setStyleSheet("border-top: 1px solid black;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_8.setGeometry(QtCore.QRect(210, 10, 281, 31))
        self.textBrowser_8.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_9.setGeometry(QtCore.QRect(210, 40, 281, 35))
        self.textBrowser_9.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.line_7 = QtWidgets.QFrame(self.page)
        self.line_7.setGeometry(QtCore.QRect(190, 80, 331, 1))
        self.line_7.setStyleSheet("border-top: 1px solid black;")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.space_req = QtWidgets.QLineEdit(self.page)
        self.space_req.setGeometry(QtCore.QRect(210, 250, 291, 20))
        self.space_req.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.space_req.setFrame(False)
        self.space_req.setReadOnly(True)
        self.space_req.setObjectName("space_req")
        self.stackedWidget.addWidget(self.page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.line_8 = QtWidgets.QFrame(self.page_5)
        self.line_8.setGeometry(QtCore.QRect(190, 290, 331, 1))
        self.line_8.setStyleSheet("border-top: 1px solid black;")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.page_5)
        self.textBrowser_10.setGeometry(QtCore.QRect(210, 40, 281, 35))
        self.textBrowser_10.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.page_5)
        self.textBrowser_11.setGeometry(QtCore.QRect(210, 10, 281, 31))
        self.textBrowser_11.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.line_9 = QtWidgets.QFrame(self.page_5)
        self.line_9.setGeometry(QtCore.QRect(190, 80, 331, 1))
        self.line_9.setStyleSheet("border-top: 1px solid black;")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.download_progressBar = QtWidgets.QProgressBar(self.page_5)
        self.download_progressBar.setGeometry(QtCore.QRect(210, 110, 281, 21))
        self.download_progressBar.setProperty("value", 0)
        self.download_progressBar.setObjectName("download_progressBar")
        self.download_text = QtWidgets.QLineEdit(self.page_5)
        self.download_text.setGeometry(QtCore.QRect(210, 140, 171, 20))
        self.download_text.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.download_text.setFrame(False)
        self.download_text.setReadOnly(True)
        self.download_text.setObjectName("download_text")
        self.next_button_5 = QtWidgets.QPushButton(self.page_5)
        self.next_button_5.setEnabled(False)
        self.next_button_5.setGeometry(QtCore.QRect(350, 300, 75, 23))
        self.next_button_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_button_5.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFD0D1;\n"
                                         "}")
        self.next_button_5.setObjectName("next_button_5")
        self.cancel_button_5 = QtWidgets.QPushButton(self.page_5)
        self.cancel_button_5.setEnabled(False)
        self.cancel_button_5.setGeometry(QtCore.QRect(430, 300, 75, 23))
        self.cancel_button_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_button_5.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: #FFD0D1;\n"
                                           "}")
        self.cancel_button_5.setObjectName("cancel_button_5")
        self.label = QtWidgets.QLabel(self.page_5)
        self.label.setGeometry(QtCore.QRect(210, 86, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_5)
        self.label_2.setGeometry(QtCore.QRect(210, 180, 251, 20))
        self.label_2.setObjectName("label_2")
        self.creamapi_progressBar_2 = QtWidgets.QProgressBar(self.page_5)
        self.creamapi_progressBar_2.setGeometry(QtCore.QRect(210, 204, 281, 21))
        self.creamapi_progressBar_2.setProperty("value", 0)
        self.creamapi_progressBar_2.setObjectName("creamapi_progressBar_2")
        self.creamapi_label = QtWidgets.QLabel(self.page_5)
        self.creamapi_label.setGeometry(QtCore.QRect(210, 234, 281, 20))
        self.creamapi_label.setObjectName("creamapi_label")
        self.label_3 = QtWidgets.QLabel(self.page_5)
        self.label_3.setGeometry(QtCore.QRect(210, 260, 281, 20))
        self.label_3.setObjectName("label_3")
        self.speed_label = QtWidgets.QLabel(self.page_5)
        self.speed_label.setGeometry(QtCore.QRect(376, 140, 121, 20))
        self.speed_label.setObjectName("speed_label")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.page_6)
        self.textBrowser_12.setGeometry(QtCore.QRect(210, 10, 281, 31))
        self.textBrowser_12.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.line_11 = QtWidgets.QFrame(self.page_6)
        self.line_11.setGeometry(QtCore.QRect(190, 80, 331, 1))
        self.line_11.setStyleSheet("border-top: 1px solid black;")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.page_6)
        self.textBrowser_13.setGeometry(QtCore.QRect(210, 40, 281, 35))
        self.textBrowser_13.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.reinstall_button = QtWidgets.QPushButton(self.page_6)
        self.reinstall_button.setEnabled(True)
        self.reinstall_button.setGeometry(QtCore.QRect(350, 300, 75, 23))
        self.reinstall_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reinstall_button.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: #FFD0D1;\n"
                                            "}")
        self.reinstall_button.setObjectName("reinstall_button")
        self.cancel_button_6 = QtWidgets.QPushButton(self.page_6)
        self.cancel_button_6.setGeometry(QtCore.QRect(430, 300, 75, 23))
        self.cancel_button_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_button_6.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: #FFD0D1;\n"
                                           "}")
        self.cancel_button_6.setObjectName("cancel_button_6")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.page_6)
        self.textBrowser_14.setGeometry(QtCore.QRect(210, 100, 281, 35))
        self.textBrowser_14.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.finish_text = QtWidgets.QTextBrowser(self.page_7)
        self.finish_text.setGeometry(QtCore.QRect(210, 100, 281, 61))
        self.finish_text.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.finish_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.finish_text.setObjectName("finish_text")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.page_7)
        self.textBrowser_16.setGeometry(QtCore.QRect(210, 10, 281, 31))
        self.textBrowser_16.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.page_7)
        self.textBrowser_17.setGeometry(QtCore.QRect(210, 40, 281, 35))
        self.textBrowser_17.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.line_12 = QtWidgets.QFrame(self.page_7)
        self.line_12.setGeometry(QtCore.QRect(190, 80, 331, 1))
        self.line_12.setStyleSheet("border-top: 1px solid black;")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.finish_button = QtWidgets.QPushButton(self.page_7)
        self.finish_button.setEnabled(False)
        self.finish_button.setGeometry(QtCore.QRect(430, 300, 75, 23))
        self.finish_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.finish_button.setStyleSheet("QPushButton {border: 1px solid #B22222;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFD0D1;\n"
                                         "}")
        self.finish_button.setObjectName("finish_button")
        self.launch_game = QtWidgets.QCheckBox(self.page_7)
        self.launch_game.setGeometry(QtCore.QRect(210, 200, 121, 21))
        self.launch_game.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.launch_game.setObjectName("launch_game")
        self.checkBox = QtWidgets.QCheckBox(self.page_7)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(210, 250, 141, 21))
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.stackedWidget.addWidget(self.page_7)
        self.listWidget_5 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_5.setGeometry(QtCore.QRect(0, 0, 191, 291))
        self.listWidget_5.setStyleSheet("background-image: url(:/images/stallaris_ba (1).jpg);")
        self.listWidget_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_5.setObjectName("listWidget_5")
        self.version = QtWidgets.QLineEdit(self.centralwidget)
        self.version.setGeometry(QtCore.QRect(10, 300, 113, 20))
        self.version.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.version.setFrame(False)
        self.version.setReadOnly(True)
        self.version.setObjectName("version")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(190, 290, 331, 1))
        self.line_10.setStyleSheet("border-top: 1px solid black;")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_button.setText(_translate("MainWindow", "Далее"))
        self.cancel_button.setText(_translate("MainWindow", "Отмена"))
        self.hello_msg.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Вас приветствует Stellaris &quot;DLC Unlocker - Разблокировщик дополнений&quot; [unknown]</span></p></body></html>"))
        self.hello2_msg.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Программа выполнит разблокировку дополнений для игры Stellaris версии [unknown]</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Нажмите &quot;Далее&quot;, чтобы продолжить или &quot;Отмена&quot;, чтобы выйти из программы установки.</p></body></html>"))
        self.next_button_3.setText(_translate("MainWindow", "Далее"))
        self.cancel_button_3.setText(_translate("MainWindow", "Отмена"))
        self.back_button_2.setText(_translate("MainWindow", "Назад"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Информация</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пожалуйста, прочитие следующую важную информацию пред тем, как продолжить.</p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   1. Данный разблокировщик распространяется абсолютно бесплатно. Любое коммерческое использование данного разблокировщика запрещается.</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   2. ДАННЫЙ РАЗБЛОКИРОВЩИК ПОСТАВЛЯЕТСЯ ПО ПРИНЦИПУ «AS IS». НИКАКИХ ГАРАНТИЙ              НЕ ПРИЛАГАЕТСЯ И НЕ ПРЕДУСМАТРИВАЕТСЯ. ВЫ ИСПОЛЬЗУЕТЕ ЭТУ МОДИФИКАЦИЮ ОРИГИНАЛЬНОЙ ИГРЫ НА СВОЙ СТРАХ И РИСК. АВТОРЫ МОДИФИКАЦИИ НЕ БУДУТ ОТВЕЧАТЬ НИ ЗА КАКИЕ ПОТЕРИ ИЛИ ИСКАЖЕНИЯ ДАННЫХ, ЛЮБУЮ УПУЩЕННУЮ ВЫГОДУ В ПРОЦЕССЕ ИСПОЛЬЗОВАНИЯ ИЛИ НЕПРАВИЛЬНОГО ИСПОЛЬЗОВАНИЯ ДАННОЙ МОДИФИКАЦИИ.</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   4. Все права, не предоставленные здесь явно, сохраняются за правообладателями.</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   5. Установка и использование данной модификации означает, что вы ознакомились и понимаете положения настоящего лицензионного соглашения и согласны с ними.</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.eula_true.setText(_translate("MainWindow", "Я  принимаю условия соглашения"))
        self.eula_false.setText(_translate("MainWindow", "Я не принимаю условия соглашения"))
        self.eula_true1.setText(_translate("MainWindow", "Я ничего не читал, но со всем согласен"))
        self.back_button_3.setText(_translate("MainWindow", "Назад"))
        self.next_button_4.setText(_translate("MainWindow", "Далее"))
        self.textBrowser_5.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Stellaris DLC Unlocker</span></p>\n"
                                              "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Требования</span><span style=\" font-size:10pt; font-weight:600;\">:</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-weight:600;\">Лицензия</span><span style=\" font-size:10pt;\">: Steam.</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Установка</span><span style=\" font-size:10pt; font-weight:600;\">:</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span><span style=\" font-size:9pt;\"> Следуйте инструкциям инсталлятора. Установка почти полностью автоматическая. </span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Удаление</span><span style=\" font-size:10pt; font-weight:600;\">:</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span><span style=\" font-size:9pt;\"> Переустановите Paradox лаунчер, удалите папку &quot;dlc&quot; в директории игры. Не забудте заново скачать те dlc которые у вас приобретены.<br /><br />Сделано лично мной для всех<br /></span><img src=\":/images/telegram (1).png\" /><a href=\"https://t.me/seuyh\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">seuyh</span></a></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/GitHub-Logo.wine (1).png\" /><a href=\"https://github.com/seuyh\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">GitHub</span></a></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">Отдельная благодарность герою нашего времени, который все это делал для нас ручками </span><img src=\":/images/telegram (1).png\" /><a href=\"https://t.me/Temri1337\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">He11oThere</span></a></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"@Temri1337\"><span style=\" font-size:8pt; text-decoration: underline; color:#000000;\"><br /></span></a><a href=\"https://www.playground.ru/stellaris/cheat/stellaris_dlc_unlocker_razblokirovschik_dopolnenij_3_10-1088979#29894040\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">playground.ru Stellaris DLC Unlocker</span></a></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#0000ff;\"><br /></p></body></html>"))
        self.cancel_button_4.setText(_translate("MainWindow", "Отмена"))
        self.textBrowser_6.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пожалуйста, прочитие следующую важную информацию пред тем, как продолжить.</p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Информация</span></p></body></html>"))
        self.next_button_2.setText(_translate("MainWindow", "Далее"))
        self.cancel_button_2.setText(_translate("MainWindow", "Отмена"))
        self.locate_folder.setText(_translate("MainWindow", "Обзор..."))
        self.back_button.setText(_translate("MainWindow", "Назад"))
        self.textBrowser_8.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Выбор папки игры</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пожалуйста, укажите папку с игрой если мы не смогли найти ее автоматически.</p></body></html>"))
        self.space_req.setText(_translate("MainWindow", "Требуется дополнительно %nan%  места"))
        self.textBrowser_10.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пожалуйста, подождите пока мы загрузим все нужные файлы с сервера.</p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Загрузка DLC</span></p></body></html>"))
        self.download_text.setText(_translate("MainWindow", "Подключение к серверу..."))
        self.next_button_5.setText(_translate("MainWindow", "Далее"))
        self.cancel_button_5.setText(_translate("MainWindow", "Отмена"))
        self.label.setText(_translate("MainWindow", "Загрузка DLC:"))
        self.label_2.setText(_translate("MainWindow", "Генерация creamapi:"))
        self.creamapi_label.setText(_translate("MainWindow", "Получение инфо о dlc: подключение к api"))
        self.label_3.setText(_translate("MainWindow", "Скорость генерации зависит от сервера."))
        self.speed_label.setText(_translate("MainWindow", "Скорость: %nan%"))
        self.textBrowser_12.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Переустановка лаунчера</span></p></body></html>"))
        self.textBrowser_13.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Необходимо переустановить Paradox лаунчер для корректной работы.</p></body></html>"))
        self.reinstall_button.setText(_translate("MainWindow", "Хорошо"))
        self.cancel_button_6.setText(_translate("MainWindow", "Отмена"))
        self.textBrowser_14.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Программа почти все сделает автоматически, вам нужно лишь следовать указаниям на экране.</p></body></html>"))
        self.finish_text.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Перезаписываем оставшиеся файлы.<br /><br />Пожалуйста подождите немного.</p></body></html>"))
        self.textBrowser_16.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Завершение</span></p></body></html>"))
        self.textBrowser_17.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Мы уже почти все доделали, осталось немного подождать.</p></body></html>"))
        self.finish_button.setText(_translate("MainWindow", "Готово"))
        self.launch_game.setText(_translate("MainWindow", "Запустить игру"))
        self.checkBox.setText(_translate("MainWindow", "Автор крутой"))
        self.version.setText(_translate("MainWindow", "version %nan%"))
