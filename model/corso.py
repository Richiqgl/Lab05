from dataclasses import dataclass
@dataclass
class Corso:
    codins:str
    crediti:int
    nome:str
    pd:int

    def __str__(self):
        return  f"{self.codins} - CFU: {self.crediti} - nome: {self.nome} pd {self.pd}"

    def __eq__(self, other):
        return self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)
