class CRUD_reporte_prestamo(object):
    
     
    def crearTablaReporte(self, conn):
        c = conn.cursor()              
        comando = """ CREATE TABLE IF NOT EXISTS ReportePrestamo (
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
        c.execute(comando)
        conn.commit()
        c.close()
        conn.close()
    
    def insertarReporte(self, usuario,reporte,conn,id_usuario):
        #Crea un nuevo reporte de prestamo el cual se asocial id de un usuario dado
        sql = ''' INSERT INTO ReportePrestamo(persona_a_quien_se_le_presto,fecha_prestamo,hora_prestamo,motivo,fecha_devolucion,hora_devolucion,estado_prestamo,usuario_id)
                  VALUES("%s","%s","%s","%s","%s","%s",%i,%i); ''' %(usuario.nombre,reporte.fecha_prestamo,reporte.hora_prestamo,reporte.motivo_prestamo,reporte.fecha_devolucion,reporte.hora_devolucion,reporte.estado_prestamo,id_usuario)
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close();
        pass
    
    def mostrarTodo(self,conn):
        #Muestra todos los elementos de la tabla de Reportes
        cur = conn.cursor()
        cur.execute("SELECT * FROM ReportePrestamo")
 
        rows = cur.fetchall()
 
        for row in rows:
            print(row)
            
    def cerrarReporte(self, usuario,reporte,conn,id_usuario):
        pass
    
    def obtenerId(self,id_usuario,reporte,conn):
        cur = conn.cursor()
        #sql ="SELECT id FROM ReportePrestamo WHERE (usuario_id = %i AND fecha_prestamo = '%s' AND hora_prestamo = '%s' );" %(usuario.nombre,usuario.cedula)
        #cur.execute(sql)
        return (cur.fetchone()[0])
    
    def prestamos_activos_de_un_usuario(self,usuario_id,conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM ReportePrestamo WHERE (usuario_id = %i AND estado_prestamo = 1") %(usuario_id) 
        rows = cur.fetchall() 
        for row in rows:
            print(row)