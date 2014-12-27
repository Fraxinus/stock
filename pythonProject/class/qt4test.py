#coding=utf-8
#对话框
import sys
from PyQt4 import QtGui, QtCore, uic
import threading
import numpy

from matlabtest import DrawWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


# class Icon(QtGui.QWidget):
#     def __init__(self, parent = None):
#         QtGui.QWidget.__init__(self, parent)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Icon')
#         self.setWindowIcon(QtGui.QIcon('../icons/100.png'))
# app = QtGui.QApplication(sys.argv)
# icon = Icon()
# icon.show()
# sys.exit(app.exec_())

class MyDialog( QtGui.QDialog ):
    def __init__( self ):
        super( MyDialog, self ).__init__()
        uic.loadUi( "ui2.ui", self )

class Window( QtGui.QWidget ):
    def __init__( self ):
        super( Window, self ).__init__()
        self.setGeometry(300, 300, 1200, 700)
        self.setWindowTitle( "hello" )
        #图标
        icon = QtGui.QIcon()
        #图片
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/100.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        # self.resize( 500, 500 )

        #气泡
        self.setToolTip('This is a <b>QWidget</b> widget')
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))

        gridlayout = QtGui.QGridLayout()

        self.AboutButton = QtGui.QPushButton( "About" )
        gridlayout.addWidget( self.AboutButton, 0, 0 )
        self.AboutQtButton = QtGui.QPushButton( "AboutQt" )
        gridlayout.addWidget( self.AboutQtButton, 0, 1 )
        self.CriticalButton = QtGui.QPushButton( "CriticalButton" )
        gridlayout.addWidget( self.CriticalButton, 1, 0 )
        self.InfoButton = QtGui.QPushButton( "Info" )
        gridlayout.addWidget( self.InfoButton, 1, 1 )
        self.QuestionButton = QtGui.QPushButton( "Question" )
        gridlayout.addWidget( self.QuestionButton, 2, 0 )
        self.WarningButton = QtGui.QPushButton( "Warning" )
        gridlayout.addWidget( self.WarningButton, 2, 1 )

        lcd = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        # vbox = QtGui.QVBoxLayout()
        # vbox.setGeometry(QtCore.QRect(300, 300, 250, 150))
        # vbox.addWidget(lcd)
        # vbox.addWidget(slider)
        # self.setLayout(vbox)

        gridlayout.addWidget( lcd, 3, 0 )
        gridlayout.addWidget( slider, 3, 1 )

        slider.valueChanged.connect(lcd.display)

        self.AnimationButton = QtGui.QPushButton( "Anima" )
        gridlayout.addWidget( self.AnimationButton, 4, 0 )

        spacer = QtGui.QSpacerItem( 200, 80 )
        gridlayout.addItem( spacer, 3, 1, 1, 5 )

        gridlayout.addWidget(DrawWidget(), 5, 1)


        self.setLayout( gridlayout )

        self.connect( self.AboutButton, QtCore.SIGNAL( 'clicked()' ), self.OnAboutButton )
        self.connect( self.AboutQtButton, QtCore.SIGNAL( 'clicked()' ), self.OnAboutQtButton )
        self.connect( self.CriticalButton, QtCore.SIGNAL( 'clicked()' ), self.OnCriticalButton )
        self.connect( self.InfoButton, QtCore.SIGNAL( 'clicked()' ), self.OnInfoButton )
        self.connect( self.QuestionButton, QtCore.SIGNAL( 'clicked()' ), self.OnQuestionButton )
        self.connect( self.WarningButton, QtCore.SIGNAL( 'clicked()' ), self.OnWarningButton )
        self.AnimationButton.clicked.connect(self.OnAnimation)


    def OnAboutButton( self ):
        QtGui.QMessageBox.about( self, 'PyQt', "About" )

    def OnAboutQtButton( self ):
        QtGui.QMessageBox.aboutQt( self, "PyQt" )

    def OnCriticalButton( self ):
        r = QtGui.QMessageBox.critical( self, "PyQT", "CriticalButton", QtGui.QMessageBox.Abort,
                                   QtGui.QMessageBox.Retry, QtGui.QMessageBox.Ignore )
        if r == QtGui.QMessageBox.Abort:
            self.setWindowTitle( "Abort" )
        elif r == QtGui.QMessageBox.Retry:
            self.setWindowTitle( "Retry" )
        elif r == QtGui.QMessageBox.Ignore:
            self.setWindowTitle( "Ignore" )
        else:
            pass

    def OnInfoButton( self ):
        QtGui.QMessageBox.information( self, "Pyqt", "information" )

    def OnQuestionButton( self ):
        r = QtGui.QMessageBox.question( self, "PyQt", "Question", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No, QtGui.QMessageBox.Cancel )

    def OnWarningButton( self ):
        r = QtGui.QMessageBox.warning( self, "PyQT", "warning", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No )
        if r == QtGui.QMessageBox.Yes:
            print 'yyyyyys'

    def OnAnimation(self):
        print 'anima'
        animation = QtCore.QPropertyAnimation(self.AnimationButton,  "geometry")
        animation.setDuration(10000)
        animation.setLoopCount(10)
        animation.setStartValue(QtCore.QRect(200, 300, 50, 60))
        # animation.setKeyValueAt(0.5, QtCore.QRect(240, 240, 100, 30));
        animation.setEndValue(QtCore.QRect(100, 200, 20, 30))
        # animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        animation.start()

        dialog = MyDialog()
        r = dialog.exec_()
        print r
        if r:
            self.AnimationButton.setText( str(r) )

# numpy.test(1,1)
app = QtGui.QApplication( sys.argv )
win = Window()
win.show()
app.exec_()