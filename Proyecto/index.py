
#import mysql.connector
import requests
from bs4 import BeautifulSoup


from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

from flask_session import Session




app = Flask(__name__)

#MYSQL coneccion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdleyes'
mysql = MySQL(app)

#settings
#como va ir protegida nuestra sesion
app.secret_key ='mysecretkey'




SQL_LISTADO = 'SELECT Expediente, Titulo FROM tinformacion WHERE Titulo like %s'

SQL_ALP = 'SELECT Expediente, Titulo FROM tinformacion WHERE Parlamento = "Partido Morado"and Titulo like %s'

SQL_ACP ='SELECT Expediente, Titulo FROM tinformacion WHERE Parlamento = "Acción Popular"and Titulo like %s'

def Obtener_Listado(Titulo):


    #-------------#
    cur=mysql.connection.cursor()
    sql = SQL_LISTADO  
    lista = None
    val = ('%'+Titulo+'%',)
    cur.execute(sql,val)
    lista = cur.fetchall()
    #if conexion is not None:
     #   conexion.disconnect()
    return lista

def Obtener_ListadoALP(Titulo):


    #-------------#
    cur=mysql.connection.cursor()
    sql = SQL_ALP  
    lista = None
    val = ('%'+Titulo+'%',)
    cur.execute(sql,val)
    lista = cur.fetchall()
    #if conexion is not None:
     #   conexion.disconnect()
    return lista

def Obtener_ListadoACP(Titulo):


    #-------------#
    cur=mysql.connection.cursor()
    sql = SQL_ACP  
    lista = None
    val = ('%'+Titulo+'%',)
    cur.execute(sql,val)
    lista = cur.fetchall()
    #if conexion is not None:
     #   conexion.disconnect()
    return lista









@app.route("/ProyectosCongresoLey", methods =["GET"])
# EL HTML LO ENVIA UNA RUTA LLAMADA INDEX
def index():
    Titulo_buscador = ""
    if "Titulo" in request.args:
        Titulo_buscador = request.args["Titulo"]
    
    leyes = Obtener_Listado(Titulo_buscador)
    #-------SINONIMOS-------#
    url='http://www.wordreference.com/sinonimos/'
    try:
        buscar=url+Titulo_buscador
        resp=requests.get(buscar)
        bs=BeautifulSoup(resp.text,'lxml')
        lista = bs.find(class_='trans clickable')
        sinonimos = lista.find("li")
        sino = sinonimos.text
        #-------SIgnificado-------#
        url2='http://www.wordreference.com/definicion/'
    
        buscar2=url2+Titulo_buscador
        resp2=requests.get(buscar2)
        bs2=BeautifulSoup(resp2.text,'lxml')
        lista2 = bs2.find(class_='trans clickable')
        significado = lista2.find("li")
        sing = significado.text
    except:
        sino = ""
        sing = ""
    
    return render_template("index.html", informacion = leyes, sab =sino, signi=sing)
   
   
@app.route("/informacion")
def InfoLeyes():
    cur=mysql.connection.cursor()

    cur.execute('SELECT Expediente, Periodo, Legislatura, Propone, Parlamento, Titulo, Objeto FROM tinformacion WHERE Expediente = "08046/2020-CR"')
    data1 = cur.fetchall()


    return render_template("informacion.html", informacion1=data1)


@app.route("/")
def sensi():

    return render_template("sensi.html")


#PARA ALIANZA PARA EL PROGRESO
@app.route("/AlianzaParaProgreso")
def AlianzaParaProgreso():
    Titulo_buscador = ""
    if "Titulo" in request.args:
        Titulo_buscador = request.args["Titulo"]
    
    leyes = Obtener_ListadoALP(Titulo_buscador)
    #-------SINONIMOS-------#
    url='http://www.wordreference.com/sinonimos/'
    try:
        buscar=url+Titulo_buscador
        resp=requests.get(buscar)
        bs=BeautifulSoup(resp.text,'lxml')
        lista = bs.find(class_='trans clickable')
        sinonimos = lista.find("li")
        sino = sinonimos.text
        #-------SIgnificado-------#
        url2='http://www.wordreference.com/definicion/'
    
        buscar2=url2+Titulo_buscador
        resp2=requests.get(buscar2)
        bs2=BeautifulSoup(resp2.text,'lxml')
        lista2 = bs2.find(class_='trans clickable')
        significado = lista2.find("li")
        sing = significado.text
    except:
        sino = ""
        sing = ""


    return render_template("AlianzaParaProgreso.html", informacion = leyes, sab =sino, signi=sing)


#para accion popular

@app.route("/AccionPopular")
def AccionPopular():
    Titulo_buscador = ""
    if "Titulo" in request.args:
        Titulo_buscador = request.args["Titulo"]
    
    leyes = Obtener_ListadoACP(Titulo_buscador)
    #-------SINONIMOS-------#
    url='http://www.wordreference.com/sinonimos/'
    try:
        buscar=url+Titulo_buscador
        resp=requests.get(buscar)
        bs=BeautifulSoup(resp.text,'lxml')
        lista = bs.find(class_='trans clickable')
        sinonimos = lista.find("li")
        sino = sinonimos.text
        #-------SIgnificado-------#
        url2='http://www.wordreference.com/definicion/'
    
        buscar2=url2+Titulo_buscador
        resp2=requests.get(buscar2)
        bs2=BeautifulSoup(resp2.text,'lxml')
        lista2 = bs2.find(class_='trans clickable')
        significado = lista2.find("li")
        sing = significado.text
    except:
        sino = ""
        sing = ""


    return render_template("AccionPopular.html", informacion = leyes, sab =sino, signi=sing)
    
    

    
    

@app.route("/FuerzaPopular")
#para fuerza popular
def FuerzaPopular():
    cur=mysql.connection.cursor()
    cur.execute('SELECT Expediente, Titulo FROM tinformacion WHERE Parlamento = "Fuerza Popular"')
    data1 = cur.fetchall()


    return render_template("FuerzaPopular.html", info=data1)

@app.route("/PartidoMorado")
#para partido morado
def PartidoMorado():
    cur=mysql.connection.cursor()
    cur.execute('SELECT Expediente, Titulo FROM tinformacion WHERE Parlamento = "Partido Morado"')
    data1 = cur.fetchall()


    return render_template("PartidoMorado.html", info=data1)

@app.route("/Frepap")
#para frepap
def Frepap():
    cur=mysql.connection.cursor()
    cur.execute('SELECT Expediente, Titulo FROM tinformacion WHERE Parlamento = "Frente Popular Agrícola del Perú"')
    data1 = cur.fetchall()


    return render_template("Frepap.html", info=data1)


@app.route("/UnionPeru")
#para union por el peru
def UnionPeru():
    cur=mysql.connection.cursor()
    cur.execute('SELECT Expediente, Titulo FROM tinformacion WHERE Parlamento = "Unión por el Perú"')
    data1 = cur.fetchall()


    return render_template("UnionPeru.html", info=data1)



if __name__ == '__main__':
    app.run(debug= True, port=8000)


