import sqlite3

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from general import ModuloListItem
from Notifications import NotificationList
from Conector import *


class ModModificarItem(ModuloListItem):
    ''' This represents the module Modificar item on the QListWidget '''
    def __init__(self, listNotifications, *args):
        super(ModModificarItem, self).__init__(*args)
        self.listNotifications = listNotifications

    def open_mod(self):
        self.mod2 = Module_Modificar(self.listNotifications)
        self.mod2.exec_()


class Module_Modificar(QDialog):
    ''' Module Modificar window '''

    producto = ""

    def __init__(self,listNotifications, *args):
        super(Module_Modificar, self).__init__(*args)
        self.listNotifications = listNotifications

        loadUi('../gui/moduloModificar.ui', self)

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
        name = self.lineEditNombre.text()

        buttonReply = QMessageBox.question(self, 'Agregar', '¿Esta seguro que desea agregar el producto {}?\n\n'.format(name))      

        if buttonReply == QMessageBox.Yes:
            respuesta = self.modificar()

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
            self.spinBoxCantidad.setMinimum(1)
            self.spinBoxCantidad.setValue(valsSearch[3])
            self.spinBoxCantidadMin.setValue(valsSearch[4])
            self.checkBoxRetornable.setChecked(bool(valsSearch[5]))
            self.buttonAccept.setDisabled(False)
            self.producto = valsSearch[0]
        
        except IndexError:
            if (self.lineEditNombre.text() != ""):
                self.comboBoxDepartamento.setCurrentIndex(0)
                self.spinBoxCantidad.setMinimum(1)
                self.spinBoxCantidad.setValue(1)
                self.spinBoxCantidadMin.setValue(0)
                self.buttonAccept.setDisabled(True)
            
        except sqlite3.OperationalError:
            respuesta = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()
    
    def modificar(self):
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()

            sql = """
            UPDATE productos SET 
                                departamento=?, 
                                nombre=?, 
                                cantidad=?, 
                                cantidadminima=?, 
                                retornable=? 
                            WHERE idproductos=? """

            cur.execute(sql,    (self.comboBoxDepartamento.currentText(), 
                                self.lineEditNombre.text(), 
                                self.spinBoxCantidad.value(), 
                                self.spinBoxCantidadMin.value(), 
                                int(bool(self.checkBoxRetornable.checkState())), 
                            self.producto,))

            respuesta = "Producto modificado exitosamente"

        except sqlite3.OperationalError:
            respuesta = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()
            
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
