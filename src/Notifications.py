import sqlite3

from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi

from Conector import *


class NotificationListItem(QListWidgetItem):
    ''' A list item for the notifications with extra configs '''
    def __init__(self, *args, **kwargs):
        super(NotificationListItem, self).__init__(*args, **kwargs)
        self.setSizeHint(QSize(30, 30))
        self.setTextAlignment(Qt.AlignCenter)
        self.args = args

    def open_noti(self):
        pass


class NotificationList:
    def __init__(self, listNotifications):
        self.listNotifications = listNotifications

    def update_list(self):
        """ Revisa la base de datos para llenar el area de notificaciones """
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()

            sqlFaltantes = """SELECT nombre, cantidad, retornable FROM productos WHERE cantidad < cantidadminima"""
            cur.execute(sqlFaltantes)
            notifications = cur.fetchall()

            iconNotification = QIcon('../gui/images/important.svg')

            for content in notifications:
                texto = "Se debe comprar: {} | Cantidad actual: {}".format(content[0], content[1])
                if content[2] == 1:
                    texto = "Se debe devolver: {} | Cantidad actual: {}".format(content[0], content[1])

                NotificationListItem(iconNotification, texto, self.listNotifications)

        except sqlite3.OperationalError:
            respuesta = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()
