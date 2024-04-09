from dataclasses import dataclass
@dataclass
class Studente:
    matricola:str
    nome:str
    cognome:str
    cds:int

    def __str__(self):
        return f"matricola {self.matricola} - nome: {self.nome} - cognome: {self.cognome} cds {self.cds}"
    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)