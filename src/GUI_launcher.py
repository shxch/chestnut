import os
import sys
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QFileDialog
from sortedcontainers import SortedSet

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
        self.updateStudentsList()
        self.btnAddStudent.clicked.connect(self.addNewStudent)
        self.btnAddPassage.clicked.connect(self.openSaveNewPassageDialog)
        self.btnDeleteStudent.clicked.connect(self.deleteStudent)
        self.btnDeletePassage.clicked.connect(self.deletePassage)
        self.btnEditStudent.clicked.connect(self.editStudent)
        self.lstStudents.itemDoubleClicked.connect(self.openSelectPassageWindow)

    def updateStudentsList(self):
        self.lstStudents.clear()
        self.lstStudents.addItems(os.listdir(studentsFolderPath))

    def addNewStudent(self):
        # noinspection PyArgumentList
        newStudentName, ok = QInputDialog.getText(None, 'New Student', 'Enter New Student\'s Name')
        if ok:
            Path(studentsFolderPath + newStudentName).touch()
            self.updateStudentsList()

    def editStudent(self):
        if self.lstStudents.currentItem() is not None:
            studentToBeEdited = self.lstStudents.currentItem().text()
            # noinspection PyArgumentList
            newName, ok = QInputDialog.getText(None, 'New Name', 'Enter New Name')
            if ok and newName:
                os.rename(studentsFolderPath + studentToBeEdited, studentsFolderPath + newName)
                self.updateStudentsList()

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
                self.updateStudentsList()

    @staticmethod
    def deletePassage():
        # noinspection PyArgumentList
        fileToBeDeleted, _ = QFileDialog.getOpenFileName(None, 'Delete File', passagesFolderPath)
        if fileToBeDeleted:
            os.remove(fileToBeDeleted)

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
        fileName, _ = QFileDialog.getSaveFileName(None, 'Save File', passagesFolderPath, '*.txt')
        if fileName:
            with open(fileName, 'w') as file:
                file.write(toBeSavedText)
            self.plainTextEdit.clear()
            dlgSaveNewPassage.close()


class WindowSelectPassage(QtWidgets.QMainWindow, Ui_winSelectPassage):
    addedPassages = SortedSet()

    # noinspection PyArgumentList
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnCancel.clicked.connect(self.cancel)
        self.btnAddToList.clicked.connect(self.addPassagesToList)
        self.btnDeleteFromList.clicked.connect(self.deletePassagesFromList)
        self.btnCreateNewPasage.clicked.connect(self.openSaveNewPassageDialog)

    def cancel(self):
        self.addedPassages.clear()
        self.lstPassages.clear()
        self.close()
        winSelectStudent.show()

    def updatePassagesList(self):
        self.lstPassages.clear()
        for passage in self.addedPassages:
            self.lstPassages.addItem(Path(passage).name)

    def addPassagesToList(self):
        # noinspection PyArgumentList
        passagesToBeAdded, _ = QFileDialog.getOpenFileNames(None, 'Add Passage', passagesFolderPath)
        if passagesToBeAdded:
            self.addedPassages.update(passagesToBeAdded)
            self.updatePassagesList()

    def deletePassagesFromList(self):
        passageIndexes = self.lstPassages.selectedIndexes()
        passageToBeDeleted = []
        for index in passageIndexes:
            passageToBeDeleted.append(self.addedPassages.__getitem__(index.row()))
        for passage in passageToBeDeleted:
            self.addedPassages.remove(passage)
        self.updatePassagesList()

    @staticmethod
    def openSaveNewPassageDialog():
        dlgSaveNewPassage.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    winSelectStudent = WindowSelectStudent()
    dlgSaveNewPassage = DialogSaveNewPassage()
    winSelectPassage = WindowSelectPassage()

    winSelectStudent.show()
    sys.exit(app.exec_())
