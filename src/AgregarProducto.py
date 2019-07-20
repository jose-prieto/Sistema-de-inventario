import sqlite3

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from general import ModuloListItem
from Conector import *


class ModAgregarItem(ModuloListItem):
    ''' This represents the module Agregar item on the QListWidget '''
    def __init__(self, *args):
        super(ModAgregarItem, self).__init__(*args)

    def open_mod(self):
        self.mod1 = Module_Agregar()
        self.mod1.exec_()


class Module_Agregar(QDialog):
    ''' Module Agregar window '''

    existente = 4
    
    def __init__(self, *args):
        super(Module_Agregar, self).__init__(*args)
        loadUi('../gui/moduloAgregar.ui', self)

        qssFile = "../gui/styles/light.qss"
        with open(qssFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.reset_ui()

    @pyqtSlot()
    def on_buttonCancel_clicked(self):
        self.close()

    @pyqtSlot()
    def on_buttonAccept_clicked(self):
        name = self.lineEditNombre.text()

        buttonReply = QMessageBox.question(self, 'Agregar', '¿Esta seguro que desea agregar el producto {}?\n\n'.format(name))      

        if buttonReply == QMessageBox.Yes:
            if (self.existente == 0):
                respuesta = self.crear(name, int(self.spinBoxCantidad.value()),
                int(self.spinBoxCantidadMin.value()), int(bool(self.checkBoxRetornable.checkState())), self.comboBoxDepartamento.currentText())

                
            elif (self.existente == 1):
                respuesta = self.agregar()

            QMessageBox.information(self, 'Informacion', respuesta)

            self.reset_ui()
            self.close()

    @pyqtSlot()
    def on_buttonSearch_clicked(self):
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()
            
            sql = """
            SELECT * FROM productos WHERE nombre=?"""

            cur.execute(sql, (self.lineEditNombre.text(),))

            valsSearch = cur.fetchall()[0]
            self.comboBoxDepartamento.setCurrentIndex(self.comboBoxDepartamento.findText(valsSearch[1]))
            self.spinBoxCantidad.setMinimum(valsSearch[3])
            self.spinBoxCantidadMin.setValue(valsSearch[4])
            self.checkBoxRetornable.setChecked(bool(valsSearch[5]))
            self.lineEditNombre.setDisabled(True)
            self.comboBoxDepartamento.setDisabled(True)
            self.spinBoxCantidadMin.setDisabled(True)
            self.checkBoxRetornable.setDisabled(True)
            self.buttonAccept.setDisabled(False)
            self.buttonSearch.setDisabled(True)
            self.existente = 1
        
        except IndexError:
            if (self.lineEditNombre.text() != ""):
                self.comboBoxDepartamento.setCurrentIndex(0)
                self.spinBoxCantidad.setMinimum(1)
                self.spinBoxCantidad.setValue(1)
                self.spinBoxCantidadMin.setValue(0)
                self.checkBoxRetornable.setChecked(False)
                self.comboBoxDepartamento.setDisabled(False)
                self.spinBoxCantidadMin.setDisabled(False)
                self.checkBoxRetornable.setDisabled(False)
                self.buttonAccept.setDisabled(False)
                self.lineEditNombre.setDisabled(True)
                self.buttonSearch.setDisabled(True)
                self.existente = 0
            
        except sqlite3.OperationalError:
            respuesta = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()

    def crear(self, nombre, cantidad, cantidadmin, retornable, departamento):
        ''' Crear la entidad en la base de datos '''
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()

            sql = """
            INSERT INTO productos(nombre, cantidad, cantidadminima, retornable, departamento)
            VALUES (?, ?, ?, ?, ?)"""
            if cur.execute(sql, (nombre,cantidad,cantidadmin,retornable, departamento,)):
                respuesta = "El producto {} fue agregado correctamente".format(nombre)
            else:
                respuesta = "No se pudo agregar correctamente"

        except sqlite3.OperationalError:
            respuesta = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()

        return respuesta
    
    def agregar(self):
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()

            sql = """
            UPDATE productos SET cantidad=? WHERE nombre=? """

            cur.execute(sql, (self.spinBoxCantidad.value(), self.lineEditNombre.text(),))

            respuesta = "Producto modificado exitosamente"

        except sqlite3.OperationalError:
            respuesta = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()

            self.reset_ui()
            self.buttonAccept.setEnabled(False)
            
        return respuesta

    def reset_ui(self):
        self.lineEditNombre.setText("")
        self.spinBoxCantidad.setValue(1)
        self.spinBoxCantidadMin.setValue(0)
        self.lineEditNombre.setDisabled(False)
        self.checkBoxRetornable.setChecked(False)
        self.comboBoxDepartamento.setCurrentIndex(0)
        self.spinBoxCantidadMin.setDisabled(False)
        self.checkBoxRetornable.setDisabled(False)
        self.buttonSearch.setDisabled(False)
