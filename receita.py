import sys

from ingrediente import Ingrediente
class Receita:
    def __init__(self, nome_receita: str):
        self.nome = nome_receita
        self.ingredientes = []

    def adicionar_ingrediente(self, ingrediente: Ingrediente):
        self.ingredientes.append(ingrediente)

    def multiplicar(self, fator : float):
        """"Aplica o fator de multiplicação a todos os ingredientes."""
        for ing in self.ingredientes:
            #reutiliza o metodo da classe Ingrediente
            ing.calcular_nova_quantidade(fator)

    def dividir(self, divisor: float):
        """"Aplica o fator de divisao a todos os ingredientes"""
        fator = 1 / divisor
        for ing in self.ingredientes:
            ing.calcular_nova_quantidade(fator)

    def escalonar_limitante(self):
        fatores = []
        for ing in self.ingredientes:
            while True:
                try:
                    q_usuario = float(input(f"Quanto voce possui de {ing.nome} ({ing.unidade}) "))

                    #Garantir que a quantidade original nao e zero
                    if ing.quantidade_original == 0:
                        raise ZeroDivisionError

                    #calcula a proporção do fator
                    fator = q_usuario / ing.quantidade_original
                    fatores.append(fator)
                    break

                except ValueError:
                    print("Quantidade Invalida. Digite um Numero.")
                except ZeroDivisionError:
                    print("Erro de Calculo. Quantidade Nao pode ser Zero")
                    sys.exit()

        if not fatores:
            print("Nenhum fator de ingrediente foi calculado.")
            return

        fator_limitante = min(fatores)

        for ing in self.ingredientes:
            ing.calcular_nova_quantidade(fator_limitante)
        print(f"\nReceita escalonada com FATOR LIMITANTE de {fator_limitante:.2f}.")





    def imprimir_receita(self):
        """"Imprime a receita calculada em formato de Tabela."""
        print("\n"+"=" * 50)
        print(f"= Resultado da Receita '{self.nome.upper()}' =")
        print("=" * 50)
        print(f"{'ingrediente':<20} | {'nova Quantidade': <18} | {'unidade'}")
        print("-" * 50)
        for ing in self.ingredientes:
            print(ing)
