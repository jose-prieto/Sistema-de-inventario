import sqlite3

from general import ModuloListItem
from Notifications import NotificationList
from Conector import *

class CRUD_Usuario(object):

    def crear(self, nombre, cedula, correo, numero, cargo, contra, deuda):
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()


            argumentos = (nombre, cedula, correo, numero, cargo, contra)

            sql = """
            INSERT INTO Usuario(nombre, cedula, mail, numero, cargo, password)
            VALUES (?, ?, ?, ?, ?, ?)"""

            if(cur.execute(sql, argumentos)): mensaje="El usuario se creo correctamente"
            else: mensaje="El usuario no pudo ser creado"       
        except sqlite3.OperationalError:
            mensaje = "Error operacional sobre la base de datos"
        finally:
            cur.close()
            conexion.commit()
            conexion.close()

        return mensaje


    def modificarusuario(self, cedula, nombre, correo):
        ''' modifica nombre y correo por el numero de cedula '''
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()

            argumentos = ( nombre, correo, cedula)

            sql ="""
            UPDATE Usuario SET nombre=(?),mail=(?) WHERE cedula=(?)
            """

            if(cur.execute(sql, argumentos)): mensaje="El usuario se modifico correctamente"
            else:mensaje=" Error al modificar usuario"
 
        except sqlite3.OperationalError:
            mensaje = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()

        return mensaje

    def eliminardeuda(self, cedula):
        ''' modifica nombre y correo por el numero de cedula '''
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()

            argumentos = (cedula)

            sql ="""
            UPDATE Usuario SET deuda=0 WHERE cedula=(?)
            """

            if(cur.execute(sql, (argumentos,))): mensaje="El usuario se le elimino la deuda correctamente"
            else:mensaje=" No se le pudo eliminar la deuda del usuario"
 
        except sqlite3.OperationalError:
            mensaje = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()

        return mensaje


    def eliminarusuario(self, cedula):
        ''' Elimina usuario por cedula'''
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()

            argumentos = (cedula)

            sql ="""
            DELETE FROM Usuario WHERE cedula=(?)
            """

            if(cur.execute(sql, (argumentos,))): mensaje="El usuario fue eliminado correctamente"
            else:mensaje="el usuario no pudo ser eliminado"
 
        except sqlite3.OperationalError:
            mensaje = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()

        return mensaje    


    def existeusuario(self, cedula):
        ''' consulta si existe un usuario retorna 1 existe, retorna 0 no existe simple bro '''
        try:
            conecta = Conector()
            conexion = conecta.crearConexion()
            cur = conexion.cursor()


            argumentos = ( cedula)

            sql = """
            SELECT numero FROM usuario WHERE cedula=(?)
            """
            cur.execute(sql, (argumentos,))

            data =cur.fetchone()

            if(data==None): 
                val=0
            else: 
                val=1  

        except sqlite3.OperationalError:
            respuesta = "Error operacional sobre la base de datos"

        finally:
            cur.close()
            conexion.commit()
            conexion.close()

        return val     