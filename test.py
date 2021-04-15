import unittest


class unitTest(unittest.TestCase):

    def run(self, ui):
        self.Test_OpenFile(ui)
        self.Test_Address(ui)
        self.Test_ClearBlock(ui)
        self.Test_ClearRow(ui)
        self.Test_Save(ui)

    def Test_OpenFile(self, ui):
        ui.OpenFile(False)

    def Test_Address(self, ui):
        ui.SetAddress("0x0000")

    def Test_ClearRow(self, ui):
        ui.ClearRow(1)

    def Test_ClearBlock(self, ui):
        ui.ClearBlock()

    def Test_Save(self, ui):
        ui.SaveBlock()
