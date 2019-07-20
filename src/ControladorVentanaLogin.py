import sys
import sqlite3
import os

from PyQt5.QtCore import pyqtSlot,QProcess
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox,QApplication
from PyQt5.uic import loadUi
from Conector import *

from Depot import *


class ControladorVentanaLogin(QDialog):
    ''' Module Agregar window '''

    cargo = ""

    def __init__(self, *args):
        super(ControladorVentanaLogin, self).__init__(*args)
        loadUi('../gui/ingreso.ui', self)

        qssFile = "../gui/styles/light.qss"
        with open(qssFile, "r") as fh:
            self.setStyleSheet(fh.read())
        self.setWindowTitle("Depot")


    @pyqtSlot()
    def on_botonCerrar_clicked(self):
        self.close()

    @pyqtSlot()
    def on_botonAceptar_clicked(self):
        ingreso = []
        if (self.textoUsuario.text() == "" or self.textoPassword.text() == ""):
            self.error1.setText("Ninguno de los campos puede estar vacio, por favor rellenelos y presione ingresar nuevamente")
        else:
            ingreso = self.verificar(self.textoUsuario.text(),self.textoPassword.text())
            if (ingreso[0]):    # Desde aqui se debe crear DEPOT
                mainProcess = QProcess(self)
                if (self.cargo == "Administrador"):
                    mainProcess.start("python",["./Depot.py"])
                elif (self.cargo == "Operador"):
                    mainProcess.start("python",["./DepotOperador.py"])
                elif (self.cargo == "Gerente"):
                    mainProcess.start("python",["./DepotGerente.py"])
            else:
                self.error1.setText("Usuario o contraseña invalidos por favor intentelo nuevamente")
        self.close()
    
    def verificar(self, cedula, password):
        respuesta = []
        respuesta.append(False)
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()
            sql = "SELECT cedula,password,cargo FROM Usuario"
            if (cur.execute(sql)):
                rows = cur.fetchall() 
                for row in rows:
                    if ((row[0] == cedula) and (row[1] == password)):
                        respuesta[0] = True
                        respuesta.append(row[2])
                        self.cargo = row[2]
            else:
                respuesta[0] = False
        except sqlite3.OperationalError:
            respuesta[0] = False

        finally:
            cur.close()
            conexion.commit()
            conexion.close()

        return respuesta

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = ControladorVentanaLogin()
    controller.show()
    sys.exit(app.exec_())
