# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'portDeviceEmulatorUI.ui'
#
# Created: Mon Mar 16 21:10:35 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(316, 389)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(130, 10, 20, 171))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.startButton = QtGui.QPushButton(Form)
        self.startButton.setGeometry(QtCore.QRect(150, 40, 141, 31))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.boxTextEdit = QtGui.QTextEdit(Form)
        self.boxTextEdit.setEnabled(False)
        self.boxTextEdit.setGeometry(QtCore.QRect(10, 210, 291, 161))
        self.boxTextEdit.setObjectName(_fromUtf8("boxTextEdit"))
        self.resetButton = QtGui.QPushButton(Form)
        self.resetButton.setGeometry(QtCore.QRect(150, 80, 141, 31))
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.aboutButton = QtGui.QPushButton(Form)
        self.aboutButton.setGeometry(QtCore.QRect(250, 10, 41, 23))
        self.aboutButton.setObjectName(_fromUtf8("aboutButton"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 121, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.portComboBox = QtGui.QComboBox(self.layoutWidget)
        self.portComboBox.setObjectName(_fromUtf8("portComboBox"))
        self.horizontalLayout.addWidget(self.portComboBox)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(150, 10, 81, 21))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.labelID = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelID.setFont(font)
        self.labelID.setObjectName(_fromUtf8("labelID"))
        self.horizontalLayout_2.addWidget(self.labelID)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Port Device Emulator", None))
        self.label_2.setText(_translate("Form", "Transmission parameters", None))
        self.startButton.setText(_translate("Form", "START", None))
        self.label_3.setText(_translate("Form", "Communication box", None))
        self.resetButton.setText(_translate("Form", "RESET", None))
        self.aboutButton.setText(_translate("Form", "About", None))
        self.label.setText(_translate("Form", "PORT:", None))
        self.label_4.setText(_translate("Form", "ID: ", None))
        self.labelID.setText(_translate("Form", "1", None))

