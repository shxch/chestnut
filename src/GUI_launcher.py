import os
import sys
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QFileDialog, QApplication, QLineEdit
from sortedcontainers import SortedSet

from GUI.MenuBar_GUI import Ui_mnb
from GUI.WindowDisplayNewWords_GUI import Ui_winDisplayNewWords
from GUI.WindowSelectPassage_GUI import Ui_winSelectPassage
from GUI.WindowSelectStudent_GUI import Ui_winSelectStudent
from src.PrintNewWordsFromTexts import get_new_words

projectPath = Path(__file__).parent.parent
passagesFolderPath = projectPath.joinpath('materials/')
studentsFolderPath = projectPath.joinpath('students/')


class WindowSelectStudent(QtWidgets.QMainWindow, Ui_winSelectStudent):

    def __init__(self, parent=None):
        # noinspection PyArgumentList
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setMenuBar(MenuBar())
        self.fileModel = QtWidgets.QFileSystemModel()
        self.fileModel.setRootPath('')
        self.tvwStudents.setModel(self.fileModel)
        self.tvwStudents.setRootIndex(self.fileModel.index(str(studentsFolderPath)))
        self.tvwStudents.hideColumn(1)
        self.tvwStudents.hideColumn(2)
        self.tvwStudents.hideColumn(3)
        self.tvwStudents.doubleClicked.connect(self.openStudentFile)
        self.btnNewStudent.clicked.connect(self.addNewStudent)
        self.btnDelete.clicked.connect(self.deleteStudent)
        self.btnRename.clicked.connect(self.renameStudent)
        self.btnNext.clicked.connect(self.openSelectPassageWindow)

    def addNewStudent(self):
        index = self.tvwStudents.currentIndex()
        currentFilePath = self.fileModel.filePath(index)
        # noinspection PyArgumentList
        newStudentName, ok = QInputDialog.getText(None, 'New Student', 'Enter New Student\'s Name')
        if ok:
            if os.path.isfile(currentFilePath):
                newFolderPath = Path(currentFilePath).parent
            else:
                newFolderPath = Path(currentFilePath)
            Path(newFolderPath.joinpath(Path(newStudentName))).touch()

    def renameStudent(self):
        index = self.tvwStudents.currentIndex()
        # noinspection PyArgumentList
        newName, ok = QInputDialog.getText(None, 'New Name', 'Enter New Name', QLineEdit.Normal,
                                           self.fileModel.fileName(index))
        if ok and newName:
            os.rename(self.fileModel.filePath(index), Path(self.fileModel.filePath(index)).parent.joinpath(newName))

    def deleteStudent(self):
        index = self.tvwStudents.currentIndex()
        msgboxConfirm = QMessageBox()
        msgboxConfirm.setWindowTitle("Delete Confirmation")
        msgboxConfirm.setText("Are you sure you want to delete " + self.fileModel.fileName(index) + "?")
        msgboxConfirm.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        choice = msgboxConfirm.exec()
        if choice == QMessageBox.Yes:
            os.remove(self.fileModel.filePath(index))

    def openSelectPassageWindow(self):
        index = self.tvwStudents.currentIndex()
        winSelectPassage.selectedStudentFilePath = self.fileModel.filePath(index)
        winSelectPassage.show()
        winSelectPassage.setWindowTitle(self.fileModel.fileName(index) + ' - Select Passages')
        winSelectStudent.close()

    def openStudentFile(self, index):
        filePath = self.fileModel.filePath(index)
        if os.path.isfile(filePath):
            os.system('notepad ' + filePath)


