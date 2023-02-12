import sqlite3
conn=sqlite3.connect('tienda.db')

def creart():

    cursor_obj = conn.cursor()
    cursor_obj.execute("DROP TABLE IF EXISTS USUARIOS")
    table = """CREATE TABLE USUARIOS 
               (ID  INTEGER PRIMARY KEY AUTOINCREMENT,
                USUARIO VARCHAR(25),
                PASSWORD VARCHAR(255) NOT NULL,
                EMAIL VARCHAR(255) NOT NULL,
                FULLNAME VARCHAR(25) NOT NULL,
                SCORE INT,
                TIPOUSUARIO VARCHAR(25)
                ); """
    cursor_obj.execute(table)
    cursor_obj.execute("DROP TABLE IF EXISTS PRODUCTOS")
    table = """CREATE TABLE PRODUCTOS 
               (ID  INTEGER PRIMARY KEY AUTOINCREMENT,
                NAMEPRODUCT VARCHAR(255) NOT NULL,
                PRICE MONEY NOT NULL, 
                CATEGORIA VARCHAR(25) NOT NULL,
                NRO_SERIE VARCHAR(25) NOT NULL,
                PRODUCTO VARCHAR(25) NOT NULL,
                STOCKACTUAL INT,
                CREACTION_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UPDATE_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ); """
    cursor_obj.execute(table)
    cursor_obj.execute("DROP TABLE IF EXISTS INVENTARIO")

    table="""CREATE TABLE INVENTARIO 
             (IDMOVIMIENTO  INTEGER PRIMARY KEY AUTOINCREMENT,
              CANTIDAD INT NOT NULL,
              FECHA_MOVIMIENTO TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              PRODUCTID INT ,
              CONSTRAINT fk_PRODUCTOS FOREIGN KEY (PRODUCTID) REFERENCES PRODUCTOS (ID)
              ) """
    cursor_obj.execute(table)
    cursor_obj.execute("DROP TABLE IF EXISTS TIPCAMBIO")

    table="""CREATE TABLE TIPCAMBIO 
             (IDTC  INTEGER PRIMARY KEY AUTOINCREMENT,
              COMPRA FLOAT NOT NULL,
              VENTA FLOAT NOT NULL, 
              ORIGEN VARCHAR(25) NOT NULL,
              MONEDA VARCHAR(25) NOT NULL,
              FECHA TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              )"""
    cursor_obj.execute(table)

    cursor_obj.execute("DROP TABLE IF EXISTS VENTA")

    table="""CREATE TABLE VENTA 
             (ORDERID  INTEGER PRIMARY KEY AUTOINCREMENT,

              PRODUCT_ID INT ,
              INVENTARIO_ID INT ,
              USUARIOS_ID INT ,
              TC_ID INT ,
              PRICETOTAL FLOAT NOT NULL,
              CONSTRAINT fk_PRODUCTOS FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCTOS (ID),
              CONSTRAINT fk_INVENTARIO FOREIGN KEY (INVENTARIO_ID) REFERENCES INVENTARIO (IDMOVIMIENTO),
              CONSTRAINT fk_USUARIOS FOREIGN KEY (USUARIOS_ID) REFERENCES USUARIOS (ID),
              CONSTRAINT fk_TIPCAMBIO FOREIGN KEY (TC_ID) REFERENCES TIPCAMBIO (IDTC)
              ) """

    cursor_obj.execute(table)
    conn.close()

# comentamos las insercciones ya que solo sera parte de la creacion de tablas
"""insert =" INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES('admin','admin','admin@datux.com','admin datux',0,'admin')"

conn.execute(insert)
insert =" INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES('cliente','cliente','email','cliente',0,'cliente')"
conn.execute(insert)


print("Table is Ready")
"""
def ingresard():
    print("Ingrese PRODUCTO")
    nameProduct=input('Ingrese el nombre del producto: ')
    price=input('Ingrese el PRICE: ')
    nroserie=input('Ingrese el Nro de Serie: ')
    mproducto=input('Ingrese el modelo del producto: ')
    categoria=input('Ingrese el CATEGORIA: ')
    stock=int(input('Ingrese el STOCKACTUAL: '))

    insert="INSERT INTO PRODUCTOS(NAMEPRODUCT,PRICE,NRO_SERIE,PRODUCTO,CATEGORIA,STOCKACTUAL) VALUES(?,?,?,?,?,?);"
    data=(nameProduct,price,nroserie,mproducto,categoria,stock)
    conn.execute(insert,data)

    print("Ingrese datos referentes a INVENTARIO")
    cantidad=int(input('Ingrese cantidad a vender: '))

    insert="INSERT INTO INVENTARIO(CANTIDAD) VALUES(?);"
    data=(cantidad)
    conn.execute(insert,data)

    conn.commit()
