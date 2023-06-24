from PyQt6 import QtCore, QtWidgets, QtGui


class Ui_mnb(object):
    def setupUi(self, mnb):
        mnb.setGeometry(QtCore.QRect(0, 0, 600, 20))
        mnb.setObjectName("menuBar")
        self.menuPassage = QtWidgets.QMenu(mnb)
        self.menuPassage.setObjectName("menuPassage")
        self.actionNewPassage = QtGui.QAction(mnb)
        self.actionNewPassage.setObjectName("actionNewPassage")
        self.actionOpenPassageFile = QtGui.QAction(mnb)
        self.actionOpenPassageFile.setObjectName("actionOpenPassageFile")
        self.menuPassage.addAction(self.actionNewPassage)
        self.menuPassage.addAction(self.actionOpenPassageFile)
        mnb.addAction(self.menuPassage.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(mnb)

    def retranslateUi(self):
        self.menuPassage.setTitle("File")
        self.actionNewPassage.setText("New Passage")
        self.actionOpenPassageFile.setText("Open Passage")
