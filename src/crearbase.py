import sqlite3
from Conector import *

class crearBase(object):
    conexion = Conector()
    conn = conexion.crearConexion()
    c=conn.cursor()

    def __init__(self):
        Usuario(self)
        productos(self)
        modificacion(self)
        prestamod(self)
        prestamosolo(self)
        productoEnPrestamo(self)
        desconectar(self)


def productos(self):
    sql = """CREATE TABLE IF NOT EXISTS productos(
                                        idproductos INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                        departamento text NOT NULL,
                                        nombre text NOT NULL,
                                        cantidad INTEGER NULL,
                                        cantidadminima INTEGER NOT NULL,
                                        retornable INTEGER NOT NULL
    );"""
    if(self.c.execute(sql)):
        print("se creo correctamente productos")
    else:
        print(" ocurrio un error")

def modificacion(self):   
    sql = """CREATE TABLE IF NOT EXISTS modificacion(
                                        idmodificacion INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                        usuario text NOT NULL,
                                        producto text NOT NULL,
                                        tipo INTEGER NOT NULL,
                                        fecha datetime(3) NOT NULL
    );"""
    if(self.c.execute(sql)):print("se creo correctamente modificacion")
    else:print(" ocurrio un error")

def prestamod(self):
    #tabla que cpnsidero deberia ser eliminada queda en observacion todo se pueda manejar desde reporte prestamo, solo nos causa mas complejidad en el programa
    sql = """CREATE TABLE IF NOT EXISTS prestamodevolucion(
                                         idprestamodevolucion INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                         usuario text NOT NULL,
                                         producto text NOT NULL,
                                         cantidad INTEGER NOT NULL,
                                         fechadevuelto datetime(3) NOT NULL
    );"""
    if (self.c.execute(sql)):
        print("se creo correctamente PRESTAMO DEVOLUCION")
    else:

        print(" ocurrio un error")   
            

def prestamosolo(self):
    sql = """ CREATE TABLE IF NOT EXISTS ReportePrestamo (
                                        id integer PRIMARY KEY,
                                        persona_a_quien_se_le_presto text NO NULL,
                                        fecha_prestamo text NOT NULL,
                                        hora_prestamo text NOT NULL,
                                        motivo text NOT NULL,
                                        fecha_devolucion text,
                                        hora_devolucion text,
                                        estado_prestamo integer NOT NULL,
                                        usuario_id int,
                                        FOREIGN KEY (usuario_id) REFERENCES Usuario (id)); """ 
    if(self.c.execute(sql)):print("se creo correctamente Reporte prestamo")
    else:print(" ocurrio un error") 

def productoEnPrestamo(self):
    sql = """ CREATE TABLE IF NOT EXISTS ProductoPrestado (
                                        id integer PRIMARY KEY,
                                        nombre_producto text NO NULL,
                                        cantidad int NOT NULL,
                                        retornable int NOT NULL,
                                        prestamo_id int,
                                        FOREIGN KEY (prestamo_id) REFERENCES ReportePrestamo (id));"""
    if(self.c.execute(sql)):print("se creo correctamente producto prestado")
    else:print(" ocurrio un error") 

def Usuario(self):
    sql = """ CREATE TABLE IF NOT EXISTS Usuario (
                                        id INTEGER PRIMARY KEY,
                                        nombre text NOT NULL,
                                        cedula text NOT NULL,
                                        mail text NOT NULL,
                                        numero text NOT NULL,
                                        cargo text  NOT NULL,
                                        password text NOT NULL,
                                        deuda int default 0); """
    if(self.c.execute(sql)):print("se creo correctamente Usuario")
    else:print(" ocurrio un error")    

def desconectar(self):
    self.conn.commit()
    self.c.close()
    self.conn.close()