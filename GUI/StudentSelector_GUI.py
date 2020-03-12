import os
from pathlib import Path

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog

studentsFolderPath = '../students/test/'


class Ui_studentSelector(object):
    def __init__(self):
        studentSelector.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(studentSelector)
        self.btnAddStudent = QtWidgets.QPushButton(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.verticalLayout.addWidget(self.btnAddStudent)
        self.btnAddPassage = QtWidgets.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.btnAddPassage)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnDeleteStudent = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteStudent.setDisabled(True)
        self.verticalLayout.addWidget(self.btnDeleteStudent)
        self.btnDeletePassage = QtWidgets.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.btnDeletePassage)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.listStudents = QtWidgets.QListWidget(self.centralwidget)
        self.verticalLayout_2.addWidget(self.listStudents)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        studentSelector.setCentralWidget(self.centralwidget)

        self.retranslateUi(studentSelector)

        self.refreshStudentsList()
        self.btnAddStudent.clicked.connect(self.saveNewStudent)
        self.btnDeleteStudent.clicked.connect(self.deleteStudent)
        self.listStudents.itemClicked.connect(self.enableDeleteButton)
        self.listStudents.itemDoubleClicked.connect(self.selectStudent)

        QtCore.QMetaObject.connectSlotsByName(studentSelector)

    def retranslateUi(self, studentSelector):
        _translate = QtCore.QCoreApplication.translate
        studentSelector.setWindowTitle(_translate("studentSelector", "Select a Student"))
        self.btnAddStudent.setText(_translate("studentSelector", "Add Student"))
        self.btnAddPassage.setText(_translate("studentSelector", "Add Passage"))
        self.btnDeleteStudent.setText(_translate("studentSelector", "Delete Student"))
        self.btnDeletePassage.setText(_translate("studentSelector", "Delete Passage"))

    def refreshStudentsList(self):
        self.listStudents.clear()
        self.listStudents.addItems(os.listdir(studentsFolderPath))

    def saveNewStudent(self):
        newStudentName, ok = QInputDialog.getText(self.centralwidget, 'New Student', 'Enter New Student\'s Name')
        if ok == True:
            Path(studentsFolderPath + newStudentName).touch()
            self.refreshStudentsList()

    def deleteStudent(self):
        studentToBeDeleted = self.listStudents.currentItem().text()
        msgboxConfirm = QMessageBox()
        msgboxConfirm.setWindowTitle("Delete Confirmation")
        msgboxConfirm.setText("Are you sure you want to delete this student's file?")
        msgboxConfirm.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        choice = msgboxConfirm.exec_()
        if choice == QMessageBox.Yes:
            os.remove(studentsFolderPath + studentToBeDeleted)
            self.refreshStudentsList()

    def enableDeleteButton(self):
        self.btnDeleteStudent.setEnabled(True)

    def selectStudent(self):
        studentSelected = self.listStudents.currentItem().text()
        print(studentSelected)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    studentSelector = QtWidgets.QMainWindow()
    ui = Ui_studentSelector()
    studentSelector.show()
    sys.exit(app.exec_())
