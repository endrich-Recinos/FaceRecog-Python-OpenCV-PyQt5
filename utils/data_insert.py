from utils.my_connection import mysql_get_mydb
from pyfiglet import figlet_format
from utils.bypass import bypass

cnx = mysql_get_mydb() 

def logo(titulo):
    print("=" * 80)
    print(figlet_format(text=titulo, font="standard", justify="center"))
    print("=" * 80)

logo("Reconocimiento Facial")

def choose():    
    print("1 - Registrar usuario")
    print("2 - Identificar usuario")
    choose = input(str("\nOpcion: "))
    return choose

def cadastro(choose):
    if choose == "1":
        cursor = cnx.cursor()
        #
        print("\nPor favor, rellene los campos a continuación como se solicita.")
        Nombre = input(str("Nombre: ")).title()
        Matricula = input(str("Matricula: "))
        Correo = input(str("Correo: ")).lower()
        Date = input(str("Fecha Nacimiento: "))
        
        cursor.execute("use Formulario")
        sql = "INSERT INTO Alumnos (Nombre, Matricula, Correo, BDate) VALUES ('%s', '%s', '%s', '%s')" % (Nombre, Matricula, Correo, Date)
        cursor.execute(sql)
        cnx.commit()
        print("\nAlumno registrado con exito")
        return Nombre, Matricula, Correo, Date

    elif choose == "2":
        print()
        