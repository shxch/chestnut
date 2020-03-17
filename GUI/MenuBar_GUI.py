from PyQt5 import QtCore, QtWidgets


class Ui_mnb(object):
    def setupUi(self, mnb):
        mnb.setGeometry(QtCore.QRect(0, 0, 600, 20))
        mnb.setObjectName("menuBar")
        self.menuPassage = QtWidgets.QMenu(mnb)
        self.menuPassage.setObjectName("menuPassage")
        self.actionNewPassage = QtWidgets.QAction(mnb)
        self.actionNewPassage.setObjectName("actionNewPassage")
        self.actionOpenPassageFile = QtWidgets.QAction(mnb)
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
