import sqlite3

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from general import ModuloListItem
from Notifications import NotificationList
from Conector import *


class ModModificarUsuarioItem(ModuloListItem):
    ''' This represents the module ModificarUsuario item on the QListWidget '''
    def __init__(self, *args):
        super(ModModificarUsuarioItem, self).__init__(*args)

    def open_mod(self):
        self.mod = Module_ModificarUsuario()
        self.mod.exec_()


class Module_ModificarUsuario(QDialog):
    ''' Module ModificarUsuario window '''
    def __init__(self, *args):
        super(Module_ModificarUsuario, self).__init__(*args)

        loadUi('../gui/moduloModificarUsuario.ui', self)

        qssFile = "../gui/styles/light.qss"
        with open(qssFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.reset_ui()
        self.buttonAccept.setEnabled(False)

    @pyqtSlot()
    def on_buttonCancel_clicked(self):
        self.close()

    @pyqtSlot()
    def on_buttonAccept_clicked(self):
        pass

    @pyqtSlot()
    def on_buttonSearch_clicked(self):
        pass

    def reset_ui(self):
        pass
