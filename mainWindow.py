
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogMain(object):
    def setupUi(self, DialogMain):
        DialogMain.setObjectName("DialogMain")
        DialogMain.resize(900, 666)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogMain.sizePolicy().hasHeightForWidth())
        DialogMain.setSizePolicy(sizePolicy)
        DialogMain.setMinimumSize(QtCore.QSize(900, 666))
        DialogMain.setMaximumSize(QtCore.QSize(900, 666))
        self.tableWidget = QtWidgets.QTableWidget(DialogMain)
        self.tableWidget.setGeometry(QtCore.QRect(140, 0, 701, 561))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButtonSave = QtWidgets.QPushButton(DialogMain)
        self.pushButtonSave.setGeometry(QtCore.QRect(740, 580, 101, 23))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.lineEditAddress = QtWidgets.QLineEdit(DialogMain)
        self.lineEditAddress.setGeometry(QtCore.QRect(10, 20, 120, 20))
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.pushButtonAddress = QtWidgets.QPushButton(DialogMain)
        self.pushButtonAddress.setGeometry(QtCore.QRect(10, 44, 120, 23))
        self.pushButtonAddress.setObjectName("pushButtonAddress")
        self.lineEditFileName = QtWidgets.QLineEdit(DialogMain)
        self.lineEditFileName.setGeometry(QtCore.QRect(10, 582, 591, 20))
        self.lineEditFileName.setObjectName("lineEditFileName")
        self.pushButtonOpenFile = QtWidgets.QPushButton(DialogMain)
        self.pushButtonOpenFile.setGeometry(QtCore.QRect(610, 580, 120, 23))
        self.pushButtonOpenFile.setObjectName("pushButtonOpenFile")
        self.pushButtonClearRow = QtWidgets.QPushButton(DialogMain)
        self.pushButtonClearRow.setGeometry(QtCore.QRect(10, 140, 120, 23))
        self.pushButtonClearRow.setObjectName("pushButtonClearRow")
        self.pushButtonClearBlock = QtWidgets.QPushButton(DialogMain)
        self.pushButtonClearBlock.setGeometry(QtCore.QRect(10, 180, 120, 23))
        self.pushButtonClearBlock.setObjectName("pushButtonClearBlock")

        self.retranslateUi(DialogMain)
        QtCore.QMetaObject.connectSlotsByName(DialogMain)

    def retranslateUi(self, DialogMain):
        _translate = QtCore.QCoreApplication.translate
        DialogMain.setWindowTitle(_translate("DialogMain", "Simple Hex Editor"))
        self.pushButtonSave.setText(_translate("DialogMain", "Сохранить"))
        self.lineEditAddress.setText(_translate("DialogMain", "0x00000000"))
        self.pushButtonAddress.setText(_translate("DialogMain", "Перейти"))
        self.lineEditFileName.setText(_translate("DialogMain", "test.dat"))
        self.pushButtonOpenFile.setText(_translate("DialogMain", "Загрузить"))
        self.pushButtonClearRow.setText(_translate("DialogMain", "Обнулить строку"))
        self.pushButtonClearBlock.setText(_translate("DialogMain", "Обнулить блок"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogMain = QtWidgets.QDialog()
    ui = Ui_DialogMain()
    ui.setupUi(DialogMain)
    DialogMain.show()
    sys.exit(app.exec_())

