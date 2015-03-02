# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StocksDetailWindow.ui'
#
# Created: Thu Feb 12 12:05:47 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
from StockListCell import StockListCell
from StocksGraph import StocksGraphView
import random

__cellSize__ = QtCore.QSize(115, 50)
__dateFormat__ = 'yyyy-MM-dd'
QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))


def _changeStrToQDate(date):
    return QtCore.QDateTime.fromString(date, __dateFormat__)


def _changeQDateToStr(qDate):
    return qDate.toString(__dateFormat__).toUtf8().data()

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
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1280, 640)
        windowRect = Form.rect()
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 138, 481))
        self.verticalLayoutWidget.setGeometry(1, 1, 138, windowRect.height() - 2)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.leftVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.leftVerticalLayout.setMargin(0)
        self.leftVerticalLayout.setObjectName(_fromUtf8("leftVerticalLayout"))
        self.cycleGroupBox = QtGui.QGroupBox(Form)
        self.cycleGroupBox.setGeometry(QtCore.QRect(windowRect.width() - 80 - 5, 90, 80, 80))
        self.cycleGroupBox.setObjectName(_fromUtf8("cycleGroupBox"))
        self.dayRadioButton = QtGui.QRadioButton(self.cycleGroupBox)
        self.dayRadioButton.setGeometry(QtCore.QRect(10, 20, 89, 18))
        self.dayRadioButton.setObjectName(_fromUtf8("dayRadioButton"))
        self.weekRadioButton = QtGui.QRadioButton(self.cycleGroupBox)
        self.weekRadioButton.setGeometry(QtCore.QRect(10, 40, 89, 18))
        self.weekRadioButton.setObjectName(_fromUtf8("weekRadioButton"))
        self.yearRadioButton = QtGui.QRadioButton(self.cycleGroupBox)
        self.yearRadioButton.setGeometry(QtCore.QRect(10, 60, 89, 18))
        self.yearRadioButton.setObjectName(_fromUtf8("yearRadioButton"))
        self.ShowStyleGroupBox = QtGui.QGroupBox(Form)
        self.ShowStyleGroupBox.setGeometry(QtCore.QRect(windowRect.width() - 80 - 5, 240, 80, 100))
        self.ShowStyleGroupBox.setObjectName(_fromUtf8("ShowStyleGroupBox"))
        self.lineRadioButton = QtGui.QRadioButton(self.ShowStyleGroupBox)
        self.lineRadioButton.setGeometry(QtCore.QRect(10, 20, 89, 18))
        self.lineRadioButton.setObjectName(_fromUtf8("lineRadioButton"))
        self.kLineRadioButton = QtGui.QRadioButton(self.ShowStyleGroupBox)
        self.kLineRadioButton.setGeometry(QtCore.QRect(10, 50, 89, 18))
        self.kLineRadioButton.setObjectName(_fromUtf8("kLineRadioButton"))
        self.DataRangeGroupBox = QtGui.QGroupBox(Form)
        self.DataRangeGroupBox.setGeometry(QtCore.QRect(280, windowRect.height() - 51 - 5, 431, 51))
        self.DataRangeGroupBox.setObjectName(_fromUtf8("DataRangeGroupBox"))
        self.dateStartEdit = QtGui.QDateEdit(self.DataRangeGroupBox)
        self.dateStartEdit.setCalendarPopup(True)
        self.dateStartEdit.setDisplayFormat('yyyy-MM-dd')
        self.dateStartEdit.dateChanged.connect(self._startDateChangedEvent)
        self.dateStartEdit.setGeometry(QtCore.QRect(30, 20, 110, 22))
        self.dateStartEdit.setObjectName(_fromUtf8("dateStartEdit"))
        self.dateEndEdit = QtGui.QDateEdit(self.DataRangeGroupBox)
        self.dateEndEdit.setCalendarPopup(True)
        self.dateEndEdit.setDisplayFormat('yyyy-MM-dd')
        self.dateEndEdit.dateChanged.connect(self._endDateChangedEvent)
        self.dateEndEdit.setGeometry(QtCore.QRect(160, 20, 110, 22))
        self.dateEndEdit.setObjectName(_fromUtf8("dateEndEdit"))
        self.refreshDateButton = QtGui.QPushButton(self.DataRangeGroupBox)
        self.refreshDateButton.setGeometry(QtCore.QRect(280, 10, 75, 23))
        self.refreshDateButton.clicked.connect(self._refreshDatePress)
        self.refreshDateButton.setObjectName(_fromUtf8("refreshDateButton"))
        self.refreshDateButton.setEnabled(False)
        self.undoDateButton = QtGui.QPushButton(self.DataRangeGroupBox)
        self.undoDateButton.setGeometry(QtCore.QRect(280, 28, 75, 23))
        self.undoDateButton.clicked.connect(self._undoDateChangePress)
        self.undoDateButton.setObjectName(_fromUtf8("undoDateButton"))
        self.refreshLockChk = QtGui.QCheckBox(self.DataRangeGroupBox)
        self.refreshLockChk.setGeometry(QtCore.QRect(360, 20, 55, 23))
        self.window.connect(self.refreshLockChk, QtCore.SIGNAL("	stateChanged(int)"), self._refreshLockChangeEvent)
        self.refreshLockChk.setObjectName(_fromUtf8("refreshLockChk"))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(
            QtCore.QRect(138 + 5,
                         0,
                         windowRect.width() - 138 - 5 - 80 - 5 - 5,
                         windowRect.height() - 51))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.centerGridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.centerGridLayout.setMargin(0)
        self.centerGridLayout.setObjectName(_fromUtf8("centerGridLayout"))

        self.testButton = QtGui.QPushButton(self.ShowStyleGroupBox)
        self.testButton.setGeometry(QtCore.QRect(10, 76, 89, 16))
        self.testButton.setObjectName(_fromUtf8("testPushButton"))
        self.testButton.clicked.connect(self.test)

        self.stocksGraphView = StocksGraphView(self)
        self.stocksGraphView.setFocus(QtCore.Qt.ClickFocus)
        self.centerGridLayout.addWidget(self.stocksGraphView.canvas)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.closeEvent = self.closeEvent
        Form.keyPressEvent = self._keyPressEvent

        self.cells_dic = {}
        self.stocksDailyData_decomposed_dic = {}
        self.QColor_list = QtGui.QColor.colorNames()
        self.earlistDay = QtCore.QDateTime.fromString(self.window.tr('2100-01-01'), self.window.tr(__dateFormat__))
        self.lastDay = QtCore.QDateTime.fromString(self.window.tr('1900-01-01'), self.window.tr(__dateFormat__))
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
        self.refreshLockChk.setText(_translate("Form", "lock", None))
        self.undoDateButton.setText(_translate("Form", "undo", None))


    def setDelegate(self, father):
        print 'analysisWindow set delegate' + str(type(father))
        if 'StockMainWindow' in str(type(father)):
            self.father = father
        else:
            raise 'analysisWindow init error,the second param must be StocksDetailWindow'

    def _initStockListView(self):
        self.stockListWidget = QtGui.QListWidget(self.verticalLayoutWidget)
        self.stockListWidget.setObjectName(_fromUtf8("stockListView"))

        palette = self.stockListWidget.palette()
        palette.setBrush(QtGui.QPalette.Highlight, QtGui.QBrush(QtGui.QColor('mediumpurple')))
        self.stockListWidget.setPalette(palette)

        self.leftVerticalLayout.addWidget(self.stockListWidget)
        self.stockListWidget.clicked.connect(self.stockListClick)
        self.stockListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.stockListWidget.connect(self.stockListWidget,
                                     QtCore.SIGNAL("customContextMenuRequested(QPoint)"),
                                     self.listItemRightClicked)

    def _initPos(self):
        self.window.move(self.father.window.pos().x() + 120,
                         self.father.window.pos().y() + 50)

    def stockListClick(self, cellIndex):
        print u'你选择的是{0}'.format(cellIndex.row())
        print dir(cellIndex)
        curListWidgetItem = self.stockListWidget.item(cellIndex.row())
        for code, cell in self.cells_dic.iteritems():
            if cell.listWidgetItem == curListWidgetItem:
                print cell.code()
                return

    def insertStock(self, code, name):
        """
        If the stock is in list,set focus,
        else load stock data,
        create widgetItem,and save in self.cells_dic
        """
        print 'AnalysisWindow: insertStock', code, name
        if code in self.cells_dic:
            print 'AnalysisWindow: insertStock exist', code
            self.stockListWidget.setCurrentItem(self.cells_dic[code].listWidgetItem)
            return True

        ret = self.insertedStockData(code)  # load data
        if not ret:  # load data fail
            print "AnalysisWindow: no data", code
            return False

        cell = StockListCell()
        cell.setupUi(code, name, itemWidget=self.stockListWidget)
        cell.resize_(__cellSize__)
        cell.setHintColor(*self.randomColor_rgb())
        cell.delBtnCallBack = self.removeStockByCellDelBtn
        self.stockListWidget.setItemWidget(cell.listWidgetItem, cell)
        self.stockListWidget.setCurrentItem(cell.listWidgetItem)
        self.cells_dic[code] = cell
        self.addLinePlot(code, needRedrawXLabel=True)
        self.stocksGraphView.draw()
        return True

    def selectStockItem(self, code):
        self.stockListWidget.setCurrentItem(self.cells_dic[code].listWidgetItem)

    def randomColor_rgb(self):
        r = 0
        g = 0
        b = 0
        while 1:
            if 0 == len(self.QColor_list):
                self.QColor_list = QtGui.QColor.colorNames()
            count = len(self.QColor_list)
            randomIndex = random.randint(0, count - 1)
            colorName = self.QColor_list[randomIndex]
            del self.QColor_list[randomIndex]
            qColor = QtGui.QColor(colorName)
            r, g, b = qColor.red(), qColor.green(), qColor.blue()
            if (r + g + b) < (210 * 3):
                break
        print r, g, b
        return r, g, b

    def insertedStockData(self, code):
        print 'analysisWindow:insertedStockData'
        """
        Load stock data from db,
        Decompose stock data for some list,
        Update date range,
        Refresh plot
        :param code:
        :return:
        """
        def _decompose(list):
            dic = {'high': [], 'adj_close': [], 'volume': [], 'low': [], 'date': [], 'close': [], 'open': []}
            for daily_data in list:
                for key, value in daily_data.iteritems():
                    dic[key].append(value)
            return dic

        if not self.refreshLockChk.isChecked():  # Date range is not locked
            stockDailyData = self.father.getStockDayData(code)
        else:
            stockDailyData = self.father.getStockDayData(code,
                                                         _changeQDateToStr(self.earlistDay),
                                                         _changeQDateToStr(self.lastDay))

        if None == stockDailyData or len(stockDailyData) == 0:
            print "AnalysisWindow: load stockDailyData error"
            return False

        self.stocksDailyData_decomposed_dic[code] = _decompose(stockDailyData)
        if self.refreshLockChk.isChecked():  # Date range is locked
            print "AnalysisWindow: Date range is locked"
            return True
        #Date range is larger?
        stockEarlistDay = _changeStrToQDate(stockDailyData[0]["date"])
        stockLastDay = _changeStrToQDate(stockDailyData[len(stockDailyData) - 1]["date"])
        if stockEarlistDay < self.earlistDay:
            self.earlistDay = stockEarlistDay
        if stockLastDay > self.lastDay:
            self.lastDay = stockLastDay
        self._refreshDateWhenLoad()
        return True

    def addLinePlot(self, code, needRedrawXLabel):
        qColor = self.cells_dic[code].hintColor
        dailyData = self.stocksDailyData_decomposed_dic[code]
        self.stocksGraphView.addDateLine(dailyData['date'], dailyData['close'],
                                         code, qColor.red(), qColor.green(), qColor.blue(),
                                         needRedrawXLabel=needRedrawXLabel)

    def removeStockByCellDelBtn(self, code, name):
        """
        Rewrite the StockListCell.delBtnCallBack.
        When click the X button,remove the item.
        If the last stock is removed,close this window.
        :param code:The cell pass the code witch the X button you click.
        :param name:The same to code.
        """
        print 'removeStockByCellDelBtn', code, name
        cell = self.cells_dic[code]
        row = self.stockListWidget.row(cell.listWidgetItem)
        item_deleted = self.stockListWidget.takeItem(row)
        del item_deleted
        del self.cells_dic[code]
        del self.stocksDailyData_decomposed_dic[code]
        self.stocksGraphView.removeLineByCode(code)
        self.stocksGraphView.draw()
        if len(self.cells_dic) == 0:
            self.close()

    def listItemRightClicked(self):
        print 'right click'

    def test(self):
        print 'test'

        print

    def _refreshDateWhenLoad(self):
        print 'analysisWindow:refreshDate'
        self.dateStartEdit.setDate(self.earlistDay.date())
        self.dateEndEdit.setDate(self.lastDay.date())

    def _refreshDatePress(self):
        startChanged = self.dateStartEdit.dateTime()
        lastChanged = self.dateEndEdit.dateTime()
        if self.earlistDay == startChanged and self.lastDay == lastChanged:
            print 'Date range have not changed'
            return

        self.earlistDay = startChanged
        self.lastDay = lastChanged

        for code in self.cells_dic.iterkeys():
            self.stocksGraphView.removeLineByCode(code)
            self.insertedStockData(code)
            self.addLinePlot(code, needRedrawXLabel=False)
        self.stocksGraphView.draw()

    def _undoDateChangePress(self):
        self.dateStartEdit.setDate(self.earlistDay.date())
        self.dateEndEdit.setDate(self.lastDay.date())

    def _startDateChangedEvent(self, QDate):
        print 'start', QDate

    def _endDateChangedEvent(self, QDate):
        print "end", QDate

    def _refreshLockChangeEvent(self, stat):
        if stat == QtCore.Qt.Checked:
            self.dateStartEdit.setEnabled(False)
            self.dateEndEdit.setEnabled(False)
            self.refreshDateButton.setEnabled(True)
        else:
            self.dateStartEdit.setEnabled(True)
            self.dateEndEdit.setEnabled(True)
            self.refreshDateButton.setEnabled(False)


    def _keyPressEvent(self, QKeyEvent):
        """
        Rewrite self.window.keyPressEvent
        """
        print 'Analysis key press', QKeyEvent.key()
        if QKeyEvent.key() == QtCore.Qt.Key_Escape:
            self.close()

    def show(self):
        print 'analysisWindow show'
        if not self.father:
            raise 'analysisWindow show error,StocksDetailWindow.setDelegate(StockMainWindow father)must be call before show'
        self._initPos()
        self.window.show()

    def closeEvent(self, event):
        """
        Use to rewrite the window.closeEvent.
        Call father's function to close this class.
        """
        print 'analysisWindow closeEvent'
        self.stockListWidget.clear()
        del self.cells_dic
        self.centerGridLayout.removeWidget(self.stocksGraphView.canvas)
        self.stocksGraphView = None
        self.father.closeAnalysisWindowNotify()
        self.father = None
        self.window = None

    def close(self):
        print 'analysisWindow close'
        self.window.close()

    def raise_(self):
        """
        bing window to top
        """
        self.window.raise_()

    def __init__(self):
        print 'AnalysisView alloc'
    def __del__(self):
        print 'AnalysisView dealloc'


if __name__ == '__main__':
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