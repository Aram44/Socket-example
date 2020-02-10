# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Aram\Documents\test.ui'
#
# Created: Fri Nov 29 23:12:36 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowIcon(QtGui.QIcon('icon.ico'))
        Form.setEnabled(True)
        Form.resize(500, 300)
        Form.setMinimumSize(QtCore.QSize(500, 300))
        Form.setMaximumSize(QtCore.QSize(500, 300))
        Form.setStyleSheet("QWidget{\n"
"background-color: #333333;\n"
"}\n"
"QTextBrowser{\n"
"color: #ffffff;\n"
"}\n"
"QLabel{\n"
"color: #ffffff;\n"
"}\n"
"QLineEdit{\n"
"color:#ffffff;\n"
"width: 120px;\n"
"background-color: #333333;\n"
"}\n"
"QScrollBar{\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"border: none;\n"
"}\n"
"QPushButton{\n"
"background-color: #333333;\n"
"color: #ffffff;\n"
"border: none;\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"width: 80px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ffffff;\n"
"color: #333333;\n"
"}")
        self.sendbtn = QtGui.QPushButton(Form)
        self.sendbtn.setGeometry(QtCore.QRect(430, 0, 75, 41))
        self.sendbtn.setStyleSheet("")
        self.sendbtn.setObjectName("sendbtn")
        self.ipadr = QtGui.QLineEdit(Form)
        self.ipadr.setGeometry(QtCore.QRect(0, 20, 91, 20))
        self.ipadr.setObjectName("lineEdit")
        self.msge = QtGui.QLineEdit(Form)
        self.msge.setGeometry(QtCore.QRect(263, 20, 163, 20))
        self.msge.setObjectName("lineEdit_2")
        self.keys = QtGui.QLineEdit(Form)
        self.keys.setGeometry(QtCore.QRect(197, 20, 62, 20))
        self.keys.setObjectName("lineEdit_3")
        self.names = QtGui.QLineEdit(Form)
        self.names.setGeometry(QtCore.QRect(95, 20, 98, 20))
        self.names.setObjectName("lineEdit_4")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(5, 0, 61, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(263, 0, 46, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(197, 0, 50, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(95, 0, 47, 13))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 40, 501, 261))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Messenger", None, QtGui.QApplication.UnicodeUTF8))
        self.sendbtn.setText(QtGui.QApplication.translate("Form", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "IP adress", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Message", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))



