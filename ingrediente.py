class Ingrediente:
    def __init__(self,nome: str, quantidade_original: float, unidade: str,):
        #atribuiçoes de estado do Objeto
        self.quantidade_calculada = 0.0
        self.nome = nome
        self.unidade = unidade
        self.quantidade_original = quantidade_original


    def calcular_nova_quantidade(self,fator: float):
        self.quantidade_calculada= self.quantidade_original * fator

    def __str__(self):
        #metodo para representação em string
        return f"{self.nome:<20} | {self.quantidade_calculada:<18.2f} | {self.unidade}"