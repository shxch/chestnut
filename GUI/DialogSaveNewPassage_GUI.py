# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogSaveNewPassage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_dlgSaveNewPassage(object):
    def setupUi(self, dlgSaveNewPassage):
        dlgSaveNewPassage.setObjectName("dlgSaveNewPassage")
        dlgSaveNewPassage.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(dlgSaveNewPassage)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(dlgSaveNewPassage)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlgSaveNewPassage)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)

        self.retranslateUi(dlgSaveNewPassage)
        self.buttonBox.rejected.connect(dlgSaveNewPassage.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgSaveNewPassage)

    def retranslateUi(self, dlgSaveNewPassage):
        _translate = QtCore.QCoreApplication.translate
        dlgSaveNewPassage.setWindowTitle(_translate("dlgSaveNewPassage", "Type In New Passage"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dlgSaveNewPassage = QtWidgets.QDialog()
    ui = Ui_dlgSaveNewPassage()
    ui.setupUi(dlgSaveNewPassage)
    dlgSaveNewPassage.show()
    sys.exit(app.exec_())
