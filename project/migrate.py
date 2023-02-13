import sqlite3
import requests
import json

conn=sqlite3.connect('tienda.db')
"""
def creart():

    cursor_obj = conn.cursor()
    cursor_obj.execute("DROP TABLE IF EXISTS USUARIOS")
    table = CREATE TABLE USUARIOS 
               (ID  INTEGER PRIMARY KEY AUTOINCREMENT,
                USUARIO VARCHAR(25),
                PASSWORD VARCHAR(255) NOT NULL,
                EMAIL VARCHAR(255) NOT NULL,
                FULLNAME VARCHAR(25) NOT NULL,
                SCORE INT,
                TIPOUSUARIO VARCHAR(25)
                ); 
    cursor_obj.execute(table)
    cursor_obj.execute("DROP TABLE IF EXISTS PRODUCTOS")
    table = CREATE TABLE PRODUCTOS 
               (ID  INTEGER PRIMARY KEY ,
                NAMEPRODUCT VARCHAR(255) NOT NULL,
                PRICE MONEY NOT NULL, 
                CATEGORIA VARCHAR(25) NOT NULL,
                NRO_SERIE VARCHAR(25) NOT NULL,
                PRODUCTO VARCHAR(25) NOT NULL,
                STOCKACTUAL INT,
                CREACTION_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UPDATE_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ); 
    cursor_obj.execute(table)
    cursor_obj.execute("DROP TABLE IF EXISTS INVENTARIO")

    table=CREATE TABLE INVENTARIO 
             (IDMOVIMIENTO  INTEGER PRIMARY KEY AUTOINCREMENT,
              CANTIDAD INT NOT NULL,
              FECHA_MOVIMIENTO TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              PRODUCTOID INT ,
              CONSTRAINT fk_PRODUCTOS FOREIGN KEY (PRODUCTOID) REFERENCES PRODUCTOS (ID)
              ) 
    cursor_obj.execute(table)
    cursor_obj.execute("DROP TABLE IF EXISTS TIPCAMBIO")

    table=CREATE TABLE TIPCAMBIO 
             (IDTC  INTEGER PRIMARY KEY AUTOINCREMENT,
              COMPRA FLOAT NOT NULL,
              VENTA FLOAT NOT NULL, 
              ORIGEN VARCHAR(25) NOT NULL,
              MONEDA VARCHAR(25) NOT NULL,
              FECHA TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              )
    cursor_obj.execute(table)

    cursor_obj.execute("DROP TABLE IF EXISTS VENTA")

    table=CREATE TABLE VENTA 
             (VENTAID  INTEGER PRIMARY KEY AUTOINCREMENT,

              PRODUCTOID INT ,
              ORDERID INT ,
              USUARIOSID INT ,
              TCID INT ,
              PRICETOTAL FLOAT ,
              CONSTRAINT fk_PRODUCTOS FOREIGN KEY (PRODUCTOID) REFERENCES PRODUCTOS (ID),
              CONSTRAINT fk_INVENTARIO FOREIGN KEY (ORDERID) REFERENCES INVENTARIO (IDMOVIMIENTO),
              CONSTRAINT fk_USUARIOS FOREIGN KEY (USUARIOSID) REFERENCES USUARIOS (ID),
              CONSTRAINT fk_TIPCAMBIO FOREIGN KEY (TCID) REFERENCES TIPCAMBIO (IDTC)
              ) 

    cursor_obj.execute(table)
    conn.close()
"""
"""
    table=ALTER TABLE PRODUCTOS ALTER COLUMN ID INT NOT NULL AUTOINCREMENT(60) PRIMARY KEY;
             ALTER TABLE INVENTARIO ALTER COLUMN IDMOVIMIENTO INT NOT NULL AUTOINCREMENT(60) PRIMARY KEY;
             ALTER TABLE TIPCAMBIO ALTER COLUMN IDTC INT NOT NULL AUTOINCREMENT(60) PRIMARY KEY;
             ALTER TABLE VENTA ALTER COLUMN VENTAID INT NOT NULL AUTOINCREMENT(60) PRIMARY KEY;
             
    cursor_obj.execute(table)
    conn.close()
"""
# comentamos las insercciones ya que solo sera parte de la creacion de tablas
"""insert =" INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES('admin','admin','admin@datux.com','admin datux',0,'admin')"

conn.execute(insert)
insert =" INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES('cliente','cliente','email','cliente',0,'cliente')"
conn.execute(insert)


print("Table is Ready")
"""
def ingresard():
    #API TIPO DE CAMBIO SUNAT
    te=[]
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    re=requests.get(url)
    t=re.json()
    te=list(t.values())
    #####
    print("\n<<<USUARIO>>>\n")
    user=input('Ingrese el nombre de usuario: ')
    contra=input('Ingrese la contraseña: ')
    email=input('Ingrese el correo electronico: ')
    fname=input('Ingrese NOMBRE COMPLETO: ')
    punt=int(input('Ingrese la puntuacion: '))
    tipo=input('Ingrese el tipo de usuario: ')

    insert="INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES(?,?,?,?,?,?);"
    data=(user,contra,email,fname,punt,tipo)
    conn.execute(insert,data)
    ###
    print("\n<<<PRODUCTO>>>\n")
    nameProduct=input('Ingrese el nombre del producto: ')
    price=int(input('Ingrese el PRICE: '))
    nroserie=input('Ingrese el Nro de Serie: ')
    mproducto=input('Ingrese el modelo del producto: ')
    categoria=input('Ingrese el CATEGORIA: ')
    stock=int(input('Ingrese el STOCKACTUAL: '))

    insert1="INSERT INTO PRODUCTOS(NAMEPRODUCT,PRICE,NRO_SERIE,PRODUCTO,CATEGORIA,STOCKACTUAL) VALUES(?,?,?,?,?,?);"
    data1=(nameProduct,price,nroserie,mproducto,categoria,stock)
    conn.execute(insert1,data1)
    #####
    print("\n<<<INVENTARIO>>>\n")
    cantidad=int(input('Ingrese cantidad a vender: '))
    product=int(input('Ingrese id de producto: '))

    insert2="INSERT INTO INVENTARIO(CANTIDAD,PRODUCTOID) VALUES(?,?);"
    data2=(cantidad,product)
    conn.execute(insert2,data2)
    #####
    print("\n<<<VENTA>>>\n")
    ptotal=int(input('Ingrese EL PRECIO TOTAL: '))
    producto=int(input('Ingrese id de producto: '))
    orden=int(input('Ingrese id de la orden del inventario: '))
    usuario=int(input('Ingrese el id del usuario: '))
    tcambio=int(input('Ingrese el id del tipo de cambio actual: '))

    insert3="INSERT INTO VENTA(PRICETOTAL,PRODUCTOID,ORDERID,USUARIOSID,TCID) VALUES(?,?,?,?,?);"
    data3=(ptotal,producto,orden,usuario,tcambio)
    conn.execute(insert3,data3)

    insert4="INSERT INTO TIPCAMBIO (COMPRA,VENTA,ORIGEN,MONEDA,FECHA) VALUES (?,?,?,?,?);"
    conn.execute(insert4,te)
    conn.commit()
    conn.close()
