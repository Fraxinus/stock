# -*- coding: utf-8 -*-

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

#设置控件文字编码
QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))


class Dialog1(QtGui.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.form = Dialog
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.dialog1_pushButton = QtGui.QPushButton(Dialog)
        self.dialog1_pushButton.setGeometry(QtCore.QRect(260, 15, 75, 23))
        self.dialog1_pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #信号连接到指定槽
        self.dialog1_pushButton.clicked.connect(self.on_dialog1_pushButton_clicked)

        self.table = QtGui.QTableWidget(Dialog)
        # self.connect(self.table, QtCore.SIGNAL("itemClicked (QTableWidgetItem*)"), self.outSelect)
        self.connect(self.table, QtCore.SIGNAL("cellDoubleClicked (int,int)"), self.outSelect2)
        self.connect(self.table, QtCore.SIGNAL("itemDoubleClicked (QTableWidgetItem*)"), self.outSelect)  #未加入内容的不响应改时间


        self.table.setColumnCount(5)
        self.table.setRowCount(100)
        self.table.setItem(0,0,QtGui.QTableWidgetItem(self.table.tr("性别")))
        self.table.setItem(0,1,QtGui.QTableWidgetItem(self.table.tr("姓名")))
        self.table.setItem(0,2,QtGui.QTableWidgetItem(self.table.tr("出生日期")))
        self.table.setItem(0,3,QtGui.QTableWidgetItem(self.table.tr("职业")))
        self.table.setItem(0,4,QtGui.QTableWidgetItem(self.table.tr("收入")))
        self.table.setGeometry(QtCore.QRect(10, 40, 380, 200))
        self.dialog1_pushButton.setObjectName(_fromUtf8("ttttttt"))

        #self.table.verticalHeader().setVisible(False)  # 去除垂直标尺
        self.table.horizontalHeader().setVisible(False)  # 去除水平标尺

        # for x in range(self.table.columnCount()):
        #     headItem = self.table.horizontalHeaderItem(x)   #获得水平方向表头的Item对象
        #     headItem.setFont(QtGui.QFont("song", 12, QtGui.QFont.Bold) )                        #设置字体
        #     headItem.setBackgroundColor(QtGui.QColor(0,60,10))      #设置单元格背景颜色
        #     headItem.setTextColor(QtGui.QColor(200,111,30))

        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
                #设置为可以选中多个目标该函数的参数还可以是：
                # QAbstractItemView.NoSelection      不能选择
                # QAbstractItemView.SingleSelection  选中单个目标
                # QAbstractItemView.MultiSelection    选中多个目标
                # QAbstractItemView.ExtendedSelection   QAbstractItemView.ContiguousSelection 的区别不明显，主要功能是正常情况下是单选，但按下Ctrl或Shift键后，可以多选

         #整行选择
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        # QAbstractItemView.SelectItems 	0 	Selecting single items.选中单个单元格
        # QAbstractItemView.SelectRows 	1 	Selecting only rows.选中一行
        # QAbstractItemView.SelectColumns 	2 	Selecting only columns.选中一列

        #禁止修改
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        # QAbstractItemView.NoEditTriggers 	0 	No editing possible. 不能对表格内容进行修改
        # QAbstractItemView.CurrentChanged 	1 	Editing start whenever current item changes.任何时候都能对单元格修改
        # QAbstractItemView.DoubleClicked 	2 	Editing starts when an item is double clicked.双击单元格
        # QAbstractItemView.SelectedClicked 	4 	Editing starts when clicking on an already selected item.单击已选中的内容
        # QAbstractItemView.EditKeyPressed 	8 	Editing starts when the platform edit key has been pressed over an item.
        # QAbstractItemView.AnyKeyPressed 	16 	Editing starts when any key is pressed over an item.按下任意键就能修改
        # QAbstractItemView.AllEditTriggers 	31 	Editing starts for all above actions.以上条件全包括


        # newItem.setTextAlignment() # 设定对齐
        # 水平对齐方式有：
        # Constant 	Value 	Description
        # Qt.AlignLeft 	0x0001 	Aligns with the left edge.
        # Qt.AlignRight 	0x0002 	Aligns with the right edge.
        # Qt.AlignHCenter 	0x0004 	Centers horizontally in the available space.
        # Qt.AlignJustify 	0x0008 	Justifies the text in the available space.
        #
        # 垂直对齐方式：
        # Constant 	Value 	Description
        # Qt.AlignTop 	0x0020 	Aligns with the top.
        # Qt.AlignBottom 	0x0040 	Aligns with the bottom.
        # Qt.AlignVCenter 	0x0080 	Centers vertically in the available space.

        # self.MyTable.setSpan(0, 0, 3, 1)  #合并 单元格   其参数为： 要改变单元格的   1行数  2列数     要合并的  3行数  4列数
        # self.MyTable.setColumnWidth(2,50)  #将第2列的单元格，设置成50宽度
        # self.MyTable.setRowHeight(2,60)      #将第2行的单元格，设置成60的高度

#          6.获得单击单元格的内容
# 通过实现 itemClicked (QTableWidgetItem *) 信号的槽函数，就可以获得鼠标单击到的单元格指针，进而获得其中的文字信息
# 首先在__init()__函数中加入
# self.connect(self.MyTable, SIGNAL("itemClicked (QTableWidgetItem*)"), self.outSelect)  #将itemClicked信号与函数outSelect绑定
# 然后实现一个outSelect函数，如下：
#     def outSelect(self, Item=None):
#         if Item == None:
#             return
#         print(Item.text())
# 运行程序后，单击一个单元格，即可获得其中的字符了

        lbp1=QtGui.QLabel()
        lbp1.setPixmap(QtGui.QPixmap("image/4.gif"))
        self.table.setCellWidget(1,0,lbp1)
        twi1=QtGui.QTableWidgetItem("Tom")
        self.table.setItem(1,1,twi1)
        dte1=QtGui.QDateTimeEdit()
        dte1.setDateTime(QtCore.QDateTime.currentDateTime())
        dte1.setDisplayFormat("yyyy/mm/dd")
        dte1.setCalendarPopup(True)
        self.table.setCellWidget(1,2,dte1)
        cbw=QtGui.QComboBox()
        cbw.addItem("Worker")
        cbw.addItem("Famer")
        cbw.addItem("Doctor")
        cbw.addItem("Lawyer")
        cbw.addItem("Soldier")
        self.table.setCellWidget(1,3,cbw)
        sb1=QtGui.QSpinBox()
        sb1.setRange(1000,10000)
        self.table.setCellWidget(1,4,sb1)

        self.table.setItem(2,0,QtGui.QTableWidgetItem("a"))
        self.table.setItem(3,0,QtGui.QTableWidgetItem("b"))
        self.table.setItem(4,0,QtGui.QTableWidgetItem("c"))


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "dialog1", None))
        self.dialog1_pushButton.setText(_translate("Dialog", "返回主窗体", None))

    def on_dialog1_pushButton_clicked(self):
        self.form.close()

    def outSelect(self, Item=None):
        if Item == None:
            return
        print 'itemclick', Item.text()
        print 'itemclick', Item.column()

    def outSelect2(self, x, y):
        print 'x', x
        print 'y', y
        item = self.table.item(x, 0)
        if item:
            print item.text()
        else:
            print 'null'

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())