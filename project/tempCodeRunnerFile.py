import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import db
#import openpyxl as

def insertData():
    #obtiene la ruta absoluta
    path_=os.getcwd()+'\project\\dataTienda.csv'
    #conection a bd
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    print(path_)
    df = pd.read_csv (path_, sep = ";") 
    ### logica para insertar 
    for i,fila in df.iterrows():
        print(fila['ORDER_ID'])

def updateDolar():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    pass

def expo_gen():
    c=[] 
    v=[]
    df = pd.read_csv(os.getcwd()+'\project\\dataTienda.csv',sep=';')
    df.to_excel(os.getcwd()+'\project\\datosexcel.xlsx',sheet_name='data',encoding='utf-8',index=False)
    #df.CANTIDAD.value_counts().plot.pie()
    for i,fila in df.iterrows():
        c.append(fila['CATEGORIA'])
    d=dict(zip(c,map(lambda x: c.count(x),c))) 
    print(d)
    v=list(d.values()) 
    print(v)


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