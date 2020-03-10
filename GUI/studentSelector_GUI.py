import os

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic.properties import QtGui


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
        self.buttonAddStudent = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAddStudent.setObjectName("buttonAddStudent")
        self.verticalLayout.addWidget(self.buttonAddStudent)
        self.buttonAddPassage = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAddPassage.setObjectName("buttonAddPassage")
        self.verticalLayout.addWidget(self.buttonAddPassage)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonDeleteStudent = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDeleteStudent.setObjectName("buttonDeleteStudent")
        self.buttonDeleteStudent.setDisabled(True)
        self.verticalLayout.addWidget(self.buttonDeleteStudent)
        self.buttonDeletePassage = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDeletePassage.setObjectName("buttonDeletePassage")
        self.verticalLayout.addWidget(self.buttonDeletePassage)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listStudents = QtWidgets.QListWidget(self.centralwidget)
        self.listStudents.setObjectName("listStudents")
        self.verticalLayout_2.addWidget(self.listStudents)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        studentSelector.setCentralWidget(self.centralwidget)
        self.actionNew_Student = QtWidgets.QAction(studentSelector)
        self.actionNew_Student.setObjectName("actionNew_Student")
        self.actionNew_Passage = QtWidgets.QAction(studentSelector)
        self.actionNew_Passage.setObjectName("actionNew_Passage")
        self.actionExit = QtWidgets.QAction(studentSelector)
        self.actionExit.setObjectName("actionExit")

        self.refreshStudentsList()
        self.buttonAddStudent.clicked.connect(self.saveNewStudent)
        self.buttonDeleteStudent.clicked.connect(self.showDeleteStudentDialog)
        self.listStudents.itemClicked.connect(self.enableDeleteButton)

        self.retranslateUi(studentSelector)
        QtCore.QMetaObject.connectSlotsByName(studentSelector)

    def retranslateUi(self, studentSelector):
        _translate = QtCore.QCoreApplication.translate
        studentSelector.setWindowTitle(_translate("studentSelector", "Select a Student"))
        self.buttonAddStudent.setText(_translate("studentSelector", "Add Student"))
        self.buttonAddPassage.setText(_translate("studentSelector", "Add Passage"))
        self.buttonDeleteStudent.setText(_translate("studentSelector", "Delete Student"))
        self.buttonDeletePassage.setText(_translate("studentSelector", "Delete Passage"))
        self.actionNew_Student.setText(_translate("studentSelector", "New Student"))
        self.actionNew_Passage.setText(_translate("studentSelector", "New Passage"))
        self.actionExit.setText(_translate("studentSelector", "Exit"))

    def refreshStudentsList(self):
        self.listStudents.clear()
        self.listStudents.addItems(os.listdir('../students/test'))

    def saveNewStudent(self):
        # newStudentName, ok = QInputDialog.getText(self.centralwidget, 'New Student', 'Enter New Student\'s Name')
        # if ok == True:
        #     # debug
        #     print(newStudentName)
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        file.close()
        self.refreshStudentsList()

    def showDeleteStudentDialog(self):
        msgboxConfirm = QMessageBox()
        msgboxConfirm.setWindowTitle("Delete Confirmation")
        msgboxConfirm.setText("Delete this student's file?")
        msgboxConfirm.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        choice = msgboxConfirm.exec_()
        if choice == QMessageBox.Yes:
            # debug
            print("Yes")

    def enableDeleteButton(self):
        self.buttonDeleteStudent.setEnabled(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    studentSelector = QtWidgets.QMainWindow()
    ui = Ui_studentSelector()
    ui.setupUi(studentSelector)
    studentSelector.show()
    sys.exit(app.exec_())
