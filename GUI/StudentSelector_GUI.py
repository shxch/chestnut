import os
from pathlib import Path

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog

studentsFolderPath = '../students/test/'


class Ui_studentSelector(object):
    def setupUi(self, studentSelector):
        studentSelector.setObjectName("studentSelector")
        studentSelector.resize(600, 400)
        studentSelector.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtWidgets.QWidget(studentSelector)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_addStudent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addStudent.setObjectName("pushButton_addStudent")
        self.verticalLayout.addWidget(self.pushButton_addStudent)
        self.pushButton_addPassage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addPassage.setObjectName("pushButton_addPassage")
        self.verticalLayout.addWidget(self.pushButton_addPassage)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_deleteStudent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deleteStudent.setObjectName("pushButton_deleteStudent")
        self.pushButton_deleteStudent.setDisabled(True)
        self.verticalLayout.addWidget(self.pushButton_deleteStudent)
        self.pushButton_deletePassage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deletePassage.setObjectName("pushButton_deletePassage")
        self.verticalLayout.addWidget(self.pushButton_deletePassage)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget_students = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_students.setObjectName("listWidget_students")
        self.verticalLayout_2.addWidget(self.listWidget_students)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        studentSelector.setCentralWidget(self.centralwidget)
        self.actionNew_Student = QtWidgets.QAction(studentSelector)
        self.actionNew_Student.setObjectName("actionNew_Student")
        self.actionNew_Passage = QtWidgets.QAction(studentSelector)
        self.actionNew_Passage.setObjectName("actionNew_Passage")
        self.actionExit = QtWidgets.QAction(studentSelector)
        self.actionExit.setObjectName("actionExit")

        self.refreshStudentsList()
        self.pushButton_addStudent.clicked.connect(self.saveNewStudent)
        self.pushButton_deleteStudent.clicked.connect(self.deleteStudent)
        self.listWidget_students.itemClicked.connect(self.enableDeleteButton)
        self.listWidget_students.itemDoubleClicked.connect(self.selectStudent)

        self.retranslateUi(studentSelector)
        QtCore.QMetaObject.connectSlotsByName(studentSelector)

    def retranslateUi(self, studentSelector):
        _translate = QtCore.QCoreApplication.translate
        studentSelector.setWindowTitle(_translate("studentSelector", "Select a Student"))
        self.pushButton_addStudent.setText(_translate("studentSelector", "Add Student"))
        self.pushButton_addPassage.setText(_translate("studentSelector", "Add Passage"))
        self.pushButton_deleteStudent.setText(_translate("studentSelector", "Delete Student"))
        self.pushButton_deletePassage.setText(_translate("studentSelector", "Delete Passage"))
        self.actionNew_Student.setText(_translate("studentSelector", "New Student"))
        self.actionNew_Passage.setText(_translate("studentSelector", "New Passage"))
        self.actionExit.setText(_translate("studentSelector", "Exit"))

    def refreshStudentsList(self):
        self.listWidget_students.clear()
        self.listWidget_students.addItems(os.listdir(studentsFolderPath))

    def saveNewStudent(self):
        newStudentName, ok = QInputDialog.getText(self.centralwidget, 'New Student', 'Enter New Student\'s Name')
        if ok == True:
            Path(studentsFolderPath + newStudentName).touch()
            self.refreshStudentsList()

    def deleteStudent(self):
        studentToBeDeleted = self.listWidget_students.currentItem().text()
        msgboxConfirm = QMessageBox()
        msgboxConfirm.setWindowTitle("Delete Confirmation")
        msgboxConfirm.setText("Delete this student's file?")
        msgboxConfirm.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        choice = msgboxConfirm.exec_()
        if choice == QMessageBox.Yes:
            os.remove(studentsFolderPath + studentToBeDeleted)
            self.refreshStudentsList()

    def enableDeleteButton(self):
        self.pushButton_deleteStudent.setEnabled(True)

    def selectStudent(self):
        studentSelected = self.listWidget_students.currentItem().text()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    studentSelector = QtWidgets.QMainWindow()
    ui = Ui_studentSelector()
    ui.setupUi(studentSelector)
    studentSelector.show()
    sys.exit(app.exec_())
