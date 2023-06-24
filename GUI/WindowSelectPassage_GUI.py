# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowSelectPassage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt6 import QtCore, QtWidgets


class Ui_winSelectPassage(object):
    def setupUi(self, winSelectPassage):
        winSelectPassage.setObjectName("winSelectPassage")
        winSelectPassage.resize(800, 600)
        winSelectPassage.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.centralwidget = QtWidgets.QWidget(winSelectPassage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lstPassages = QtWidgets.QListWidget(self.centralwidget)
        self.lstPassages.setAlternatingRowColors(True)
        self.lstPassages.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.lstPassages.setProperty("isWrapping", False)
        self.lstPassages.setWordWrap(True)
        self.lstPassages.setObjectName("lstPassages")
        self.gridLayout.addWidget(self.lstPassages, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnRemove = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemove.setObjectName("btnRemove")
        self.verticalLayout.addWidget(self.btnRemove)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.chkOutputMode = QtWidgets.QCheckBox(self.centralwidget)
        self.chkOutputMode.setChecked(False)
        self.chkOutputMode.setObjectName("chkOutputMode")
        self.verticalLayout.addWidget(self.chkOutputMode)
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setObjectName("btnOk")
        self.verticalLayout.addWidget(self.btnOk)
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setObjectName("btnCancel")
        self.verticalLayout.addWidget(self.btnCancel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        winSelectPassage.setCentralWidget(self.centralwidget)

        self.retranslateUi(winSelectPassage)
        QtCore.QMetaObject.connectSlotsByName(winSelectPassage)

    def retranslateUi(self, winSelectPassage):
        _translate = QtCore.QCoreApplication.translate
        winSelectPassage.setWindowTitle(_translate("winSelectPassage", "Select Passages"))
        self.lstPassages.setSortingEnabled(False)
        self.btnAdd.setText(_translate("winSelectPassage", "Add"))
        self.btnRemove.setText(_translate("winSelectPassage", "Remove"))
        self.chkOutputMode.setText(_translate("winSelectPassage", "Separate Mode"))
        self.btnOk.setText(_translate("winSelectPassage", "OK"))
        self.btnCancel.setText(_translate("winSelectPassage", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    winSelectPassage = QtWidgets.QMainWindow()
    ui = Ui_winSelectPassage()
    ui.setupUi(winSelectPassage)
    winSelectPassage.show()
    sys.exit(app.exec())
