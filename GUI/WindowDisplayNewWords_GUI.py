# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowDisplayNewWords.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_winDisplayNewWords(object):
    def setupUi(self, winDisplayNewWords):
        winDisplayNewWords.setObjectName("winDisplayNewWords")
        winDisplayNewWords.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(winDisplayNewWords)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.txtNewWords = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.txtNewWords.setFont(font)
        self.txtNewWords.setAcceptRichText(False)
        self.txtNewWords.setObjectName("txtNewWords")
        self.gridLayout.addWidget(self.txtNewWords, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnCopyAllWords = QtWidgets.QPushButton(self.centralwidget)
        self.btnCopyAllWords.setObjectName("btnCopyAllWords")
        self.verticalLayout.addWidget(self.btnCopyAllWords)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setObjectName("btnBack")
        self.verticalLayout.addWidget(self.btnBack)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.lblNumWords = QtWidgets.QLabel(self.centralwidget)
        self.lblNumWords.setObjectName("lblNumWords")
        self.gridLayout.addWidget(self.lblNumWords, 0, 0, 1, 1)
        winDisplayNewWords.setCentralWidget(self.centralwidget)

        self.retranslateUi(winDisplayNewWords)
        QtCore.QMetaObject.connectSlotsByName(winDisplayNewWords)

    def retranslateUi(self, winDisplayNewWords):
        _translate = QtCore.QCoreApplication.translate
        winDisplayNewWords.setWindowTitle(_translate("winDisplayNewWords", "Contained Words"))
        self.txtNewWords.setHtml(_translate("winDisplayNewWords",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnCopyAllWords.setText(_translate("winDisplayNewWords", "Copy All Words"))
        self.btnBack.setText(_translate("winDisplayNewWords", "Back"))
        self.lblNumWords.setText(_translate("winDisplayNewWords", "# words"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    winDisplayNewWords = QtWidgets.QMainWindow()
    ui = Ui_winDisplayNewWords()
    ui.setupUi(winDisplayNewWords)
    winDisplayNewWords.show()
    sys.exit(app.exec_())
