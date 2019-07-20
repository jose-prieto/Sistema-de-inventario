class CRUD_producto(object):

        
    def insertarproducto(self, producto,conn):
        # Inserta un nuevo usuario en la base de datos a partir de una conecion y un objeto usuario
        sql = ''' INSERT INTO productos(departamento,nombre,cantidad,cantidadminima,retornable)
              VALUES(?,?,?,?,?); ''' 
        c = conn.cursor()
        c.execute(sql, producto)
        conn.commit()
        c.close()
        conn.close()