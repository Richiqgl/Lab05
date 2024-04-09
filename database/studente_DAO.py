# Add whatever it is needed to interface with the DB Table studente

import mysql.connector
from database.DB_connect import get_connection
from database.DB_connect import get_connection
from model.studente import Studente
def getStudente():
    try:
        cnx = get_connection()
        cursor =cnx.cursor(dictionary=True)
        query="""SELECT * 
                FROM studente"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Studente(row["matricola"],
                                  row["nome"],
                                  row["cognome"],
                                  row["cds"]))
        cursor.close()
        cnx.close()
        return result

    except mysql.connector.Error as err:
        print(err)
        return None