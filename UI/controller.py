import flet as ft
import mysql.connector

from model.model import Model
from database.DB_connect import get_connection
from model.studente import Studente
from model.corso import Corso

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


    """
    Costruisce una funzione che restituisce gli studenti iscritti ad un corso
    :return un messagio di allerta se il corso non è selezionato     
    """
    def cercaIscrizione(self,e):
        self._view.txt_result.controls.clear()
        if self._view.txt_name.value is None:
            dlg=ft.AlertDialog(title=ft.Text("Corso non selezionato"),open=True)
            self._view._page.dialog=dlg
            self._view.update_page()
            return
        self._codiceCorso=self._view.txt_name.value
        try:
            cnx = get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.* 
                    FROM studente s, iscrizione i
                    WHERE codins=%s AND s.matricola=i.matricola"""
            cursor.execute(query, (self._codiceCorso,))
            result = []
            for row in cursor:
                result.append(Studente(row["matricola"],
                                    row["nome"],
                               row["cognome"],
                               row["CDS"]))
            cursor.close()
            cnx.close()
            for elemento in result:
                self._view.txt_result.controls.append(ft.Text(f"{elemento.__str__()}"))
            self._view.update_page()
        except mysql.connector.Error as err:
            print(err)
            return

    """
        Costruisce una funzione che restituisce lo studente con una particolare matricola 
        :return un messagio di allerta se il corso non è selezionato     
    """
    def cercaMatricola(self,e):
        self._view.txt_result.controls.clear()
        self._view._nome.value =""
        self._view._cognome.value = ""
        matricola_cercata=self._view._matricola.value
        try:
            cnx = get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.* 
                        FROM studente s
                        WHERE matricola=%s """
            cursor.execute(query, (matricola_cercata,))
            row=cursor.fetchone()
            if row is None:
                dlg = ft.AlertDialog(title=ft.Text("Matricola non trovata"), open=True)
                self._view._page.dialog = dlg
                self._view.update_page()
                return None
            else:
                elemento = Studente(row["matricola"],
                                    row["nome"],
                                    row["cognome"],
                                    row["CDS"])
                cursor.close()
                cnx.close()
                self._view._nome.value=elemento.nome
                self._view._cognome.value=elemento.cognome
                self._view.update_page()
                return 1
        except mysql.connector.Error as err:
            print(err)
            return None

    """ Costruisce una funzione che restituisce i corsi data un amatricola inserita nel database 
    """
    def cercaCorsi(self,e):
        if self.cercaMatricola(e) == 1:
            matricola_cercata=self._view._matricola.value
            try:
                cnx = get_connection()
                cursor = cnx.cursor(dictionary=True)
                query = """SELECT c.* 
                        FROM studente s, iscrizione i,corso c
                        WHERE s.matricola=%s AND s.matricola=i.matricola AND i.codins=c.codins"""
                cursor.execute(query, (matricola_cercata,))
                result = []
                for row in cursor:
                    result.append(Corso(row["codins"],
                                   row["crediti"],
                                   row["nome"],
                                   row["pd"]))
                cursor.close()
                cnx.close()
                for corso in result:
                    self._view.txt_result.controls.append(ft.Text(corso.__str__()))
                self._view.update_page()
            except mysql.connector.Error as err:
                print(err)
                return







