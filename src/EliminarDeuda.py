import sqlite3

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from general import ModuloListItem
from Conector import *


class ModEliminarDeudaItem(ModuloListItem):
    ''' This represents the module EliminarDeuda item on the QListWidget '''
    def __init__(self, *args):
        super(ModEliminarDeudaItem, self).__init__(*args)

    def open_mod(self):
        self.mod = Module_EliminarDeuda()
        self.mod.exec_()


class Module_EliminarDeuda(QDialog):
    ''' Module EliminarDeuda window '''
    def __init__(self, *args):
        super(Module_EliminarDeuda, self).__init__(*args)
        loadUi('../gui/moduloEliminarDeuda.ui', self)

        qssFile = "../gui/styles/light.qss"
        with open(qssFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.reset_ui()

    @pyqtSlot()
    def on_buttonCancel_clicked(self):
        self.close()

    @pyqtSlot()
    def on_buttonAccept_clicked(self):
        pass

    def reset_ui(self):
        pass
