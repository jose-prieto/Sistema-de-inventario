import sqlite3

class Conector(object):
        
    def crearConexion(self):

        conn = sqlite3.connect("../db/Depot.db")
        return conn

        
    