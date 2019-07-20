import sqlite3
from datetime import datetime

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from general import ModuloListItem
from Notifications import NotificationListItem

from Conector import *


class ModRetiroItem(ModuloListItem):
    ''' This represents the module Retiro item on the QListWidget '''
    def __init__(self, listNotifications, *args):
        super(ModRetiroItem, self).__init__(*args)
        self.listNotifications = listNotifications

    def open_mod(self):
        self.mod3 = Module_Retiro(self.listNotifications)
        self.mod3.exec_()


class Module_Retiro(QDialog):
    ''' Module Retiro window '''
    def __init__(self, listNotifications, *args):
        super(Module_Retiro, self).__init__(*args)
        self.listNotifications = listNotifications
        loadUi('../gui/moduloRetiro.ui', self)

        qssFile = "../gui/styles/light.qss"
        with open(qssFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.reset_ui()

    def modificarCantidadResta(self, nombre, cantidad):
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            consulta = conexion.cursor()    

            sqlSearchCantidad ="""
            SELECT cantidad, cantidadminima, retornable FROM productos WHERE nombre=?"""

            if consulta.execute(sqlSearchCantidad, (nombre,)):
                cantidad_actual, cantidad_minima, retornable = consulta.fetchone()
                fecha_actual = datetime.now().strftime("%D")
                hora_actual = datetime.now().strftime("%H:%M:%S")

                sqlUpdateProductos = """UPDATE productos SET cantidad=? WHERE nombre=?"""

                sqlInsertPrestamo = """INSERT INTO ReportePrestamo(persona_a_quien_se_le_presto,fecha_prestamo,hora_prestamo,motivo,fecha_devolucion,hora_devolucion,estado_prestamo,usuario_id)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?)"""

                cantidad_resultante = cantidad_actual-cantidad
                if cantidad_resultante < 0:
                    respuesta = "No se pudo generar el prestamo, existe {} de {}".format(cantidad_actual, nombre)
                elif consulta.execute(sqlUpdateProductos, (cantidad_resultante,nombre,)):
                    if consulta.execute(sqlInsertPrestamo,  ("Ninguno", fecha_actual,hora_actual,self.lineEditMotivo.text(),"","",1,0,)):
                        respuesta = "Inventario actualizado y reporte generado"
                
                        if cantidad_resultante < cantidad_minima:
                            texto = "Se debe comprar: {} | Cantidad actual: {}".format(nombre, cantidad_resultante)

                            if retornable == 1:
                                texto = "Se debe devolver: {} | Cantidad actual: {}".format(nombre, cantidad_resultante)

                            iconNotification = QIcon('../gui/images/important.svg')
                            NotificationListItem(iconNotification, texto, self.listNotifications)
                    else:
                        respuesta = "Error al actualizar"
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
        self.modificarCantidadResta(self.lineEditNombre.text(), self.spinBoxCantidadRetirar.value())

    def reset_ui(self):
        self.lineEditNombre.setText("")
        self.lineEditMotivo.setText("")
        self.spinBoxCantidadRetirar.setValue(1)
