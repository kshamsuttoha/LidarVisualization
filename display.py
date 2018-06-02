# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display6.ui'
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
        MainWindow.resize(750, 750)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(120, -1, 120, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.horizontalLayout.addWidget(self.startButton)
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(150, -1, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.radioButton_slow = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_slow.setChecked(True)
        self.radioButton_slow.setObjectName(_fromUtf8("radioButton_slow"))
        self.buttonGroup = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radioButton_slow)
        self.horizontalLayout_2.addWidget(self.radioButton_slow)
        self.radioButton_medium = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_medium.setObjectName(_fromUtf8("radioButton_medium"))
        self.buttonGroup.addButton(self.radioButton_medium)
        self.horizontalLayout_2.addWidget(self.radioButton_medium)
        self.radioButton_fast = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_fast.setObjectName(_fromUtf8("radioButton_fast"))
        self.buttonGroup.addButton(self.radioButton_fast)
        self.horizontalLayout_2.addWidget(self.radioButton_fast)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
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
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_CSV)
        self.menuFile.addAction(self.actionSave_STL)
        self.menuFile.addAction(self.actionClear)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LIDAR DISPLAY", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.radioButton_slow.setText(_translate("MainWindow", "Slow", None))
        self.radioButton_medium.setText(_translate("MainWindow", "Medium", None))
        self.radioButton_fast.setText(_translate("MainWindow", "Fast", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionSave_CSV.setText(_translate("MainWindow", "Save CSV", None))
        self.actionSave_STL.setText(_translate("MainWindow", "Save STL", None))
        self.actionClear.setText(_translate("MainWindow", "Clear", None))

