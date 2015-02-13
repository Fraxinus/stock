# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StocksDetailWindow.ui'
#
# Created: Thu Feb 12 12:05:47 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import StockListCell

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
    def setupUi(self, Form):
        self.window = Form
        self.father = None
        self.fatherShow = Form.show
        Form.show = self.show
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(923, 480)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 138, 481))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.leftVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.leftVerticalLayout.setMargin(0)
        self.leftVerticalLayout.setObjectName(_fromUtf8("leftVerticalLayout"))
        self.cycleGroupBox = QtGui.QGroupBox(Form)
        self.cycleGroupBox.setGeometry(QtCore.QRect(790, 90, 120, 80))
        self.cycleGroupBox.setObjectName(_fromUtf8("cycleGroupBox"))
        self.dayRadioButton = QtGui.QRadioButton(self.cycleGroupBox)
        self.dayRadioButton.setGeometry(QtCore.QRect(10, 20, 89, 16))
        self.dayRadioButton.setObjectName(_fromUtf8("dayRadioButton"))
        self.weekRadioButton = QtGui.QRadioButton(self.cycleGroupBox)
        self.weekRadioButton.setGeometry(QtCore.QRect(10, 40, 89, 16))
        self.weekRadioButton.setObjectName(_fromUtf8("weekRadioButton"))
        self.yearRadioButton = QtGui.QRadioButton(self.cycleGroupBox)
        self.yearRadioButton.setGeometry(QtCore.QRect(10, 60, 89, 16))
        self.yearRadioButton.setObjectName(_fromUtf8("yearRadioButton"))
        self.ShowStyleGroupBox = QtGui.QGroupBox(Form)
        self.ShowStyleGroupBox.setGeometry(QtCore.QRect(790, 240, 120, 100))
        self.ShowStyleGroupBox.setObjectName(_fromUtf8("ShowStyleGroupBox"))
        self.lineRadioButton = QtGui.QRadioButton(self.ShowStyleGroupBox)
        self.lineRadioButton.setGeometry(QtCore.QRect(10, 20, 89, 16))
        self.lineRadioButton.setObjectName(_fromUtf8("lineRadioButton"))
        self.kLineRadioButton = QtGui.QRadioButton(self.ShowStyleGroupBox)
        self.kLineRadioButton.setGeometry(QtCore.QRect(10, 50, 89, 16))
        self.kLineRadioButton.setObjectName(_fromUtf8("kLineRadioButton"))
        self.DataRangeGroupBox = QtGui.QGroupBox(Form)
        self.DataRangeGroupBox.setGeometry(QtCore.QRect(280, 400, 431, 51))
        self.DataRangeGroupBox.setObjectName(_fromUtf8("DataRangeGroupBox"))
        self.dateStartEdit = QtGui.QDateEdit(self.DataRangeGroupBox)
        self.dateStartEdit.setCalendarPopup(True)
        self.dateStartEdit.setGeometry(QtCore.QRect(30, 20, 110, 22))
        self.dateStartEdit.setObjectName(_fromUtf8("dateStartEdit"))
        self.dateEndEdit = QtGui.QDateEdit(self.DataRangeGroupBox)
        self.dateEndEdit.setCalendarPopup(True)
        self.dateEndEdit.setGeometry(QtCore.QRect(190, 20, 110, 22))
        self.dateEndEdit.setObjectName(_fromUtf8("dateEndEdit"))
        self.refreshDateButton = QtGui.QPushButton(self.DataRangeGroupBox)
        self.refreshDateButton.setGeometry(QtCore.QRect(330, 20, 75, 23))
        self.refreshDateButton.setObjectName(_fromUtf8("refreshDateButton"))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 0, 611, 391))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.centerGridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.centerGridLayout.setMargin(0)
        self.centerGridLayout.setObjectName(_fromUtf8("centerGridLayout"))

        self.testButton = QtGui.QPushButton(self.ShowStyleGroupBox)
        self.testButton.setGeometry(QtCore.QRect(10, 76, 89, 16))
        self.testButton.setObjectName(_fromUtf8("testPushButton"))
        self.testButton.clicked.connect(self.test)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.closeEvent = self.closeEvent

        self._initStockListView()
        return self

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.cycleGroupBox.setTitle(_translate("Form", "Cycle", None))
        self.dayRadioButton.setText(_translate("Form", "day", None))
        self.weekRadioButton.setText(_translate("Form", "week", None))
        self.yearRadioButton.setText(_translate("Form", "year", None))
        self.ShowStyleGroupBox.setTitle(_translate("Form", "Show Style", None))
        self.lineRadioButton.setText(_translate("Form", "line", None))
        self.kLineRadioButton.setText(_translate("Form", "K line", None))
        self.DataRangeGroupBox.setTitle(_translate("Form", "Date Range", None))
        self.refreshDateButton.setText(_translate("Form", "refresh", None))
        self.testButton.setText(_translate("Form", "test", None))

    def setDelegate(self, father):
        print 'analysisWindow set delegate' + str(type(father))
        if 'StockMainWindow' in str(type(father)):
            self.father = father
        else:
            raise 'analysisWindow init error,the second param must be StocksDetailWindow'

    def show(self):
        print 'analysisWindow show'
        if not self.father:
            raise 'analysisWindow show error,StocksDetailWindow.setDelegate(StockMainWindow father)must be call before show'
        self.fatherShow()

    def _initStockListView(self):
        self.stockListWidget = QtGui.QListWidget(self.verticalLayoutWidget)
        self.stockListWidget.setObjectName(_fromUtf8("stockListView"))
        self.leftVerticalLayout.addWidget(self.stockListWidget)
        self.stockListWidget.clicked.connect(self.stockListClick)
        self.stockListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.stockListWidget.connect(self.stockListWidget, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.listItemRightClicked)

        list_data = [1, 2, 3, 4]
        listItem = QtGui.QListWidgetItem("123\r\n\r\n100", self.stockListWidget)
        listItem.setSizeHint(__cellSize__)
        listItem2 = QtGui.QListWidgetItem("222", self.stockListWidget)
        self.stockListWidget.addItem(listItem)
        self.stockListWidget.addItem(listItem2)

    def stockListClick(self, modelIndex):
        print u'你选择的是{0}'.format(modelIndex.row())
        print dir(modelIndex)

    def insertStock(self, code, name):
        print 'insertStock',code,name
        listItem = QtGui.QListWidgetItem(" ", self.stockListWidget)
        listItem.setSizeHint(__cellSize__)

        form = QtGui.QWidget()
        cell = StockListCell.Ui_Form()
        cell.setupUi(form, code, name)
        cell.form.resize(__cellSize__)
        self.stockListWidget.setItemWidget(listItem, cell.form)


    def listItemRightClicked(self):
        print 'right click'

    def rebuildListWidget(self):
        self.stockListWidget.clear()
        items=self.listItems.keys()
        if len(items)>1: items.sort()
        for listItemName in items:
            listItem = QtGui.QListWidgetItem(listItemName, self.stockListWidget)
            self.listItems[listItemName]=listItem


    def test(self):
        print 'test'
        print self.stockListWidget.item(0).text().toUtf8().data()
        print self.father.code
        listItem = QtGui.QListWidgetItem("ttt\r\n\r\n100", self.stockListWidget)
        listItem.setText(" ")
        listItem.setSizeHint(__cellSize__)
        # self.stockListWidget.addItem(listItem)

        form = QtGui.QWidget()
        cell = StockListCell.Ui_Form().setupUi(form)
        # cell.setupUi(form)
        # form.show()
        btn = QtGui.QPushButton('btn')
        # cell.setGeometry(QtCore.QRect(10, 76, 10, 10))
        self.stockListWidget.setItemWidget(listItem, cell)

    def closeEvent(self, event):
        print 'analysisWindow close'
        self.father.closeAnalysisWindow()

    def close(self):
        self.window.close()

    def raise_(self):
        """
        bing window to top
        """
        self.window.raise_()


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    #Form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    window = Ui_Form()
    window.setupUi(Form)
    Form.show()
    # in mac, cant get on top auto when start,
    # add raise_() to solve that
    if sys.platform == 'darwin':
        Form.raise_()
    sys.exit(app.exec_())