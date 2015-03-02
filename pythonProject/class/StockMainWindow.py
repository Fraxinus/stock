#coding=utf-8

# Form implementation generated from reading ui file 'StockMainWindow.ui'
#
# Created: Sun Jan 25 16:21:02 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import StockData
import threading
import functools
import StocksAnalysisWindow

import time

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

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))
__enumError__ = -1


def async(wrapped):
        def wrapper(*args, **kwargs):
            t = threading.Thread(target=wrapped, args=args, kwargs=kwargs)
            t.daemon = True
            t.start()

        functools.update_wrapper(wrapper, wrapped)
        return wrapper



class StockMainWindow(object):
    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(812, 600)
        MainWindow.move(30, 60)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 791, 431))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stockTable = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.stockTable.setObjectName(_fromUtf8("stockCView"))
        self.verticalLayout.addWidget(self.stockTable)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.horizontalLayout.addWidget(self.searchEdit)
        self.searchSubmitBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.searchSubmitBtn.setObjectName(_fromUtf8("searchSubmitBtn"))
        self.horizontalLayout.addWidget(self.searchSubmitBtn)
        self.testBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.testBtn.setObjectName(_fromUtf8("testBtn"))
        self.testBtn.clicked.connect(self.test)
        self.horizontalLayout.addWidget(self.testBtn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 490, 811, 61))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.closeEvent = self.closeEvent


        # info = "  <font style='color: green;background: white;'>this is a test for change the fg & bg color ,text info</font>"
        # self.statueLabel.setText(info)
        self.StockAnalysisWindow = None
        self._initMenuBar()
        self._initStatusBar()
        self._initTableView()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.window.connect(self.window, QtCore.SIGNAL('exit()'), QtCore.SLOT('close()'))
        self.centralwidget.resizeEvent = self.layoutautoResizeEvent

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.searchEdit.setPlaceholderText(_translate("MainWindow", "code or name", None))
        self.searchSubmitBtn.setText(_translate("MainWindow", "search", None))
        self.testBtn.setText(_translate("MainWindow", "test", None))
        self.statusLabels['status'].setText(_translate("MainWindow", "status", None))
        self.statusLabels['ip'].setText(_translate("MainWindow", "ip:未连接", None))
        self.statusLabels['exchange'].setText(_translate("MainWindow", "exchange:None", None))
        self.statusLabels['sector'].setText(_translate("MainWindow", "sector:default", None))

    def __init__(self):
        self.stockData = None

    def layoutautoResizeEvent(self, event):
        """
        auto to set the width of the layouts == window.width,when the mainwindow resize
        :param event:
        """
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, event.size().width(), 61))
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, event.size().width() - 10, 431))
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 490, event.size().width(), 61))
        self.menubar.setGeometry(QtCore.QRect(0, 0, event.size().width(), 23))

    def _initMenuBar(self):
        self.menubar = QtGui.QMenuBar(self.window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.window.setMenuBar(self.menubar)

        startMenu = self.menubar.addMenu(_fromUtf8("开始"))
        # startMenu.hovered.connect(self.hoveredEvent)
        self.menuConnectAction = startMenu.addAction(_fromUtf8("连接数据库"))
        self.menuConnectAction.triggered.connect(self.menuConnectActionPress)
        self.menuDisconnectAction = startMenu.addAction(_fromUtf8("关闭数据库"))
        self.menuDisconnectAction.triggered.connect(self.menuDisconnectActionPress)
        self.menuDisconnectAction.setDisabled(True)
        self.menuSetUpAction = startMenu.addAction(_fromUtf8("设置"))
        self.menuSetUpAction.triggered.connect(self.setup)
        startMenu.addSeparator()
        self.exitAction = startMenu.addAction(_fromUtf8("退出"))
        self.exitAction.setShortcut('Escape')
        self.exitAction.triggered.connect(self.exit)

        marketMenu = self.menubar.addMenu(_fromUtf8("市场"))
        self.menuMarketSHAction = marketMenu.addAction(_fromUtf8("上交所"))
        self.menuMarketSHAction.setCheckable(True)
        self.menuMarketSHAction.setEnabled(False)
        self.menuMarketSHAction.triggered.connect(self.menuMarketSHActionPress)
        self.menuMarketSZAction = marketMenu.addAction(_fromUtf8("深交所"))
        self.menuMarketSZAction.setCheckable(True)
        self.menuMarketSZAction.setEnabled(False)
        self.menuMarketSZAction.triggered.connect(self.menuMarketSZActionPress)

        sectorMenu = self.menubar.addMenu(_fromUtf8("板块"))
        self.menuSectorMenuAction = sectorMenu.addAction(_fromUtf8("default"))
        # self.menuExchangeSHAction.triggered.connect(self.connectDB)
        self.menuSectorAction = sectorMenu.addAction(_fromUtf8("2"))
        # self.menuExchangeSZAction.triggered.connect(self.connectDB)

    def _initStatusBar(self):
        self.statusbar = QtGui.QStatusBar(self.window)
        self.statusbar.setObjectName(_fromUtf8("statusBar"))
        self.window.setStatusBar(self.statusbar)
        self.statusLabels = dict()
        self.statusLabels['ip'] = QtGui.QLabel(self.window)
        self.statusLabels['exchange'] = QtGui.QLabel(self.window)
        self.statusLabels['sector'] = QtGui.QLabel(self.window)
        self.statusLabels['status'] = QtGui.QLabel(self.window)
        self.statusProgressBar = QtGui.QProgressBar(self.window)
        self.statusProgressBar.setObjectName(_fromUtf8("statusProgressBar"))

        self.statusbar.addPermanentWidget(self.statusProgressBar, stretch=2)
        self.statusProgressBar.setMinimum(0)
        self.statusProgressBar.setVisible(False)
        self.statusbar.addPermanentWidget(self.statusLabels['status'], stretch=1)
        self.statusbar.addPermanentWidget(self.statusLabels['sector'], stretch=0)
        self.statusbar.addPermanentWidget(self.statusLabels['exchange'], stretch=0)
        self.statusbar.addPermanentWidget(self.statusLabels['ip'], stretch=0)

    def _initTableView(self):
        self.stockTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.stockTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.stockTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.window.connect(self.stockTable, QtCore.SIGNAL("itemClicked(QTableWidgetItem*)"),
                            self.stockTBItemClick)
        # self.connect(self.stockTBView, QtCore.SIGNAL("cellDoubleClicked (int,int)"), self.stockTBItemClick)
        self.window.connect(self.stockTable, QtCore.SIGNAL("itemDoubleClicked(QTableWidgetItem*)"),
                            self.stockTBItemDoubleClick)
        ##max columnCount==30
        self.stockTable.setColumnCount(17)
        self.stockTable.setRowCount(100)
        self.stockTable.setHorizontalHeaderLabels(['name', 'price_last', 'price_highest', 'date_origin', 'date_last',
                                                   'businessClassify', 'count', 'ACirculate', 'AStockCount',
                                                   'companyShortName', 'companyFullName', 'area', 'province', 'city', 'HP',
                                                   'regAddr', 'engName'])
        index = self.enumStockTableColumn('name')
        width = self.stockTable.columnWidth(index) - 20
        self.stockTable.setColumnWidth(index, width)
        index = self.enumStockTableColumn('price_last')
        width = self.stockTable.columnWidth(index) - 16
        self.stockTable.setColumnWidth(index, width)
        index = self.enumStockTableColumn('price_highest')
        width = self.stockTable.columnWidth(index) - 16
        self.stockTable.setColumnWidth(index, width)
        index = self.enumStockTableColumn('date_origin')
        width = self.stockTable.columnWidth(index) - 16
        self.stockTable.setColumnWidth(index, width)
        index = self.enumStockTableColumn('date_last')
        width = self.stockTable.columnWidth(index) - 16
        self.stockTable.setColumnWidth(index, width)

    def _initAnalysisWindow(self, father):
        Form = QtGui.QWidget()
        window = StocksAnalysisWindow.Ui_Form()
        window.setupUi(Form)
        window.setDelegate(father)
        return window

    def enumStockTableColumn(self, key):
        """
            get the column num by the name of column
            :param key:the name of column
            :return:is int,the column num
            """
        return {
            'name': 0, 'price_last': 1, 'price_highest': 2, 'date_origin': 3, 'date_last': 4,
            'businessClassify': 5, 'count': 6, 'ACirculate': 7, 'AStockCount': 8,
            'companyShortName': 9, 'companyFullName': 10, 'area': 11, 'province': 12, 'city': 13, 'HP': 14,
            'regAddr': 15, 'engName': 16
        }.get(key, __enumError__)

    def showStatusMessage(self, key, message):
        """
        According to the different key,to normalize message(translate to utf8),
        and display to different label
        :param key: the key of self.statusLabels
            :keys contain: status/sector/exchange/ip
        :param message:
        """

        def _rebuildStatusMessageContent(key, message):
            return {
                'status': message,
                'sector': self.statusLabels[key].text().split(':')[0] + ':' + message,
                'exchange': self.statusLabels[key].text().split(':')[0] + ':' + message,
                'ip': self.statusLabels[key].text().split(':')[0] + ':' + message
            }.get(key, None)

        try:
            finalMessage = _rebuildStatusMessageContent(key, message)
        except Exception, e:
            print 'showStatusMessage:error %s' % e
            self.statusLabels['status'].setText(_translate("MainWindow", 'showStatusMessage:error %s' % e, None))
        else:
            self.statusLabels[key].setText(_translate("MainWindow", finalMessage, None))

    def menuConnectActionPress(self):
        print 'connect press'
        self.stockData = self._connectDB()
        if self.stockData:
            self.showStatusMessage('status', 'connect db success')
            self.menuConnectAction.setDisabled(True)
            self.menuDisconnectAction.setEnabled(True)
            self.menuMarketSHAction.setEnabled(True)
            self.showStatusMessage('exchange', '上交所')
            self.menuMarketSHAction.setChecked(True)
            self.menuMarketSZAction.setEnabled(True)
            self.showStatusMessage('ip', self.stockData.getServerIP())
            self.updateStockTableProgress()
        else:
            self.showStatusMessage('status', 'connect db fails')

    def menuDisconnectActionPress(self):
        print 'disconnect press'
        self._disconnectDB()
        self.showStatusMessage('status', 'disconnectDB')
        self.menuConnectAction.setEnabled(True)
        self.menuDisconnectAction.setDisabled(True)
        self.showStatusMessage('exchange', "None")
        self.menuMarketSHAction.setEnabled(False)
        self.menuMarketSZAction.setEnabled(False)
        self.menuMarketSHAction.setChecked(False)
        self.menuMarketSZAction.setChecked(False)

    def menuMarketSHActionPress(self):
        if self.menuMarketSZAction.isChecked():
            self.menuMarketSZAction.setChecked(False)
            self.showStatusMessage('exchange', "上交所")
            self.stockData.changeStockExchange(StockData.ShangHaiStockDB)
            self.updateStockTableProgress()
        else:
            self.menuMarketSHAction.setChecked(True)
            return

    def menuMarketSZActionPress(self):
        if self.menuMarketSHAction.isChecked():
            self.menuMarketSHAction.setChecked(False)
            self.showStatusMessage('exchange', "深交所")
            self.stockData.changeStockExchange(StockData.ShenZhenStockDB)
            self.updateStockTableProgress()
        else:
            self.menuMarketSZAction.setChecked(True)
            return

    def stockTBItemClick(self, WidgetItem):
        code = self.stockTable.verticalHeaderItem(WidgetItem.row()).text().toUtf8().data()
        key = self.stockTable.horizontalHeaderItem(WidgetItem.column()).text().toUtf8().data()
        value = WidgetItem.text().toUtf8().data()
        self.showStatusMessage('status', 'selected: ' + 'code: ' + code + '  ' + key + ': ' + value)

    def stockTBItemDoubleClick(self, WidgetItem):
        code = self.stockTable.verticalHeaderItem(WidgetItem.row()).text().toUtf8().data()
        name = self.stockTable.item(WidgetItem.row(),
                                    self.enumStockTableColumn("name")).text().toUtf8().data()
        if not self.StockAnalysisWindow:
            self.StockAnalysisWindow = self._initAnalysisWindow(self)
            self.StockAnalysisWindow.show()
            self.StockAnalysisWindow.insertStock(code, name)
            self.StockAnalysisWindow.raise_()
        else:
            if self.StockAnalysisWindow.insertStock(code, name):
                self.StockAnalysisWindow.raise_()
            else:
                print '弹出警告筐'



    def _connectDB(self):
        stockData = StockData.StockDataClass(StockData.ShangHaiStockDB)
        if not stockData.isConnectSuccess():
            stockData = None
        return stockData

    def _disconnectDB(self):
        self.stockData = None

    def getStockInfos(self):
        return self.stockData.getStockInfo_dicORList()

    def getStockDayData(self, code, start=None, end=None):
        return self.stockData.loadStockDayDataByDate(code, start, end)

    def updateStockTableProgress(self):
        def _loadStockInfoAndUpdateStockTable(self):
            """
            Clear stockTable,then request data from db.
            This is an coroutine function.
            It would show and update progress progressBar in statusBar.
            Finally,hide the progressBar
            yield in mac don`t work like in windows
            """
            self.stockTable.clearContents()
            stockInfo_list = self.getStockInfos()
            rowCount = len(stockInfo_list)
            self.statusProgressBar.setMaximum(rowCount)
            self.statusProgressBar.setVisible(True)

            self.stockTable.setRowCount(rowCount)
            for index, stockInfo in enumerate(stockInfo_list):
                yield index  # self.statusProgressBar.setValue(index)
                for key, value in stockInfo.iteritems():
                    columnNum = self.enumStockTableColumn(key)
                    if columnNum == __enumError__:
                        if key == 'code':
                            self.stockTable.setVerticalHeaderItem(index, QtGui.QTableWidgetItem(value))
                        continue

                    if self.isNumber(value):
                        widgetItem = QtGui.QTableWidgetItem(repr(value))
                    else:
                        widgetItem = QtGui.QTableWidgetItem(value)
                    widgetItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.stockTable.setItem(index, columnNum, widgetItem)
            self.statusProgressBar.setVisible(False)
            self.showStatusMessage('status', self.stockData.curExchangeName + " data load completed")

        loader = _loadStockInfoAndUpdateStockTable(self)
        for index in loader:
            self.statusProgressBar.setValue(index)

    def hoveredEvent(self, ationx):
        if ationx == self.menuConnectAction:
            print 'hoveredEvent', ationx

        if ationx == self.menuDisconnectAction:
            print 'hoveredEvent', ationx

    def closeEvent(self, event):
        """
        Rewrite the widget.closeEvent
        """
        print 'main window close'
        if self.StockAnalysisWindow:
            self.StockAnalysisWindow.close()
            self.StockAnalysisWindow = None
        self.stockData = None

    def closeAnalysisWindowNotify(self):
        print 'closeAnalysisWindow notify'
        self.window.raise_()
        self.StockAnalysisWindow = None


    def setup(self):
        """
    application set up, ex.: DB ip
        """
        pass

    def exit(self):
        print 'main quit exit'
        self.window.emit(QtCore.SIGNAL('exit()'))

    def test(self):
        print 'test'
        self.lastDay = QtCore.QDateTime.fromString('1900-01-01', 'yyyy-MM-dd')
        print self.lastDay
        print self.lastDay.toString('yyyy-MM-dd')


        # t = threading.Thread(target=self.loadStockInfoAndUpdateStockTable)
        # t.daemon = False
        # t.start()

        # import httplib2
        # import socks
        # h = httplib2.Http(proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 1080))
        # r,c = h.request("http://table.finance.yahoo.com/table.csv?s=601318.ss")
        # print r
        # print c

    def isNumber(self, str):
        """
        str.isDigit() ：float will be deemed to be str.
        :param str: any str
        :return: true when the content of str is a number
        """
        try:
            str + 1
        except TypeError:
            return False
        else:
            return True


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QMainWindow()
    #Form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    window = StockMainWindow()
    window.setupUi(Form)
    Form.show()
    # in mac, cant get on top auto when app start,
    # add raise_() to solve that
    if sys.platform == 'darwin':
        Form.raise_()
    window.menuConnectActionPress()
    sys.exit(app.exec_())