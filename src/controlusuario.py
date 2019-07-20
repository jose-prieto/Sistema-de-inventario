import re

from general import ModuloListItem
from CRUD_Usuario import *


class Controlusuario(object):

    def crearusuario(self, nombre, cedula, correo , contraseña, cargo):
        try:
            dao = CRUD_Usuario()
            if(isinstance(cedula, str) and isinstance(cedula, str) and isinstance(nombre, str) and cedula.isdigit() and re.search("@",correo) ):
                if(dao.existeusuario(cedula)==0):
                    mensaje=dao.crear(nombre,cedula,correo,1,cargo,contraseña,0)

                else: mensaje="EXISTE USUARIO"
            else: mensaje="Algunos de los datos es invalido"
        except: 
            mensaje="Error inesperado con la aplicacion"
        return mensaje

    def modificarusuario(self,nombre):
        mensaje=nombre
        return mensaje

    def eliminardeuda(self):
        mensaje="deuda"

        return mensaje

    def eliminarusuario(self):
        mensaje="eliminar usuario"
        return mensaje    
