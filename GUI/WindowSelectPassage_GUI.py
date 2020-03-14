# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowSelectPassage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_winSelectPassage(object):
    def setupUi(self, winSelectPassage):
        winSelectPassage.setObjectName("winSelectPassage")
        winSelectPassage.resize(800, 600)
        winSelectPassage.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtWidgets.QWidget(winSelectPassage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lstPassages = QtWidgets.QListWidget(self.centralwidget)
        self.lstPassages.setObjectName("lstPassages")
        self.gridLayout.addWidget(self.lstPassages, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAddToList = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddToList.setObjectName("btnAddToList")
        self.verticalLayout.addWidget(self.btnAddToList)
        self.btnDeleteFromList = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteFromList.setObjectName("btnDeleteFromList")
        self.verticalLayout.addWidget(self.btnDeleteFromList)
        self.btnCreateNewPasage = QtWidgets.QPushButton(self.centralwidget)
        self.btnCreateNewPasage.setObjectName("btnCreateNewPasage")
        self.verticalLayout.addWidget(self.btnCreateNewPasage)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.chkMode = QtWidgets.QCheckBox(self.centralwidget)
        self.chkMode.setChecked(False)
        self.chkMode.setObjectName("chkMode")
        self.verticalLayout.addWidget(self.chkMode)
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setObjectName("btnOk")
        self.verticalLayout.addWidget(self.btnOk)
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setObjectName("btnCancel")
        self.verticalLayout.addWidget(self.btnCancel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        winSelectPassage.setCentralWidget(self.centralwidget)
        self.actionNew_Student = QtWidgets.QAction(winSelectPassage)
        self.actionNew_Student.setObjectName("actionNew_Student")
        self.actionNew_Passage = QtWidgets.QAction(winSelectPassage)
        self.actionNew_Passage.setObjectName("actionNew_Passage")
        self.actionExit = QtWidgets.QAction(winSelectPassage)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(winSelectPassage)
        QtCore.QMetaObject.connectSlotsByName(winSelectPassage)

    def retranslateUi(self, winSelectPassage):
        _translate = QtCore.QCoreApplication.translate
        winSelectPassage.setWindowTitle(_translate("winSelectPassage", "Select Passages"))
        self.btnAddToList.setText(_translate("winSelectPassage", "Add To List"))
        self.btnDeleteFromList.setText(_translate("winSelectPassage", "Delete From List"))
        self.btnCreateNewPasage.setText(_translate("winSelectPassage", "Create New Passage"))
        self.chkMode.setText(_translate("winSelectPassage", "Separate Mode"))
        self.btnOk.setText(_translate("winSelectPassage", "OK"))
        self.btnCancel.setText(_translate("winSelectPassage", "Cancel"))
        self.actionNew_Student.setText(_translate("winSelectPassage", "New Student"))
        self.actionNew_Passage.setText(_translate("winSelectPassage", "New Passage"))
        self.actionExit.setText(_translate("winSelectPassage", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    winSelectPassage = QtWidgets.QMainWindow()
    ui = Ui_winSelectPassage()
    ui.setupUi(winSelectPassage)
    winSelectPassage.show()
    sys.exit(app.exec_())
