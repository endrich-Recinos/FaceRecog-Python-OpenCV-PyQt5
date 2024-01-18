import mysql.connector
from mysql.connector import errorcode

def mysql_get_mydb():    
    try:
        cnx = mysql.connector.connect(user='root', password='',
                                host='127.0.0.1')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Ocurrio un error al establecer conexcion, por favor, verifique que sus datos esten bien")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Base de datos no existe")
        else:
            cnx.close()
    return cnx


    
