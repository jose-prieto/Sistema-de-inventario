import sys

from crearbase import *
from CRUD_Usuario import *
from Conector import *
from CRUD_productos import *


def Script():

    crearBase()
    prueba = CRUD_Usuario()
    conn = Conector()


    #creando la base de datos Usuarios
    usuarios = [["Daren Gonzalez","25545624","daren1997gonzalez@gmail.com","1","Administrador","pass"] ,["Bryan Rodriguez","2","bryrodri1@gmail.com","2","Administrador","pass1"],["Omar Perez","3","oaperezr.18@est.ucab.edu.ve","3","Operador","pass3"],["Jose Prieto","24217857","jap25o94@gmail.com","4","Operador","pass4"],["Fernando Martinez","5","fmartinezr195@gmail.com","5","Gerente","pass5"],["Johadson Mijares","6","correo","6","Gerente","pass6"]]
    for usuario in usuarios:
        print(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5])
        prueba.insertarUsuario(usuario,conn.crearConexion()) 
    productos = []


    ###Laminas de acrilico
    productos.append(["Laminas de acrilico","Acrilico 3mm (1.22 x 2.44)",426,5,0])
    productos.append(["Laminas de acrilico","Acrilico 5mm (1.52 x 3.05)",14,5,0])
    productos.append(["Laminas de acrilico","Acrilico 5mm (1.22 x 2.44)",40,5,0])
    productos.append(["Laminas de acrilico","Blanca 4mm Goma (1.22 x 2.44)",29,5,0])
    productos.append(["Laminas de acrilico","Blanca 3mm (1.22 x 2.44)",15,5,0])
    productos.append(["Laminas de acrilico","Acrilico 400 (1.22 x 1.83)",44,5,0])
    productos.append(["Laminas de acrilico","Roja 3mm (1.22 x 2.44)",27,5,0])
    productos.append(["Laminas de acrilico","Poliacril 3mm (1.22x 2.44)",30,5,0])
    productos.append(["Laminas de acrilico","Goma 5mm (1.22 x 2.44)",13,5,0])
    productos.append(["Laminas de acrilico","Acrilico 5mm (1.83 x 1.83)",6,5,0])
    productos.append(["Laminas de acrilico","Acrilico 3mm (1.22 x 2.44",60,5,0])
    productos.append(["Laminas de acrilico","Goma 5mm (1.22x 1.52)",24,5,0])
    productos.append(["Laminas de acrilico","MDF 3mm",7,3,0])
    productos.append(["Laminas de acrilico","MDF 15mm",12,3,0])
    productos.append(["Laminas de acrilico","PVC 3mm",24,6,0])
    productos.append(["Laminas de acrilico","PVC 4mm Sintetica",42,6,0])
    productos.append(["Laminas de acrilico","PVC 4 mm",89,6,0])
    productos.append(["Laminas de acrilico","PVC 5mm",3,1,0])
    productos.append(["Laminas de acrilico","Formica",10,3,0])
    productos.append(["Laminas de acrilico","Laminas de corcho",5,1,0])
    ###Laminas de acrilico

    ###Laminas de metal
    productos.append(["Laminas de metal","Aluminio (0.30 o 0.50mm)",225,10,0])
    productos.append(["Laminas de metal","Aluminio 1mm",135,10,0])
    productos.append(["Laminas de metal","Aluminio 1.3mm",348,10,0])
    productos.append(["Laminas de metal","Aluminio 1.6mm",380,10,0])
    productos.append(["Laminas de metal","Aluminio 2mm",50,10,0])
    productos.append(["Laminas de metal","Acero (18 o 0.90mm)(1.22 x 2.44)",0,2,0])
    productos.append(["Laminas de metal","Acero (20 o 1mm)(1.22 x 2.44)",16,4,0])
    productos.append(["Laminas de metal","Acero (22 o 0.80mm)(1.22 x 2.44)",29,4,0])
    productos.append(["Laminas de metal","Acero (24 o 0.60mm)(1.22 x 2.44)",26,4,0])
    productos.append(["Laminas de metal","Galvanizadas (22 o 0.80mm)(1.22 x 2.44)",80,4,0])
    productos.append(["Laminas de metal","Galvanizadas (24 o 0.60mm)(1.22 x 2.44)",10,4,0])
    productos.append(["Laminas de metal","Galvanizadas 22",26,5,0])
    ###Laminas de metal

    ###Tubos de Aluminio
    productos.append(["Tubos de Aluminio","Aluminio 1x1",5263,1000,1])
    productos.append(["Tubos de Aluminio","Aluminio 1 x 1/2",555,50,1])
    productos.append(["Tubos de Aluminio","Aluminio 11/2 x 3/4",1015,100,1])
    productos.append(["Tubos de Aluminio","Aluminio 2x1",158,10,1])
    productos.append(["Tubos de Aluminio","Alumino 1/2x1/2",604,100,1])
    productos.append(["Tubos de Aluminio","Aluminio 2x2",40,10,1])
    productos.append(["Tubos de Aluminio","Aluminio 3/4x3/4",600,100,1])
    productos.append(["Tubos de Aluminio","Aluminio Pendon 3/8",10,1,1])
    productos.append(["Tubos de Aluminio","Aluminio con aleta 1x1",729,100,1])
    productos.append(["Tubos de Aluminio",'Aluminio pletinas 1"',7,2,1])
    productos.append(["Tubos de Aluminio",'Aluminio Pletinas 2"',11,2,1])
    productos.append(["Tubos de Aluminio","Aluminio Angulos 1x1",102,10,1])
    productos.append(["Tubos de Aluminio",'Aluminio Angulos 2"',8,2,1])
    ###Tubos de aluminio

    
    ###Tubos de hierro
    productos.append(["Tubos de hierro","Hierro 1x1",4,1,1])
    productos.append(["Tubos de hierro","Hierro 2x2",0,0,1])
    productos.append(["Tubos de hierro","Hierro 2x1",0,0,1])
    productos.append(["Tubos de hierro","Hierro 3x1 1/2",2,1,1])
    productos.append(["Tubos de hierro","Hierro 3x1",2,1,1])
    productos.append(["Tubos de hierro","Hierro 3x3",12,5,1])
    productos.append(["Tubos de hierro","Hierro 4x4",10,2,1])
    productos.append(["Tubos de hierro","Angulo Hierro 1x1",0,0,1])
    productos.append(["Tubos de hierro",'Angulo Hierro 4"',25,5,1])
    productos.append(["Tubos de hierro",'Redondos de hierro 1 1/2"',26,5,1])
    productos.append(["Tubos de hierro",'Pletina 2"',10,2,1])
    ###Tubos de hierro


    ###Inventario internas
    
    productos.append(["Inventario de Internas","Alicate boca pato",6,2,1])
    productos.append(["Inventario de Internas","Alicate de Electricidad",2,1,1])
    productos.append(["Inventario de Internas","Alicate de Gancho",1,0,1])
    productos.append(["Inventario de Internas","Alicate de presion",1,1,1])
    productos.append(["Inventario de Internas","Cepillos de alambre",1,1,1])
    productos.append(["Inventario de Internas","Cincel de pala",2,1,1])
    productos.append(["Inventario de Internas","Cincel de punta",3,1,1])
    productos.append(["Inventario de Internas","Destornillador de copa",6,1,1])
    productos.append(["Inventario de Internas","Destornillador de estrella",3,1,1])
    productos.append(["Inventario de Internas","Destornillador de estria",5,1,1])
    productos.append(["Inventario de Internas","Destonillador de pala",2,1,1])
    productos.append(["Inventario de Internas","Equpos de soldar",2,1,1])
    productos.append(["Inventario de Internas","Juego de llaves L",2,1,1])
    productos.append(["Inventario de Internas","Llaves ajustables",10,2,1])
    productos.append(["Inventario de Internas","Llaves de tubo",3,1,1])
    productos.append(["Inventario de Internas","Machetes",2,1,1])
    productos.append(["Inventario de Internas","Mandarrias",2,1,1])
    productos.append(["Inventario de Internas","Marco de ceguetas",0,1,1])
    productos.append(["Inventario de Internas","Martillos de goma",5,2,1])
    productos.append(["Inventario de Internas","Martillos de metal",6,2,1])
    productos.append(["Inventario de Internas","Niveles",4,2,1])
    productos.append(["Inventario de Internas","Pinzas para electricidad",2,1,1])
    productos.append(["Inventario de Internas","Piquetas",6,2,1])
    productos.append(["Inventario de Internas","Tijeras de corte grande",3,1,1])
    productos.append(["Inventario de Internas","Tijera roja",4,1,1])
    productos.append(["Inventario de Internas","Tijeras verdes",4,1,1])
    productos.append(["Inventario de Internas","Tenazas",1,1,1])
    productos.append(["Inventario de Internas","Escaleras Grandes",10,2,1])
    productos.append(["Inventario de Internas","Escaleras pequeñas",7,2,1])
    productos.append(["Inventario de Internas","Extintores",8,2,1])
    productos.append(["Inventario de Internas","Gato naranja",3,1,1])
    productos.append(["Inventario de Internas","Gato negro pequeño",1,1,1])
    productos.append(["Inventario de Internas","Gato rojo grande",2,1,1])
    productos.append(["Inventario de Internas","Gato rojo pequeño",1,1,1])
    productos.append(["Inventario de Internas","Juego de llaves para ambiar cauchos",4,1,1])
    productos.append(["Inventario de Internas","Llave de camion",2,1,1])
    productos.append(["Inventario de Internas","Niveladores Grandes",8,2,1])
    productos.append(["Inventario de Internas","Niveladores pequeños",30,3,1])
    productos.append(["Inventario de Internas","pistola de silicon caliente",4,1,1])
    productos.append(["Inventario de Internas","Pistolas de silicon frio",22,2,1])
    productos.append(["Inventario de Internas","triangulos randes",5,2,1])
    productos.append(["Inventario de Internas","Trinagulos pequeños",3,1,1])
    productos.append(["Inventario de Internas","Barras para subir los gatos",3,1,1])
    productos.append(["Inventario de Internas","Cables auxiliares",1,1,1])
    productos.append(["Inventario de Internas","Caladora",0,0,1])
    productos.append(["Inventario de Internas","Cierra orbital",2,1,1])
    productos.append(["Inventario de Internas","Esmeril Grande",2,1,1])
    productos.append(["Inventario de Internas","Esmeril Pequeño",3,1,1])
    productos.append(["Inventario de Internas","Grapadora Neumatica",2,1,1])
    productos.append(["Inventario de Internas","Pistola de calor",3,1,1])
    productos.append(["Inventario de Internas","Remachadora manual",1,1,1])
    productos.append(["Inventario de Internas","Remachadora Neumatica",6,1,1])
    productos.append(["Inventario de Internas","Taladors 3/8",4,1,1])
    productos.append(["Inventario de Internas","Taladro de apreatar tornillos",1,1,1])
    productos.append(["Inventario de Internas","Taladors percutores",6,1,1])
    productos.append(["Inventario de Internas","Taladro inalambrico",2,1,1])
    productos.append(["Inventario de Internas","Trompo Pequeño",1,1,1])
    productos.append(["Inventario de Internas","Tirro de papel",44,10,0])
    productos.append(["Inventario de Internas","Silicon frio",12,6,1])
    productos.append(["Inventario de Internas","Bolsas",1345,100,0])
    productos.append(["Inventario de Internas","Silicon caliente",31,10,0])
    productos.append(["Inventario de Internas","Morropa 7 caja",504,10,1])
    productos.append(["Inventario de Internas","Tirras (paquete)",700,100,0])
    productos.append(["Inventario de Internas","Tapa boca",100,10,1])
    productos.append(["Inventario de Internas","Teipe negro",3,1,1])
    productos.append(["Inventario de Internas","Lentes de seguridad",5,1,1])
    productos.append(["Inventario de Internas","Mecha de hierro 3/16",30,10,1])
    productos.append(["Inventario de Internas","Mecha de Hierro 3/8",20,2,1])
    productos.append(["Inventario de Internas","Mecha de hierro 5/16",9,1,1])
    productos.append(["Inventario de Internas","Mecha de hierro 1/4",28,2,1])
    productos.append(["Inventario de Internas","Mecha de hierro 1/8",63,2,1])
    productos.append(["Inventario de Internas","Mecha de hierro 1/2",16,2,1])
    productos.append(["Inventario de Internas","Mecha de concreto 1/2",14,2,1])
    productos.append(["Inventario de Internas","Mecha de concreto 7/16",14,1,1])
    productos.append(["Inventario de Internas","Mecha de concreto 5/16",13,1,1])
    productos.append(["Inventario de Internas","Mecha de concreto 3/8",5,1,1])
    productos.append(["Inventario de Internas","Mecha de concreto 1/4",1,1,1])
    productos.append(["Inventario de Internas","Mecha de concreto 9/16",7,2,1])
    productos.append(["Inventario de Internas","Mecha de concreto 3/16",1,1,1])
    ###Inventario de internas


    ###Vinil
    
    productos.append(["Vinil","Laminado Matte 8520",5,1,0])
    productos.append(["Vinil","Protective clear 8914",3,1,0])
    productos.append(["Vinil","Azul 3M (1.30mts)",1,1,0])
    productos.append(["Vinil","Blanco 3M",14,1,0])
    productos.append(["Vinil","Arlon azul (1.37 x 50mts)",8,2,0])
    productos.append(["Vinil","Arlon azul (1.30mts)",1,1,0])
    productos.append(["Vinil","Arlon blanco Brillante (1.37 x 45mts)",1,1,0])
    productos.append(["Vinil","Arlon Blanco Brillante (1.50 x 50mts)",3,1,0])
    productos.append(["Vinil","Arlon Laminado Brillante (0.70 x 45Mts)",64,2,0])
    productos.append(["Vinil","Arlon Laminado Matte (0.70 x 45Mts)",20,2,0])
    productos.append(["Vinil","Arlon Negro (0.70 x 45MTs)",1,1,0])
    productos.append(["Vinil","Arlon Rojo (1.37 x 50Mts)",10,1,0])
    productos.append(["Vinil","Arlon Verde (1.30Mts)",1,1,0])
    productos.append(["Vinil","CartonGraf Blanco Brillante (1.97 x 50Mts)",16,2,0])
    productos.append(["Vinil","CartonGraf Blanco Brillante (1.37 x 50Mts)",1,1,0])
    productos.append(["Vinil","CartonGraf clear (1.37 x 5Mts)",1,1,0])
    productos.append(["Vinil","CartonGraf Clear Matte (1.37 x 50Mts)",1,1,0])
    productos.append(["Vinil","Focus clear",1,1,0])
    productos.append(["Vinil","Mactac Clear Brillante (1.37 x 50Mts)",1,1,0])
    productos.append(["Vinil","Ritrama Blanco",0,0,0])
    productos.append(["Vinil","Ritrama Blanco Matte",2,1,0])
    productos.append(["Vinil","RItrama Clear (1.37 x 50Mts)",0,0,0])
    productos.append(["Vinil","BlacklinFilm",16,2,0])
    productos.append(["Vinil","Chino Esmerilado",1,1,0])
    productos.append(["Vinil","LG Esmerilado",23,2,0])
    productos.append(["Vinil","Flooring",1,1,0])
    productos.append(["Vinil","3M Microperforado (1.37 x 50Mts)", 8,1,0]) 
    productos.append(["Vinil","Microperforado",1,1,0])
    productos.append(["Vinil","Nuevo Microperforado (1.37 x 50Mts)",6,1,0])
    productos.append(["Vinil","One sign Microperforado (1.52 x 50Mts)",11,1,0])
    productos.append(["Vinil","Papel Ahumado",2,1,0])
    productos.append(["Vinil","Envision(especial)",1,1,0])
    productos.append(["Vinil","Transfer",12,1,0])
    productos.append(["Vinil","Econo Blanco Pega gris (1.37 x 45Mts)",1,1,0])
    productos.append(["Vinil","Banesco Vinil de Cebefa de puntos (P20-90)",8,1,0])
    productos.append(["Vinil","Banesco Vinil de Cebefa de puntos (P20-30 rollos)",3,1,0])
    productos.append(["Vinil","Banesco Vinil de cenefa de puntos (P20-75 caja)",2,1,0])
    productos.append(["Vinil","LG Vinil clear brillante (1.52 x 45.72Mts)",24,5,0])
    productos.append(["Vinil","LG Vinil Laminado Matte (1.52 x 45.72Mts)",10,1,0])
    productos.append(["Vinil","LG Vinil Laminado Matte (1.37 x 45.72Mts)",10,1,0])
    ###Vinil



    ###Departamento de letra
    
    productos.append(["Departamento de Letra","Braso",23,5,1])
    productos.append(["Departamento de Letra","Fuller Acero - Brill",3,1,1])
    productos.append(["Departamento de Letra","Acido Muriatico",4,2,0])
    productos.append(["Departamento de Letra","Bolsa Algodon",4,1,0])
    productos.append(["Departamento de Letra","Cautin",38,5,1])
    productos.append(["Departamento de Letra","estaño",800,100,0])
    productos.append(["Departamento de Letra","Limas 1/2 caña",7,2,0])
    productos.append(["Departamento de Letra","Balatex",7,1,0])
    productos.append(["Departamento de Letra","Limas rabo raton",3,1,0])
    productos.append(["Departamento de Letra","Lijas para Lijadora Grande",6,2,0])
    productos.append(["Departamento de Letra","Disco para pulir pequeño",6,1,0])
    productos.append(["Departamento de Letra","Disco para pulir grande",4,1,0])
    productos.append(["Departamento de Letra","pasta para pulir",64,10,0])
    ###Departamento de letra


    ###Departamento de herreria
    
    productos.append(["Departamento de Herreria","Disco de corte 4-1/2 x 1/4 x 7/8",44,5,0])
    productos.append(["Departamento de Herreria","Disco de corte 7-x 1/4x7/8",40,5,0])
    productos.append(["Departamento de Herreria","Disco de corte 4-1/2x1/8x7/80",37,5,0])
    productos.append(["Departamento de Herreria","Disco de corte Grande",3,1,0])
    productos.append(["Departamento de Herreria","Disco de corte piedra",2,1,0])
    productos.append(["Departamento de Herreria","Caretas para soldar",4,1,1])
    productos.append(["Departamento de Herreria","peto",6,1,1])
    productos.append(["Departamento de Herreria","Guantes de carnaza",19,5,1])
    productos.append(["Departamento de Herreria","Alambre para soldar caja",8,2,0])
    productos.append(["Departamento de Herreria","Electrodos finos caja",2,1,0])
    productos.append(["Departamento de Herreria","Electrodos Gruesos caja",1,1,0])
    productos.append(["Departamento de Herreria","Caretas para soldar pequeña",18,5,1])
    productos.append(["Departamento de Herreria","Escuadras",3,1,1])
    productos.append(["Departamento de Herreria",'Disco de corte 14"',3,1,0])
    productos.append(["Departamento de Herreria",'Disco de corte 7"x1/8"x7/8"',30,0,0])
    ###Deartamento de herreria


    ###Departamento de pintura

    
    productos.append(["Departamento de Pintura","B.V rojo",17,5,0])
    productos.append(["Departamento de Pintura","Extintor Rojo",1,0,0])
    productos.append(["Departamento de Pintura","Vinotinto",1,1,0])
    productos.append(["Departamento de Pintura","Banco Agricola Verde Oscuro",5,1,0])
    productos.append(["Departamento de Pintura","B.N.C Verde",1,1,0])
    productos.append(["Departamento de Pintura","Blanco brillante",0,1,0])
    productos.append(["Departamento de Pintura","Blanco Acrilico",2,1,0])
    productos.append(["Departamento de Pintura","Blanco Sierra",1,0,0])
    productos.append(["Departamento de Pintura","Blanco Matte satinado",1,1,0])
    productos.append(["Departamento de Pintura","Negro brillante",1,1,0])
    productos.append(["Departamento de Pintura","Negro Acrilico",2,1,0])
    productos.append(["Departamento de Pintura","Negro esmalte",1,1,0])
    productos.append(["Departamento de Pintura","B.N.C Azul",4,1,0])
    productos.append(["Departamento de Pintura","Acrilico 100 banco azul",1,1,0])
    productos.append(["Departamento de Pintura","Acrilico gris",5,1,0])
    productos.append(["Departamento de Pintura","Esmalte gris",6,1,0])
    productos.append(["Departamento de Pintura","Trafico amarillo",0,1,0])
    productos.append(["Departamento de Pintura","B.N.C Naranja",1,1,0])
    productos.append(["Departamento de Pintura","Olivio",3,1,0])
    productos.append(["Departamento de Pintura","Caroni Marron",6,1,0])
    productos.append(["Departamento de Pintura","B.V Caucho matte exterior",1,1,0])
    productos.append(["Departamento de Pintura","Alfa beige",0,1,0])
    productos.append(["Departamento de Pintura","Pare Pare cuñe blanco",10,1,0])
    productos.append(["Departamento de Pintura","Fondos acrilicos",49,10,0])
    productos.append(["Departamento de Pintura","Herreria Fondo antocorrosivo",2,1,0])
    productos.append(["Departamento de Pintura","Aluminio fino",9,1,0])
    productos.append(["Departamento de Pintura","Esmalte aluminio fino",8,2,0])
    productos.append(["Departamento de Pintura","Micro flex",4,1,0])
    productos.append(["Departamento de Pintura","Masilla roja",16,1,0])
    productos.append(["Departamento de Pintura","Removedor",1,1,0])
    productos.append(["Departamento de Pintura","High Tech + Activador",4,1,0])
    productos.append(["Departamento de Pintura","Vox Premier+ Activador",9,1,0])
    productos.append(["Departamento de Pintura","Sellador Madera",4,1,0])
    productos.append(["Departamento de Pintura","Transparente",1,1,0])
    productos.append(["Departamento de Pintura","Pega amarilla cuñete",2,1,0])
    productos.append(["Departamento de Pintura","Pega blanca",1,1,0])
    productos.append(["Departamento de Pintura","Masilla para pared",10,1,0])
    productos.append(["Departamento de Pintura","Coladores",300,1,0])
    productos.append(["Departamento de Pintura","Brochas",3,1,1])
    productos.append(["Departamento de Pintura","Rodillos",15,4,1])
    productos.append(["Departamento de Pintura","Camisas para rosillos",32,5,1])
    productos.append(["Departamento de Pintura","Bandejas",4,1,1])
    productos.append(["Departamento de Pintura","Lijas 120",81,5,0])
    productos.append(["Departamento de Pintura","Lijas 180",70,5,0])
    productos.append(["Departamento de Pintura","Lijas 240",175,5,0])
    productos.append(["Departamento de Pintura","Lijas 80",100,5,0])
    productos.append(["Departamento de Pintura","Lijas 400",230,5,0])
    productos.append(["Departamento de Pintura","Thinner",37,4,0])
    productos.append(["Departamento de Pintura","Pistola de pintura",0,1,1])
    productos.append(["Departamento de Pintura","Bandejas platinadas",2,1,1])
    productos.append(["Departamento de Pintura","Camisas de rodillas blancas 3/8",9,1,1])
    productos.append(["Departamento de Pintura","Paletas para mover pintura",9,1,1])
    productos.append(["Departamento de Pintura","Activador de pintura para el piso",7,1,1])
    ###Departamento de pintura



    ###Inventario de carro
    
    productos.append(["Inventario de Carro","Cauchos Goddiyer",4,1,0])
    productos.append(["Inventario de Carro","Cauchos Grabber AT",4,1,0])
    productos.append(["Inventario de Carro","Cauchos Destination",2,1,0])
    productos.append(["Inventario de Carro","Cauchos Aventure AT",2,1,0])
    productos.append(["Inventario de Carro","Cauchos Goodiyer",1,1,0])
    productos.append(["Inventario de Carro","Cauchos Goodiyer",6,1,0])
    productos.append(["Inventario de Carro","Cauchos Safeway",2,1,0])
    productos.append(["Inventario de Carro","Cauchos Kumbo",2,1,0])
    productos.append(["Inventario de Carro","Cauchos Moto",1,1,0])
    productos.append(["Inventario de Carro","Cauchos Sr Orlando",4,1,0])
    productos.append(["Inventario de Carro","Cauchos Sr Celeste",4,1,0])
    productos.append(["Inventario de Carro","Bandas",20,2,0])
    productos.append(["Inventario de Carro","Coliendro Xtender",0,1,0])
    productos.append(["Inventario de Carro","Pastillos Delco Durastop",5,1,0])
    productos.append(["Inventario de Carro","Pastillas ACD-310-GG-B14",1,1,0])
    productos.append(["Inventario de Carro","Pastillas ACDELCO",6,1,0])
    productos.append(["Inventario de Carro","Pastillas Murusi",1,1,0])
    productos.append(["Inventario de Carro","pastillas American Brake",4,1,0])
    productos.append(["Inventario de Carro","Mosos TSR",2,1,0])
    productos.append(["Inventario de Carro","Mosos PPA",1,1,0])
    productos.append(["Inventario de Carro","Mosos Primer Choise",3,1,0])
    productos.append(["Inventario de Carro","Filtros ACDELCO",11,2,0])
    productos.append(["Inventario de Carro","Filtros Isuzu",13,2,0])
    productos.append(["Inventario de Carro","Filtros Isuzu Tokio",5,1,0])
    productos.append(["Inventario de Carro","Filtros WEB",1,1,0])
    productos.append(["Inventario de Carro","Amortiguadores Equipped",4,1,0])
    productos.append(["Inventario de Carro","Aceite de transmision Venoco",6,1,0])
    productos.append(["Inventario de Carro","Carambas SQ",8,1,0])
    productos.append(["Inventario de Carro","Liga para freno Venusa",0,1,0])
    productos.append(["Inventario de Carro","Aceite de transmision Marca Diferente",3,1,000])
    ####Inventario carro



    ###Inventario tornillos
    
    productos.append(["Inventario de Tornillos","Tornillos Broca 3/4",1300,100,0])
    productos.append(["Inventario de Tornillos","Tornillos Broca 8*1/2",5304,100,0])
    productos.append(["Inventario de Tornillos","Tornillos Chupeta 1/2",110,10,0])
    productos.append(["Inventario de Tornillos","Teld Bold",1046,100,0])
    productos.append(["Inventario de Tornillos",'Tornillos Broca 1"',700,100,0])
    productos.append(["Inventario de Tornillos","Tornillos Cabeza plana 8x1/5",2300,100,0])
    productos.append(["Inventario de Tornillos",'Tornillos exagonales 2"',370,100,0])
    productos.append(["Inventario de Tornillos","Tornillos 3/16x1",2300,100,0])
    productos.append(["Inventario de Tornillos","Tornillos 3/16 x 1/2",1400,100,0])
    productos.append(["Inventario de Tornillos","Tuercas 3/16",5000,100,0])
    productos.append(["Inventario de Tornillos","Tuercas 1/2",900,100,0])
    productos.append(["Inventario de Tornillos","Tuercas 1/4",1500,100,0])
    productos.append(["Inventario de Tornillos","Ramplus 1/4",1500,100,0])
    productos.append(["Inventario de Tornillos","Ramplus 3/16",600,100,0])
    productos.append(["Inventario de Tornillos","Ramplus 5/16",1870,100,0])
    productos.append(["Inventario de Tornillos","Ramplus de Drywall",894,100,0])
    productos.append(["Inventario de Tornillos","Ramplus de verde",2350,100,0])
    ###Inventario Tornillos

    creador = CRUD_producto()

    for producto in productos:
        print(producto)
        creador.insertarproducto(producto,conn.crearConexion())



if __name__ == '__main__':
    Script()