class WindowSelectPassage(QtWidgets.QMainWindow, Ui_winSelectPassage):

    # noinspection PyArgumentList
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setMenuBar(MenuBar())
        self.selectedStudentFilePath = ''
        self.addedPassagesFilePaths = SortedSet()
        self.btnCancel.clicked.connect(self.cancel)
        self.btnAdd.clicked.connect(self.addPassagesToList)
        self.btnRemove.clicked.connect(self.removePassagesFromList)
        self.btnOk.clicked.connect(self.ok)
        self.lstPassages.doubleClicked.connect(self.openPassageFile)

    def cancel(self):
        self.close()
        self.__init__()
        winSelectStudent.show()

    def updatePassagesList(self):
        self.lstPassages.clear()
        for passage in self.addedPassagesFilePaths:
            self.lstPassages.addItem(Path(passage).stem)

    def addPassagesToList(self):
        # noinspection PyArgumentList
        passagesToBeAdded, _ = QFileDialog.getOpenFileNames(None, 'Add Passage', str(passagesFolderPath))
        if passagesToBeAdded:
            self.addedPassagesFilePaths.update(passagesToBeAdded)
            self.updatePassagesList()

    def removePassagesFromList(self):
        toBeRemovedPassagesFilePaths = []
        for index in self.lstPassages.selectedIndexes():
            toBeRemovedPassagesFilePaths.append(self.addedPassagesFilePaths[index.row()])
        self.addedPassagesFilePaths.difference_update(toBeRemovedPassagesFilePaths)
        self.updatePassagesList()

    def ok(self):
        if self.lstPassages.count() > 0:
            self.close()
            winDisplayNewWords.selectedStudentFilePath = self.selectedStudentFilePath
            winDisplayNewWords.addedPassages = self.addedPassagesFilePaths
            winDisplayNewWords.outputMode = 'separate' if self.chkOutputMode.isChecked() else 'cumulative'
            winDisplayNewWords.displayNewWords()
            winDisplayNewWords.show()

    def openPassageFile(self, index):
        os.system("notepad " + self.addedPassagesFilePaths[index.row()])


class WindowDisplayNewWords(QtWidgets.QMainWindow, Ui_winDisplayNewWords):

    # noinspection PyArgumentList
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.selectedStudentFilePath = ''
        self.addedPassages = SortedSet()
        self.outputMode = 'cumulative'
        self.displayWords = ''
        self.btnBack.clicked.connect(self.back)
        self.btnCopytoClipboard.clicked.connect(self.copyToClipBoard)

    def back(self):
        self.close()
        self.__init__()
        winSelectPassage.show()

    def displayNewWords(self):
        newWords = get_new_words(self.selectedStudentFilePath, self.addedPassages, self.outputMode)
        for word in newWords:
            self.displayWords += word + '\n'
        self.setWindowTitle(Path(self.selectedStudentFilePath).stem)
        self.lblNumWords.setText(str(len(newWords)) + ' new words')
        self.txtNewWords.setText(self.displayWords)

    def copyToClipBoard(self):
        # noinspection PyArgumentList
        QApplication.clipboard().setText(self.displayWords)
        msgCopied = QMessageBox()
        msgCopied.setText("New words have been copied to clipboard.")
        msgCopied.setWindowTitle("Success")
        msgCopied.setStandardButtons(QMessageBox.Ok)
        msgCopied.exec()


class MenuBar(QtWidgets.QMenuBar, Ui_mnb):
    def __init__(self, parent=None):
        QtWidgets.QMenuBar.__init__(self, parent)
        self.setupUi(self)
        self.actionNewPassage.triggered.connect(self.createNewPassage)
        self.actionOpenPassageFile.triggered.connect(self.openPassageFile)

    @staticmethod
    def createNewPassage():
        os.system("notepad")

    @staticmethod
    def openPassageFile():
        # noinspection PyArgumentList
        fileToBeOpened, _ = QFileDialog.getOpenFileName(None, 'Open File', str(passagesFolderPath))
        if fileToBeOpened:
            os.system("notepad " + fileToBeOpened)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mnb = MenuBar()
    winSelectStudent = WindowSelectStudent()
    winSelectPassage = WindowSelectPassage()
    winDisplayNewWords = WindowDisplayNewWords()

    winSelectStudent.show()
    sys.exit(app.exec())
