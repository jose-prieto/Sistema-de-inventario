import sqlite3

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from general import ModuloListItem
from controlusuario import *
from Conector import *


class ModCrearUsuarioItem(ModuloListItem):
    ''' This represents the module CrearUsuario item on the QListWidget '''
    def __init__(self, *args):
        super(ModCrearUsuarioItem, self).__init__(*args)

    def open_mod(self):
        self.mod = Module_CrearUsuario()
        self.mod.exec_()

class Module_CrearUsuario(QDialog):
    ''' Module CrearUsuario window '''
    def __init__(self, *args):
        super(Module_CrearUsuario, self).__init__(*args)
        loadUi('../gui/moduloCrearUsuario.ui', self)

        qssFile = "../gui/styles/light.qss"
        with open(qssFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.reset_ui()

    @pyqtSlot()
    def on_buttonCancel_clicked(self):
        self.close()
        pass

    @pyqtSlot()
    def on_buttonAccept_clicked(self):
        name = self.nombre.text()

        buttonReply = QMessageBox.question(self, 'Agregar',
                        '¿Esta seguro que desea crear el usuario de {}?\n\n'.format(name))

        if buttonReply == QMessageBox.Yes:
            control = Controlusuario()
            respuesta= control.crearusuario(name,self.cedula.text(),self.correo.text(), self.contrasena.text(), self.tipo.currentText())
            #respuesta = control.crearusuario()
            #respuesta = self.crear(name, str(combobox.currentText()), self.spinBoxCantidadMin.value(), self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text())

            QMessageBox.information(self, 'Informacion', respuesta)

            self.reset_ui()
        pass

    def crear(self, nombre, cargo, ci, correo, passw):
        ''' Crear la entidad en la base de datos '''
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()

            sql = """
            INSERT INTO Usuario(nombre, cedula, mail, numero, cargo, password)
            VALUES (?, ?, ?, ?, ?, ?)"""
            if cur.execute(sql, (nombre,ci,correo, 100,cargo,passw,)):
                respuesta = "El usuario {} fue creado correctamente".format(nombre)
            else:
                respuesta = "No se pudo agregar correctamente"     

        except sqlite3.OperationalError:
            respuesta = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()

        return respuesta

    def reset_ui(self):
        self.nombre.setText("")
        self.contrasena.setText("")
        self.cedula.setText("")
        self.correo.setText("")
