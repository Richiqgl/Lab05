import flet as ft
import mysql.connector

from model.model import Model
from database.DB_connect import get_connection

class Controller:
    def __init__(self, view, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def cercaIscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return

        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def popola_tendina(self):
        corsi = self._model.getCorsi()
        for corso in corsi:
            self._view.txt_name.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        self._view.update_page()


    def cercaIscrizione(self):
        self._codiceCorso=self._view.txt_name.value
        try:
            cnx = get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.* 
                    FROM studente s, iscrizione i
                    WHERE codins=%s s.matricola=i.matricola"""
            cursor.execute(query, (self._codiceCorso,))
            result = []
            for row in cursor:
                result.append((row["matricola"],
                                    row["nome"],
                               row["cognome"],
                               row["cds"]))
            cursor.close()
            cnx.close()
            return result
        except mysql.connector.Error as err:
            print(err)
            return

