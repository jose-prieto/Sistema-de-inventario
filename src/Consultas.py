import sqlite3

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from general import ModuloListItem
from Conector import *


class ModConsultasItem(ModuloListItem):
    ''' This represents the module Consultas item on the QListWidget '''
    def __init__(self, *args):
        super(ModConsultasItem, self).__init__(*args)

    def open_mod(self):
        self.mod4 = Module_Consultas()
        self.mod4.exec_()


class Module_Consultas(QDialog):
    ''' Module Consultas window '''
    def __init__(self, *args):
        super(Module_Consultas, self).__init__(*args)
        loadUi('../gui/moduloConsultas.ui', self)

        qssFile = "../gui/styles/light.qss"
        with open(qssFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.reset_ui()

    @pyqtSlot()
    def on_buttonCancel_clicked(self):
        self.close()

    @pyqtSlot()
    def on_buttonBuscar_clicked(self):
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()
            
            sql = """
            SELECT * FROM productos WHERE nombre=?"""

            cur.execute(sql, (self.lineEditNombre.text(),))

            valsSearch = cur.fetchall()[0]

            nombre = valsSearch[1]
            cantidad = valsSearch[2]
            cantidadMin = valsSearch[3]
            retornable = bool(valsSearch[4])

            respuesta = "Nombre: {}\nCantidad: {}\nCantidad Minima: {}\nRetornable: {}".format(nombre, cantidad, cantidadMin, retornable)
        
        except IndexError:
            respuesta = "Ese producto no se encuentra en la base de datos"
        except sqlite3.OperationalError:
            mensaje = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()

            QMessageBox.about(self, 'Informacion', respuesta)

    def reset_ui(self):
        self.lineEditNombre.setText("")
