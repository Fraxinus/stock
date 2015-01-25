#coding=utf-8

# Form implementation generated from reading ui file 'StockMainWindow.ui'
#
# Created: Sun Jan 25 16:21:02 2015
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(812, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 791, 431))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stockCView = QtGui.QColumnView(self.verticalLayoutWidget)
        self.stockCView.setObjectName(_fromUtf8("stockCView"))
        self.verticalLayout.addWidget(self.stockCView)
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
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 490, 811, 61))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.statusLabels = dict()
        self.statusLabels['ip'] = QtGui.QLabel(MainWindow)
        self.statusLabels['exchange'] = QtGui.QLabel(MainWindow)
        self.statusLabels['sector'] = QtGui.QLabel(MainWindow)
        self.statusLabels['status'] = QtGui.QLabel(MainWindow)

        # info = "  <font style='color: green;background: white;'>this is a test for change the fg & bg color ,text info</font>"
        # self.statueLabel.setText(info)
        self._initMenuBar()
        self._initStatusBar()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.centralwidget.resizeEvent = self.layoutautoResizeEvent

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.searchEdit.setPlaceholderText(_translate("MainWindow", "code or name", None))
        self.searchSubmitBtn.setText(_translate("MainWindow", "search", None))
        self.statusLabels['status'].setText(_translate("MainWindow", "status", None))
        self.statusLabels['ip'].setText(_translate("MainWindow", "ip:未连接", None))
        self.statusLabels['exchange'].setText(_translate("MainWindow", "exchange:None", None))
        self.statusLabels['sector'].setText(_translate("MainWindow", "sector:default", None))

    def layoutautoResizeEvent(self, event):
        """
        auto to set the width of the layouts == window.width,when the mainwindow resize
        :param event:
        """
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, event.size().width(), 61))
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, event.size().width()-10, 431))
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 490, event.size().width(), 61))
        self.menubar.setGeometry(QtCore.QRect(0, 0, event.size().width(), 23))

    def _initMenuBar(self):
        startMenu = self.menubar.addMenu(_fromUtf8("开始"))
        # startMenu.hovered.connect(self.hoveredEvent)
        self.menuConnectAction = startMenu.addAction(_fromUtf8("连接数据库"))
        self.menuConnectAction.triggered.connect(self.connectDB)
        self.menuDisconnectAction = startMenu.addAction(_fromUtf8("关闭数据库"))
        self.menuDisconnectAction.triggered.connect(self.disconnectDB)
        self.menuDisconnectAction.setDisabled(True)
        self.menuDisconnectAction = startMenu.addAction(_fromUtf8("设置"))
        self.menuDisconnectAction.triggered.connect(self.setup)
        startMenu.addSeparator()
        self.exitAction = startMenu.addAction(_fromUtf8( "退出"))
        self.exitAction.triggered.connect(self.exit)

        marketMenu = self.menubar.addMenu(_fromUtf8("市场"))
        self.menuMarketSHAction = marketMenu.addAction(_fromUtf8("上交所"))
        # self.menuExchangeSHAction.triggered.connect(self.connectDB)
        self.menuMarketSZAction = marketMenu.addAction(_fromUtf8("深交所"))
        # self.menuExchangeSZAction.triggered.connect(self.connectDB)

        sectorMenu = self.menubar.addMenu(_fromUtf8("板块"))
        self.menuSectorMenuAction = sectorMenu.addAction(_fromUtf8("default"))
        # self.menuExchangeSHAction.triggered.connect(self.connectDB)
        self.menuSectorAction = sectorMenu.addAction(_fromUtf8("2"))
        # self.menuExchangeSZAction.triggered.connect(self.connectDB)


    def _initStatusBar(self):
        self.statusbar.addPermanentWidget(self.statusLabels['status'], stretch=1)
        self.statusbar.addPermanentWidget(self.statusLabels['sector'], stretch=0)
        self.statusbar.addPermanentWidget(self.statusLabels['exchange'], stretch=0)
        self.statusbar.addPermanentWidget(self.statusLabels['ip'], stretch=0)

    def showStatusMessage(self, key, message):
        """
        According to the different key,to normalize message(translate to utf8),
        and display to different label
        :param key: the key of self.statusLabels
            :keys contain: status/sector/exchange/ip
        :param message:
        """
        def rebuildMessageContent(key, message):
            return {
                'status': message,
                'sector': self.statusLabels[key].text().split(':')[0]+':'+message,
                'exchange': self.statusLabels[key].text().split(':')[0]+':'+message,
                'ip': self.statusLabels[key].text().split(':')[0]+':'+message
                }.get(key, None)
        try:
            finalMessage = rebuildMessageContent(key, message)
        except Exception, e:
            print 'showStatusMessage:error %s' % e
            self.statusLabels['status'].setText(_translate("MainWindow", 'showStatusMessage:error %s' % e, None))
        else:
            self.statusLabels[key].setText(_translate("MainWindow", finalMessage, None))

    def connectDB(self):
        self.showStatusMessage('status', 'connect 2 db')
        print 'connect'
        self.menuConnectAction.setDisabled(True)
        self.menuDisconnectAction.setEnabled(True)

    def disconnectDB(self):
        self.showStatusMessage('status', 'disconnectDB')
        self.menuConnectAction.setEnabled(True)
        self.menuDisconnectAction.setDisabled(True)
        print 'disconnect'

    def hoveredEvent(self, ationx):
        if ationx == self.menuConnectAction:
            print 'hoveredEvent', ationx

        if ationx == self.menuDisconnectAction:
            print 'hoveredEvent', ationx

    def setup(self):
        """
    application set up, ex.: DB ip
        """
        pass

    def exit(self):
        self.window.close()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QMainWindow()
    window = Ui_MainWindow()
    window.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())