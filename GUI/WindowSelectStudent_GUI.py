# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowSelectStudent.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_winSelectStudent(object):
    def setupUi(self, winSelectStudent):
        winSelectStudent.setObjectName("winSelectStudent")
        winSelectStudent.resize(600, 400)
        winSelectStudent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtWidgets.QWidget(winSelectStudent)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lstStudents = QtWidgets.QListWidget(self.centralwidget)
        self.lstStudents.setAlternatingRowColors(True)
        self.lstStudents.setObjectName("lstStudents")
        self.verticalLayout_2.addWidget(self.lstStudents)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnNewStudent = QtWidgets.QPushButton(self.centralwidget)
        self.btnNewStudent.setObjectName("btnNewStudent")
        self.verticalLayout.addWidget(self.btnNewStudent)
        self.btnRename = QtWidgets.QPushButton(self.centralwidget)
        self.btnRename.setObjectName("btnRename")
        self.verticalLayout.addWidget(self.btnRename)
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setObjectName("btnDelete")
        self.verticalLayout.addWidget(self.btnDelete)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setObjectName("btnNext")
        self.verticalLayout.addWidget(self.btnNext)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        winSelectStudent.setCentralWidget(self.centralwidget)

        self.retranslateUi(winSelectStudent)
        QtCore.QMetaObject.connectSlotsByName(winSelectStudent)

    def retranslateUi(self, winSelectStudent):
        _translate = QtCore.QCoreApplication.translate
        winSelectStudent.setWindowTitle(_translate("winSelectStudent", "Select a Student"))
        self.lstStudents.setSortingEnabled(False)
        self.btnNewStudent.setText(_translate("winSelectStudent", "New Student"))
        self.btnRename.setText(_translate("winSelectStudent", "Rename"))
        self.btnDelete.setText(_translate("winSelectStudent", "Delete"))
        self.btnNext.setText(_translate("winSelectStudent", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    winSelectStudent = QtWidgets.QMainWindow()
    ui = Ui_winSelectStudent()
    ui.setupUi(winSelectStudent)
    winSelectStudent.show()
    sys.exit(app.exec_())
