# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sun Feb 23 01:31:54 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Wheel(object):
    def setupUi(self, Wheel):
        Wheel.setObjectName("Wheel")
        Wheel.resize(289, 323)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Wheel)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.display_label = QtGui.QLabel(Wheel)
        self.display_label.setObjectName("display_label")
        self.verticalLayout_2.addWidget(self.display_label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.upB = QtGui.QPushButton(Wheel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upB.sizePolicy().hasHeightForWidth())
        self.upB.setSizePolicy(sizePolicy)
        self.upB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.upB.setObjectName("upB")
        self.horizontalLayout.addWidget(self.upB)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftB = QtGui.QPushButton(Wheel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftB.sizePolicy().hasHeightForWidth())
        self.leftB.setSizePolicy(sizePolicy)
        self.leftB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.leftB.setObjectName("leftB")
        self.horizontalLayout_2.addWidget(self.leftB)
        self.downB = QtGui.QPushButton(Wheel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downB.sizePolicy().hasHeightForWidth())
        self.downB.setSizePolicy(sizePolicy)
        self.downB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.downB.setObjectName("downB")
        self.horizontalLayout_2.addWidget(self.downB)
        self.rightB = QtGui.QPushButton(Wheel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightB.sizePolicy().hasHeightForWidth())
        self.rightB.setSizePolicy(sizePolicy)
        self.rightB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rightB.setObjectName("rightB")
        self.horizontalLayout_2.addWidget(self.rightB)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Wheel)
        QtCore.QMetaObject.connectSlotsByName(Wheel)

    def retranslateUi(self, Wheel):
        Wheel.setWindowTitle(QtGui.QApplication.translate("Wheel", "gr-remotecar control for HackRF", None, QtGui.QApplication.UnicodeUTF8))
        self.display_label.setText(QtGui.QApplication.translate("Wheel", "Command:", None, QtGui.QApplication.UnicodeUTF8))
        self.upB.setText(QtGui.QApplication.translate("Wheel", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.leftB.setText(QtGui.QApplication.translate("Wheel", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.downB.setText(QtGui.QApplication.translate("Wheel", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.rightB.setText(QtGui.QApplication.translate("Wheel", "Right", None, QtGui.QApplication.UnicodeUTF8))

