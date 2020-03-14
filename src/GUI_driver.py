import os
import sys
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QFileDialog

from GUI.DialogSaveNewPassage_GUI import Ui_dlgSaveNewPassage
from GUI.WindowSelectPassage_GUI import Ui_winSelectPassage
from GUI.WindowSelectStudent_GUI import Ui_winSelectStudent

studentsFolderPath = '../students/test/'
passagesFolderPath = '../materials/test/'


class WindowSelectStudent(QtWidgets.QMainWindow, Ui_winSelectStudent):
    def __init__(self, parent=None):
        # noinspection PyArgumentList
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.refreshStudentsList()
        self.btnAddStudent.clicked.connect(self.addNewStudent)
        self.btnAddPassage.clicked.connect(self.openSaveNewPassageDialog)
        self.btnDeleteStudent.clicked.connect(self.deleteStudent)
        self.btnDeletePassage.clicked.connect(self.deletePassage)
        self.btnEditStudent.clicked.connect(self.editStudent)
        self.lstStudents.itemDoubleClicked.connect(self.openSelectPassageWindow)

    def refreshStudentsList(self):
        self.lstStudents.clear()
        self.lstStudents.addItems(os.listdir(studentsFolderPath))

    def addNewStudent(self):
        # noinspection PyArgumentList
        newStudentName, ok = QInputDialog.getText(None, 'New Student', 'Enter New Student\'s Name')
        if ok:
            Path(studentsFolderPath + newStudentName).touch()
            self.refreshStudentsList()

    def editStudent(self):
        if self.lstStudents.currentItem() is not None:
            studentToBeEdited = self.lstStudents.currentItem().text()
            # noinspection PyArgumentList
            newName, ok = QInputDialog.getText(None, 'New Name', 'Enter New Name')
            if ok and len(newName) > 0:
                os.rename(studentsFolderPath + studentToBeEdited, studentsFolderPath + newName)
                self.refreshStudentsList()

    def deleteStudent(self):
        if self.lstStudents.currentItem() is not None:
            studentToBeDeleted = self.lstStudents.currentItem().text()
            msgboxConfirm = QMessageBox()
            msgboxConfirm.setWindowTitle("Delete Confirmation")
            msgboxConfirm.setText("Are you sure you want to delete this student's file?")
            msgboxConfirm.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

            choice = msgboxConfirm.exec()
            if choice == QMessageBox.Yes:
                os.remove(studentsFolderPath + studentToBeDeleted)
                self.refreshStudentsList()

    @staticmethod
    def deletePassage():
        # noinspection PyArgumentList
        fileToBeDeleted = QFileDialog.getOpenFileName(None, 'Delete File', passagesFolderPath, '*.txt')
        if len(fileToBeDeleted[0]) > 0:
            os.remove(fileToBeDeleted[0])

    def openSelectPassageWindow(self):
        studentSelected = self.lstStudents.currentItem().text()
        winSelectPassage.show()
        winSelectPassage.setWindowTitle(studentSelected + ' - Select Passages')
        winSelectStudent.close()

    @staticmethod
    def openSaveNewPassageDialog():
        dlgSaveNewPassage.exec()


class DialogSaveNewPassage(QtWidgets.QDialog, Ui_dlgSaveNewPassage):
    # noinspection PyArgumentList
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.savePassage)

    def savePassage(self):
        toBeSavedText = self.plainTextEdit.toPlainText()
        # noinspection PyArgumentList
        fileName = QFileDialog.getSaveFileName(None, 'Save File', passagesFolderPath, '*.txt')
        if len(fileName[0]) > 0:
            with open(fileName[0], 'w') as file:
                file.write(toBeSavedText)
            self.plainTextEdit.clear()
            dlgSaveNewPassage.close()


class WindowSelectPassage(QtWidgets.QMainWindow, Ui_winSelectPassage):
    # noinspection PyArgumentList
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnCancel.clicked.connect(self.cancel)

    def cancel(self):
        self.update()
        self.close()
        winSelectStudent.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    winSelectStudent = WindowSelectStudent()
    dlgSaveNewPassage = DialogSaveNewPassage()
    winSelectPassage = WindowSelectPassage()

    winSelectStudent.show()
    sys.exit(app.exec_())
