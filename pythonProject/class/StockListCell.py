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


class StockListCell(QtGui.QWidget):
    def __init__(self):
        super(StockListCell, self).__init__()

    def setupUi(self, code, name, itemWidget=None):
        self.setObjectName(_fromUtf8("Form"))
        self._code = code
        self._name = name
        self.delButton = QtGui.QPushButton(self)
        self.delButton.setGeometry(QtCore.QRect(80, 10, 30, 30))
        self.delButton.setObjectName(_fromUtf8("delButton"))
        self.delButton.clicked.connect(self.delBtnPress)
        self.codeLabel = QtGui.QLabel(self)
        self.codeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.codeLabel.setGeometry(QtCore.QRect(10, 5, 55, 21))
        self.codeLabel.setObjectName(_fromUtf8("codeLabel"))
        self.namelabel = QtGui.QLabel(self)
        self.namelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.namelabel.setGeometry(QtCore.QRect(10, 4+21, 55, 21))
        self.namelabel.setObjectName(_fromUtf8("namelabel"))
        self.listWidgetItem = QtGui.QListWidgetItem(" ", itemWidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.delButton.setText(_translate("Form", "x", None))
        self.codeLabel.setText(_translate("Form", self._code, None))
        self.namelabel.setText(_translate("Form", self._name, None))

    def resize_(self, QSize):
        self.resize(QSize)
        self.listWidgetItem.setSizeHint(QSize)

    def code(self):
        return self._code

    def name(self):
        return self._name

    def delBtnCallBack(self, code, name):
        raise 'delBtnCallBack must be rewrited'

    def delBtnPress(self):
        self.delBtnCallBack(self.code(), self.name())
