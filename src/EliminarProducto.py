import sqlite3

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from general import ModuloListItem
from Conector import *


class ModEliminarItem(ModuloListItem):
    ''' This represents the module Eliminar item on the QListWidget '''
    def __init__(self, *args):
        super(ModEliminarItem, self).__init__(*args)

    def open_mod(self):
        self.mod = Module_Eliminar()
        self.mod.exec_()


class Module_Eliminar(QDialog):
    ''' Module Eliminar window '''

    name = ""

    def __init__(self, *args):
        super(Module_Eliminar, self).__init__(*args)
        loadUi('../gui/moduloEliminar.ui', self)

        qssFile = "../gui/styles/light.qss"
        with open(qssFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.reset_ui()

    @pyqtSlot()
    def on_buttonCancel_clicked(self):
        self.close()

    @pyqtSlot()
    def on_buttonAccept_clicked(self):
        self.name = self.lineEditNombre.text()

        buttonReply = QMessageBox.question(self, 'Eliminar', '¿Esta seguro que desea eliminar el producto {}?\n\n'.format(self.name))      

        if buttonReply == QMessageBox.Yes:
            
            respuesta = self.eliminar()

            QMessageBox.information(self, 'Informacion', respuesta)

            self.reset_ui()
            self.close()

    def eliminar(self):
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()

            sql = """ DELETE FROM productos WHERE nombre=? """

            cur.execute(sql, (self.lineEditNombre.text(),))
            valsSearch = cur.fetchall()[0]
            
            respuesta = "El producto {} fue eliminado de la base de datos correctamente".format(self.name)

        except IndexError:
            respuesta = "Producto inexistente"

        except sqlite3.OperationalError:
            respuesta = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()

        return respuesta

    def reset_ui(self):
        pass
