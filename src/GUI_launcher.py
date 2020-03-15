import os
import sys
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QFileDialog, QApplication
from sortedcontainers import SortedSet

from GUI.DialogSaveNewPassage_GUI import Ui_dlgSaveNewPassage
from GUI.WindowDisplayNewWords_GUI import Ui_winDisplayNewWords
from GUI.WindowSelectPassage_GUI import Ui_winSelectPassage
from GUI.WindowSelectStudent_GUI import Ui_winSelectStudent
from src.PrintNewWordsFromTexts import get_new_words

studentsFolderPath = '../students/current_students/'
passagesFolderPath = '../materials/'


class WindowSelectStudent(QtWidgets.QMainWindow, Ui_winSelectStudent):
    studentsFilePaths = []

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
        self.studentsFilePaths.clear()
        for fileName in os.listdir(studentsFolderPath):
            self.studentsFilePaths.append(studentsFolderPath + fileName)
            self.lstStudents.addItem(Path(fileName).stem)

    def addNewStudent(self):
        # noinspection PyArgumentList
        newStudentName, ok = QInputDialog.getText(None, 'New Student', 'Enter New Student\'s Name')
        if ok:
            Path(studentsFolderPath + newStudentName + '.txt').touch()
            self.updateStudentsList()

    def editStudent(self):
        if self.lstStudents.currentItem() is not None:
            studentToBeEditedFilePath = self.studentsFilePaths[self.lstStudents.currentIndex().row()]
            # noinspection PyArgumentList
            newName, ok = QInputDialog.getText(None, 'New Name', 'Enter New Name')
            if ok and newName:
                os.rename(studentToBeEditedFilePath, studentsFolderPath + newName + '.txt')
                self.updateStudentsList()

    def deleteStudent(self):
        if self.lstStudents.currentItem() is not None:
            studentToBeDeletedFilePath = self.studentsFilePaths[self.lstStudents.currentIndex().row()]
            msgboxConfirm = QMessageBox()
            msgboxConfirm.setWindowTitle("Delete Confirmation")
            msgboxConfirm.setText("Are you sure you want to delete this student's file?")
            msgboxConfirm.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

            choice = msgboxConfirm.exec()
            if choice == QMessageBox.Yes:
                os.remove(studentToBeDeletedFilePath)
                self.updateStudentsList()

    @staticmethod
    def deletePassage():
        # noinspection PyArgumentList
        fileToBeDeleted, _ = QFileDialog.getOpenFileName(None, 'Delete File', passagesFolderPath)
        if fileToBeDeleted:
            os.remove(fileToBeDeleted)

    def openSelectPassageWindow(self):
        selectedStudentFilePath = self.studentsFilePaths[self.lstStudents.currentIndex().row()]
        winSelectPassage.selectedStudentFilePath = selectedStudentFilePath
        winSelectPassage.show()
        winSelectPassage.setWindowTitle(Path(selectedStudentFilePath).stem + ' - Select Passages')
        winSelectStudent.close()

    @staticmethod
    def openSaveNewPassageDialog():
        dlgSaveNewPassage.exec()


class DialogSaveNewPassage(QtWidgets.QDialog, Ui_dlgSaveNewPassage):
    savedPassageFilePath = ''

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
            self.savedPassageFilePath = fileName
            dlgSaveNewPassage.close()


class WindowSelectPassage(QtWidgets.QMainWindow, Ui_winSelectPassage):
    selectedStudentFilePath = ''
    addedPassages = SortedSet()

    # noinspection PyArgumentList
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnCancel.clicked.connect(self.cancel)
        self.btnAddToList.clicked.connect(self.addPassagesToList)
        self.btnDeleteFromList.clicked.connect(self.deletePassagesFromList)
        self.btnCreateNewPasage.clicked.connect(self.openSaveNewPassageDialog)
        self.btnOk.clicked.connect(self.ok)

    def cancel(self):
        self.addedPassages.clear()
        self.lstPassages.clear()
        self.close()
        winSelectStudent.show()

    def updatePassagesList(self):
        self.lstPassages.clear()
        for passage in self.addedPassages:
            self.lstPassages.addItem(Path(passage).stem)

    def addPassagesToList(self):
        # noinspection PyArgumentList
        passagesToBeAdded, _ = QFileDialog.getOpenFileNames(None, 'Add Passage', passagesFolderPath)
        if passagesToBeAdded:
            self.addedPassages.update(passagesToBeAdded)
            self.updatePassagesList()

    def deletePassagesFromList(self):
        for index in self.lstPassages.selectedIndexes():
            self.addedPassages.pop(index.row())
        self.updatePassagesList()

    def openSaveNewPassageDialog(self):
        dlgSaveNewPassage.exec()
        self.addedPassages.add(dlgSaveNewPassage.savedPassageFilePath)
        self.updatePassagesList()

    def ok(self):
        if self.lstPassages.count() > 0:
            self.close()
            winDisplayNewWords.selectedStudentFilePath = self.selectedStudentFilePath
            winDisplayNewWords.addedPassages = self.addedPassages
            winDisplayNewWords.outputMode = 'separate' if self.chkMode.isChecked() else 'cumulative'
            winDisplayNewWords.displayNewWords()
            winDisplayNewWords.show()


class WindowDisplayNewWords(QtWidgets.QMainWindow, Ui_winDisplayNewWords):
    selectedStudentFilePath = ''
    addedPassages = SortedSet()
    displayWords = ''
    outputMode = 'cumulative'

    # noinspection PyArgumentList
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnBack.clicked.connect(self.back)
        self.btnCopytoClipboard.clicked.connect(self.copyToClipBoard)
        self.selectedStudentFilePath = ''
        self.addedPassages = SortedSet()
        self.displayWords = ''
        self.outputMode = 'cumulative'

    def back(self):
        self.close()
        self.__init__()
        winSelectPassage.show()

    def displayNewWords(self):
        newWords = get_new_words(self.selectedStudentFilePath, self.addedPassages, self.outputMode)
        for word in newWords:
            self.displayWords += word + '\n'
        self.lblNumWords.setText(str(len(newWords)) + ' new words')
        self.txtNewWords.setText(self.displayWords)

    def copyToClipBoard(self):
        # noinspection PyArgumentList
        QApplication.clipboard().setText(self.displayWords)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    winSelectStudent = WindowSelectStudent()
    dlgSaveNewPassage = DialogSaveNewPassage()
    winSelectPassage = WindowSelectPassage()
    winDisplayNewWords = WindowDisplayNewWords()

    winSelectStudent.show()
    sys.exit(app.exec_())
