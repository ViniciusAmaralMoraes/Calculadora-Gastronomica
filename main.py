import sys
from receita import Receita
from ingrediente import Ingrediente

# iniciando uma saudação ao usuario

print("\n"+"=" * 50)
print("BEM VINDO AO REFATORAMENTO DE RECEITAS ")
print(""+"=" * 50)

nome_receita = input("\nDigite o Nome da sua Receita: ")
minha_receita = Receita(nome_receita)

while True:
    try:
        quantidade_Ingredientes = int(input("Quantos Ingredientes tem a Receita? "))
        if quantidade_Ingredientes <=0 :
            raise ValueError("O Numero de Ingredientes deve ser Positivo.")
        break
    except ValueError as e:
        print(f"ERRO: entrada Invalida. {e}")

print('\n')

for i in range(quantidade_Ingredientes):
    while True:
        try:
            entrada = input(f"[{i+1}/{quantidade_Ingredientes}] Digite: Nome, Quantidade e Unidade (ex: Farinha 500 g): ").split()

            if len(entrada) != 3:
                raise  ValueError("Formato incorreto.")

            ingrediente, quantidade_str, unidade = entrada
            quantidade = float(quantidade_str)

            if quantidade <= 0 :
                raise ValueError("A quantidade deve ser Positiva.")

            minha_receita.adicionar_ingrediente(Ingrediente(ingrediente, quantidade, unidade))
            break

        except ValueError as e:
            # Captura erros de formato ou de valor
            print(f"ERRO: {e}. Por favor, siga o formato 'Nome Quantidade Unidade'.")



#Menu de Escolhoas

while True:
    print("\n--- Menu de Opções ---")
    print("1 - Escalonar a receita (Ajuste por ingrediente limitante)"
          "\n2 - Multiplicar a receita"
          "\n3 - Dividir a receita"
          "\n4 - Desistir da Receita (sair do Programa)")

    try:
        opcao = int(input("Escolha uma das opção: "))

        if opcao == 1:
            minha_receita.escalonar_limitante()
            break

        elif opcao == 2:
            fator_multiplicacao = float(input("Digite por quanto quer MULTIPLICAR a Receita: "))
            if fator_multiplicacao <= 0:
                raise ValueError
            minha_receita.multiplicar(fator_multiplicacao)
            break

        elif opcao == 3:
            fator_divisao = float(input("Digite por quanto quer DIVIDIR a Receita: "))
            if fator_divisao <= 0:
                raise ValueError
            minha_receita.dividir(fator_divisao)
            break

        elif opcao == 4:
            print("Obrigado por usar o Recalculador de Receitas!")
            sys.exit()

        else:
            print("Opção inválida! Tente novamente.")

    except ValueError:
        print("Entrada inválida! Digite um número para a opção ou para o fator de cálculo.")
    except Exception as e:
        # Captura erros internos
        print(f"Ocorreu um erro: {e}")
        break

minha_receita.imprimir_receita()