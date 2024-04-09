import database.studente_DAO
import database.corso_DAO
class Model:
    def getCorsi(self):
        return database.corso_DAO.getCorsi()
    def getStudenti(self):
        return database.studente_DAO.getStudente()

