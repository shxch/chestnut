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
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAddStudent = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddStudent.setObjectName("btnAddStudent")
        self.verticalLayout.addWidget(self.btnAddStudent)
        self.btnEditStudent = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditStudent.setObjectName("btnEditStudent")
        self.verticalLayout.addWidget(self.btnEditStudent)
        self.btnAddPassage = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddPassage.setObjectName("btnAddPassage")
        self.verticalLayout.addWidget(self.btnAddPassage)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnDeleteStudent = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteStudent.setObjectName("btnDeleteStudent")
        self.verticalLayout.addWidget(self.btnDeleteStudent)
        self.btnDeletePassage = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeletePassage.setObjectName("btnDeletePassage")
        self.verticalLayout.addWidget(self.btnDeletePassage)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lstStudents = QtWidgets.QListWidget(self.centralwidget)
        self.lstStudents.setObjectName("lstStudents")
        self.verticalLayout_2.addWidget(self.lstStudents)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        winSelectStudent.setCentralWidget(self.centralwidget)
        self.actionNew_Student = QtWidgets.QAction(winSelectStudent)
        self.actionNew_Student.setObjectName("actionNew_Student")
        self.actionNew_Passage = QtWidgets.QAction(winSelectStudent)
        self.actionNew_Passage.setObjectName("actionNew_Passage")
        self.actionExit = QtWidgets.QAction(winSelectStudent)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(winSelectStudent)
        QtCore.QMetaObject.connectSlotsByName(winSelectStudent)

    def retranslateUi(self, winSelectStudent):
        _translate = QtCore.QCoreApplication.translate
        winSelectStudent.setWindowTitle(_translate("winSelectStudent", "Select a Student"))
        self.btnAddStudent.setText(_translate("winSelectStudent", "Add Student"))
        self.btnEditStudent.setText(_translate("winSelectStudent", "Edit Student"))
        self.btnAddPassage.setText(_translate("winSelectStudent", "Add Passage"))
        self.btnDeleteStudent.setText(_translate("winSelectStudent", "Delete Student"))
        self.btnDeletePassage.setText(_translate("winSelectStudent", "Delete Passage"))
        self.actionNew_Student.setText(_translate("winSelectStudent", "New Student"))
        self.actionNew_Passage.setText(_translate("winSelectStudent", "New Passage"))
        self.actionExit.setText(_translate("winSelectStudent", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    winSelectStudent = QtWidgets.QMainWindow()
    ui = Ui_winSelectStudent()
    ui.setupUi(winSelectStudent)
    winSelectStudent.show()
    sys.exit(app.exec_())
