import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import requests
import json
import os
import db
import random
from migrate import creart

def insertData():
    creart()
    te=[]
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    re=requests.get(url)
    t=re.json()
    te=list(t.values()) 
    print(te)
    #creart()
    #obtiene la ruta absoluta
    path_=os.getcwd()+'\project\\dataTienda.csv'
    #conection a bd
    #conn=db.Conection('tienda.db')
    conn=sqlite3.connect('tienda.db')
    cursor=conn.cursor()

    with open(path_,'r') as file:
        filas=0
        for row in file:
            heading = next(file)
            d=row.split(";")
            pl=[d[3],d[7],d[8],d[4],d[6],d[9]]
            il=[d[5],d[10]]
            vl=[d[1]]
            cursor.execute("INSERT INTO PRODUCTOS (NAMEPRODUCT,PRICE,CATEGORIA,NRO_SERIE,PRODUCTO,STOCKACTUAL) VALUES (?,?,?,?,?,?);",pl)
            cursor.execute("INSERT INTO INVENTARIO (CANTIDAD,FECHA_MOVIMIENTO) VALUES (?,?);",il)
            cursor.execute("INSERT INTO TIPCAMBIO (COMPRA,VENTA,ORIGEN,MONEDA,FECHA) VALUES (?,?,?,?,?);",te)
            cursor.execute("INSERT INTO VENTA (PRICETOTAL) VALUES (?);",vl)
            conn.commit()
            filas+=1
    conn.close()
    print(f"Se agregaron {filas} filas")
    print(path_)
    df = pd.read_csv (path_, sep = ";") 
    ### logica para insertar 
    for i,fila in df.iterrows():
        print(fila['ORDER_ID'])

def updateDolar():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    pass

def expo_gen():
    #Listas
    c,v,p,e,k = [],[],[],[],[]

    #EXCEL*******************************
    df = pd.read_csv(os.getcwd()+'\project\\dataTienda.csv',sep=';')
    df.to_excel(os.getcwd()+'\project\\datosexcel.xlsx',sheet_name='data',encoding='utf-8',index=False)
    #GRÀFICO*******************************
    #Captura de datos
    for i,fila in df.iterrows():
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
    1)Insertar data:
    2)Actualizar data del dolar
    3)Generar reporte [Excel]
    0)Salir
"""
print(message)
a=int(input('ingrese la tarea a realizar: '))
while a!=0:
    os.system("cls")
    if a==1:
        insertData()
    elif a==2:
        updateDolar()
    elif a==3:
        expo_gen()
    else:
        print("Opcion incorrecta. Vuelva a introducir")

    print(message)
    a=int(input('ingrese la tarea a realizar: '))