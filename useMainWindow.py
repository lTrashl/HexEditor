from mainWindow import Ui_DialogMain
from PyQt5.QtWidgets import QTableWidgetItem  # для работы с таблицей
import sys, os  # для работы с файлами
import array  # пригодится
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetSelectionRange


class useMainWindow(Ui_DialogMain):
    def _init(self):
        print('Create main window')
        return

    def SetMainActions(self, application):
        # обработчики
        self.pushButtonAddress.clicked.connect(self.SetAddress)
        self.pushButtonSave.clicked.connect(self.SaveBlock)
        self.pushButtonOpenFile.clicked.connect(self.OpenFile)

        self.pushButtonClearBlock.clicked.connect(self.ClearBlock)
        self.pushButtonClearRow.clicked.connect(self.ClearRow)

        self.application = application  # может пригодиться. А может и нет
        self.FileName = "test.dat"
        self.Address = 0
        self.chunk = []
        return

    def ClearBlock(self):
        print("Clear block")
        for row in range(0, 16):
            for col in range(0, 16):
                self.tableWidget.setItem(row, col, QTableWidgetItem("00"))

    def ClearRow(self):
        print("Clear row")
        if (self.defaultrow < 0):
            Item = self.tableWidget.currentItem()
            if Item == None:
                print("No current")
                return
            row = Item.row()
        else:
            row = self.defaultrow
        print("row = ", row)
        for col in range(0, 16):
            self.tableWidget.setItem(row, col, QTableWidgetItem("00"))

    def OpenFile(self):
        # открыть файл
        if self.ShowDialog:
            print("Dialog")
            q = QFileDialog()
            fname = q.getOpenFileName()
        else:
            fname = ["test.dat"]
        print(fname[0])
        self.lineEditFileName.setText(fname[0])

        self.FileName = self.lineEditFileName.text()
        self.lineEditAddress.setText("0x00000000")
        self.Address = 0

        statinfo = os.stat(self.FileName)
        self.size = statinfo.st_size
        print("Open ", self.FileName, " size = ", self.size)
        self.ShowBlock()
        return

    def SetAddress(self):
        # Прочитать блок
        print("address")
        if self.value == "":
            self.Address = int(self.lineEditAddress.text(), 16)
        else:
            self.Address = int(self.value, 16)

        if self.Address > self.size: self.Address = self.size - 1;
        self.Address &= 0xFFFFFF00;  # Кратно 256
        self.ShowBlock()
        return

    def SaveBlock(self):
        # Обновить текущий блок
        print("Save ", hex(self.Address), " to ", self.FileName)
        a = array.array('B')  # массив из байтов (unsigned char)

        for row in range(0, 16):
            for col in range(0, 16):
                s = self.tableWidget.item(row, col).text()
                if s != "-":
                    # print(s)
                    try:
                        b1 = int(s, 16)
                        if (b1 < 0) or (b1 > 255):
                            b1 = 1 / 0
                    except:
                        # Вывести на консоль
                        print("ERROR!!", row, " ", col)
                        # позиционировать в таблице
                        self.tableWidget.clearSelection()
                        Range = QTableWidgetSelectionRange(row, col, row, col)
                        self.tableWidget.setRangeSelected(Range, True)
                        # Вывести на GUI
                        mb = QMessageBox()
                        mb.setIcon(QMessageBox.Information)
                        mb.setWindowTitle('Error')
                        mb.setText('Не байт в строке ' + str(row) + ' столбце ' + str(col))
                        mb.setStandardButtons(QMessageBox.Ok)
                        mb.exec()
                        return

                    a.append(b1)

        f = open(self.FileName, 'r+b')
        f.seek(self.Address)
        f.write(a)
        f.close()
        self.ShowBlock()
        return

    # Показать прочитанный блок
    def ShowBlock(self):
        print("Show ", hex(self.Address), " from ", self.FileName)
        self.tableWidget.setRowCount(16)
        self.tableWidget.setColumnCount(17)
        # Раcставить заголовки столбцов и строк
        # Вот так вот незатейливо, но зато быстро - столбцы:
        self.tableWidget.setHorizontalHeaderLabels(
            ["+00", "+01", "+02", "+03", "+04", "+05", "+06", "+07", "+08", "+09", "+0A", "+0B", "+0C", "+0D", "+0E",
             "+0F", "Текст"])
        # по вертикали - чуть затейливее, хотя тоже не фонтан
        labels = []
        for i in range(0, 16):
            labels.append(hex(self.Address + i * 0x10))

        self.tableWidget.setVerticalHeaderLabels(labels)

        f = open(self.FileName, 'rb')

        f.seek(self.Address)
        self.chunk = f.read(256)

        index = 0

        for row in range(0, 16):
            textcolumn = ""  # текстовое представление
            for col in range(0, 16):
                if index < len(self.chunk):
                    b1 = int(self.chunk[index])
                    s = hex(b1)
                    s = s[2:]  # убрать 0x
                # если превышен размер файла - выводить специальный символ
                else:
                    b1 = -1
                    s = "-"
                self.tableWidget.setItem(row, col, QTableWidgetItem(s))
                if b1 >= 0x20:
                    textcolumn += chr(b1)  # '!'#self.chunk[index]
                else:
                    textcolumn += "."
                index += 1
            self.tableWidget.setItem(row, 16, QTableWidgetItem(textcolumn))

        self.tableWidget.resizeColumnsToContents()
        f.close()
        return


