import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import requests
import json
import os
import db
import random
from migrate import ingresard

"""def insertData():
    #CREACIÓN/ACTUALIZACIÓN DE LA TABLAS (1 USO)
    creart()
    relle=[0,0] 
    #MANEJO Y EXTRACCIÒN DE DATOS DE LA API-SUNAT
    te=[]
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    re=requests.get(url)
    t=re.json()
    te=list(t.values()) 
    print(te)
    #obtiene la ruta absoluta Y CONEXIÓN
    path_=os.getcwd()+'\project\\dataTienda.csv'
    conn=sqlite3.connect('tienda.db')
    cursor=conn.cursor()
    #RELLENAR BASE DE DATOS CON ARCHIVO CSV
    with open(path_,'r') as file:
        filas=0
        m=1
        heading = next(file)
        for row in file:
            del relle[0]
            del relle[0]
            relle.append(m)
            relle.append(m)
            d=row.split(";")
            pl=[d[3],d[7],d[8],d[4],d[6],d[9]]
            il=[d[5],d[10],d[2]]
            vl=[d[0],d[1],d[2]]
            ml=vl+relle
            cursor.execute("INSERT INTO PRODUCTOS (NAMEPRODUCT,PRICE,CATEGORIA,NRO_SERIE,PRODUCTO,STOCKACTUAL) VALUES (?,?,?,?,?,?);",pl)
            cursor.execute("INSERT INTO INVENTARIO (CANTIDAD,FECHA_MOVIMIENTO,PRODUCTOID) VALUES (?,?,?);",il)
            cursor.execute("INSERT INTO TIPCAMBIO (COMPRA,VENTA,ORIGEN,MONEDA,FECHA) VALUES (?,?,?,?,?);",te)
            cursor.execute("INSERT INTO VENTA (ORDERID,PRICETOTAL,PRODUCTOID,TCID,USUARIOSID) VALUES (?,?,?,?,?);",ml)
            conn.commit()
            filas+=1
            m+=1
    conn.close()
    print(f"Se agregaron {filas} filas")
    #print(path_)
    #df = pd.read_csv (path_, sep = ";") 
    ### logica para insertar 
    #for i,fila in df.iterrows():
        #print(fila['ORDER_ID'])
"""
def alterar():
    ingresard()

def updateDolar():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    pass

def expo_gen():
    #Listas
    c,v,p,e,k = [],[],[],[],[]

    #EXCEL*******************************
    #df = pd.read_csv(os.getcwd()+'\project\\dataTienda.csv',sep=';')
    conn=sqlite3.connect('tienda.db')
    #cursor=conn.cursor()
    #solicitar tablas
    cons1="SELECT * FROM USUARIOS"
    cons2="SELECT * FROM PRODUCTOS"
    cons3="SELECT * FROM INVENTARIO"
    cons4="SELECT * FROM TIPCAMBIO"
    cons5="SELECT * FROM VENTA"
    df1= pd.read_sql(cons1,conn,index_col='ID')
    df2= pd.read_sql(cons2,conn,index_col='ID')
    df3= pd.read_sql(cons3,conn,index_col='IDMOVIMIENTO')
    df4= pd.read_sql(cons4,conn,index_col='IDTC')
    df5= pd.read_sql(cons5,conn,index_col='VENTAID')
    with pd.ExcelWriter(os.getcwd()+'\project\\datosexcel.xlsx') as writer:
        df1.to_excel(writer,sheet_name='usuarios',encoding='utf-8',index=False)
        df2.to_excel(writer,sheet_name='productos',encoding='utf-8',index=False)
        df3.to_excel(writer,sheet_name='inventario',encoding='utf-8',index=False)
        df4.to_excel(writer,sheet_name='tipcambio',encoding='utf-8',index=False)
        df5.to_excel(writer,sheet_name='venta',encoding='utf-8',index=False)
    #GRÀFICO*******************************
    #Captura de datos
    for i,fila in df2.iterrows():
        c.append(fila['CATEGORIA'])
    #Procesamiento---------------------
    d=dict(zip(c,map(lambda x: c.count(x),c))) #print(d)
    v=list(d.values()) #print(v)
    t=sum(v) #print(t)
    for k in range(len(v)):
        por=(v[k]/t)*100
        p.append(por) #print(p)
    #for l in range(len(v)):
        #e.append(random.random()) #Explodes
    k=list(d.keys()) #print(k)
    #Mostrar g. circular---------------------
    fig1, ax1=plt.subplots()
    ax1.pie(p,labels=k,autopct='%1.1f%%',shadow=True,startangle=90)
    ax1.axis('equal')
    plt.show()
    #Motrar g. barras---------------------
    fig = plt.figure(figsize=(6,6))
    ax=fig.add_subplot(1,1,1)
    ax.set(title="G.Barras",xlabel="Categorias",ylabel="Cantidad"
                            , xlim=(0,len(k)),ylim=(0,max(v)))
    ax.bar(k,v,color='red')
    plt.show()


message="""
    1)Insertar data
    2)Actualizar data del dolar
    3)Generar reporte [Excel]
    0)Salir
"""
print(message)
a=int(input('ingrese la tarea a realizar: '))
while a!=0:
    os.system("cls")
    if a==1:
        alterar()
    elif a==2:
        updateDolar()
    elif a==3:
        expo_gen()
    else:
        print("Opcion incorrecta. Vuelva a introducir")

    print(message)
    a=int(input('ingrese la tarea a realizar: '))

