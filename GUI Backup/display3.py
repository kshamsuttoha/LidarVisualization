# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Khan\Desktop\Fall 2017\ENGPHYS PROJECT\PyQt\display3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(533, 852)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(96, 520, 131, 61))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(340, 520, 131, 61))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(19, 9, 500, 500))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 600, 500, 200))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_CSV = QtGui.QAction(MainWindow)
        self.actionSave_CSV.setObjectName(_fromUtf8("actionSave_CSV"))
        self.actionSave_STL = QtGui.QAction(MainWindow)
        self.actionSave_STL.setObjectName(_fromUtf8("actionSave_STL"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_CSV)
        self.menuFile.addAction(self.actionSave_STL)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LIDAR DISPLAY", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionSave_CSV.setText(_translate("MainWindow", "Save CSV", None))
        self.actionSave_STL.setText(_translate("MainWindow", "Save STL", None))

