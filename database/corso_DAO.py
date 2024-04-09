# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso
def getCorsi():
    try:
        cnx = get_connection()
        cursor =cnx.cursor(dictionary=True)
        query="""SELECT * 
                FROM corso"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Corso(row["codins"],
                                  row["nome"],
                                  row["crediti"],
                                row["pd"]))
        cursor.close()
        cnx.close()
        return result

    except Exception:
        print(Exception)
        return None
