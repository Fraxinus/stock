# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StockListCell.ui'
#
# Created: Thu Feb 12 20:12:43 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


__cellSize__ = QtCore.QSize(115, 50)
QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))

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
    def setupUi(self, Form, code, name):
        Form.setObjectName(_fromUtf8("Form"))
        # Form.resize(__cellSize__)
        self.form = Form
        self.code = code
        self.name = name
        self.delButton = QtGui.QPushButton(Form)
        self.delButton.setGeometry(QtCore.QRect(80, 10, 30, 30))
        self.delButton.setObjectName(_fromUtf8("delButton"))
        self.codeLabel = QtGui.QLabel(Form)
        self.codeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.codeLabel.setGeometry(QtCore.QRect(10, 5, 55, 21))
        self.codeLabel.setObjectName(_fromUtf8("codeLabel"))
        self.namelabel = QtGui.QLabel(Form)
        self.namelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.namelabel.setGeometry(QtCore.QRect(10, 4+21, 55, 21))
        self.namelabel.setObjectName(_fromUtf8("namelabel"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.delButton.setText(_translate("Form", "x", None))
        self.codeLabel.setText(_translate("Form", self.code, None))
        self.namelabel.setText(_translate("Form", self.name, None))

