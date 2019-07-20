import sqlite3

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from general import ModuloListItem
from Notifications import NotificationList
from Conector import *


class ModDevolucionItem(ModuloListItem):
    ''' This represents the module Devolucion item on the QListWidget '''
    def __init__(self, listNotifications, *args):
        super(ModDevolucionItem, self).__init__(*args)
        self.listNotifications = listNotifications

    def open_mod(self):
        self.mod5 = Module_Devolucion(self.listNotifications)
        self.mod5.exec_()


class Module_Devolucion(QDialog):
    ''' Module Devolucion window '''
    def __init__(self, listNotifications,*args):
        super(Module_Devolucion, self).__init__(*args)
        self.listNotifications = listNotifications

        loadUi('../gui/moduloDevolucion.ui', self)

        qssFile = "../gui/styles/light.qss"
        with open(qssFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.reset_ui()

    def modificarCantidadSuma(self, nombre, cantidad):
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()

            consulta = conexion.cursor()        
            sql ="""
            SELECT cantidad FROM productos WHERE nombre='%s'
            """%(nombre)        
            if(consulta.execute(sql)):
                cantidad_actual= consulta.fetchone()[0]
                sql ="""UPDATE productos SET cantidad=%i WHERE nombre='%s'
                        """%(cantidad_actual+cantidad,nombre)
                if(consulta.execute(sql)): 
                    respuesta = "Inventario actualizado"
                else:
                    respuesta = "Error al actualizar"

        except sqlite3.OperationalError:
            respuesta = "Error operacional sobre la base de datos"

        finally:
            consulta.close()
            conexion.commit()
            conexion.close()

            QMessageBox.about(self, 'Informacion', respuesta)

            self.reset_ui()

    @pyqtSlot()
    def on_buttonCancel_clicked(self):
        self.close()

    @pyqtSlot()
    def on_buttonAccept_clicked(self):
        self.modificarCantidadSuma(self.lineEditNombre.text(), self.spinBoxCantidadDevolver.value())

    def reset_ui(self):
        self.lineEditNombre.setText("")
        self.spinBoxCantidadDevolver.setValue(0)

    def closeEvent(self, event):
        self.listNotifications.clear()
        notifications = NotificationList(self.listNotifications)
        notifications.update_list()
        event.accept()
