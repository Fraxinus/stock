# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StockListCell.ui'
#
# Created: Thu Feb 12 20:12:43 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


__cellSize__ = QtCore.QSize(115, 50)
__styleFormat__ = 'border:0px groove gray;border-radius:15px;' \
                  'padding:1px 2px;background-color:rgb(%d,%d,%d);'
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
        self.codeLabel.setGeometry(QtCore.QRect(15, 5, 55, 21))
        self.codeLabel.setObjectName(_fromUtf8("codeLabel"))
        self.nameLabel = QtGui.QLabel(self)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setGeometry(QtCore.QRect(15, 4 + 21, 55, 21))
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.listWidgetItem = QtGui.QListWidgetItem(" ", itemWidget)
        self.listWidgetItem.setBackgroundColor(QtGui.QColor('lightgrey'))
        self.hintColor = None

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.delButton.setText(_translate("Form", "X", None))
        self.codeLabel.setText(_translate("Form", self._code, None))
        self.nameLabel.setText(_translate("Form", self._name, None))

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

    def setHintColor(self, r, g, b):
        self.hintColor = QtGui.QColor(r, g, b)
        palette = self.delButton.palette()
        palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor('black'))
        self.delButton.setPalette(palette)
        style = __styleFormat__ % (r, g, b)
        self.delButton.setStyleSheet(style)
        palette = self.nameLabel.palette()
        palette.setColor(QtGui.QPalette.Text, self.hintColor)
        self.nameLabel.setPalette(palette)
        self.codeLabel.setPalette(palette)
