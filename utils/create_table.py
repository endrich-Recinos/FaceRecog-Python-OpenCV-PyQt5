import mysql.connector
from utils.my_connection import mysql_get_mydb

cnx = mysql_get_mydb()
cursor = cnx.cursor()

def create_table(cnx):
    cursor = cnx.cursor()
    try:
        # cursor.execute("DROP DATABASE Formulario")
        cursor.execute("CREATE DATABASE IF NOT EXISTS Formulario")
        cursor.execute("use Formulario")
        cursor.execute("CREATE TABLE IF NOT EXISTS Alumnos (ID int auto_increment, Nombre varchar(50) not null, Matricula varchar(50) not null, Correo varchar(200) not null, BDate varchar(200) not null, Data TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, primary key (id))")        
    except mysql.connector.Error as err:
        print("Ocurrio un error en su tabla")
        print(err)
    else:
        print("Tabla creada con exito")