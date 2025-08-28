


n = int(input("Quantos Ingredientes serao digitados? "))

nome: [str] = [0 for x in range(n)]
unidade: [str] = [0 for x in range(n)]
quantidade_receita: [float] = [0 for x in range(n)]
quantidade_usuario: [float] = [0 for x in range(n)]


for i in range (n):
    nome[i]= str(input("Digite o nome do ingrediente: "))
    quantidade_receita[i] = float(input("Digite a Quantidade: "))
    unidade[i]= str(input("Digite a Unidade do ingrediente: "))

print("Oque voce deseja Fazer?")
print("1 - Escalonar a receita "
      "\n2- Multiplicar a receita a receita "
      "\n3- divir a receita ")
opcao = int(input(""))

while True:
    if opcao == 1:
        print("Agora Digite as Quatidades que voce tem de cada Item ")

        for i in range (n):
            quantidade_usuario[i]= float(input(f"Qunato Voce possui de {nome[i]} ? "))

        if quantidade_usuario[i] <= 0:
            print("Quantidade insuficiente!!")
            exit()

        fator_limitante = min(quantidade_usuario[i] / quantidade_receita[i] for i in range(n))

        for i in range(n):
            quantidade_usuario[i] = quantidade_usuario[i] * fator_limitante
        break



    elif opcao == 2:
        M = float(input("Agora Digite Por quanto voce quer multiplicar a receita "))
        for i in range(n):
            quantidade_usuario[i] = quantidade_receita[i] * M
        break

    elif opcao == 3:
        D = float(input("Agora Digite Por quanto voce quer Dividir a receita "))

        for i in range(n):
            quantidade_usuario[i] = quantidade_receita[i] / D
        break

    else:
        print("Opçao invalida")
        break


print("\nAqui Estao os ingredientes e suas quantidades Nescessarias para a receita")
print("")
print(f"{'Ingrediente':<20} | {'Quantidade':<12} | {'Unidade'}")
print("-" * 45)

for i in range(n):
    print(f"{nome[i]:<20} | {quantidade_usuario[i]:<12.2f} | {unidade[i]}")