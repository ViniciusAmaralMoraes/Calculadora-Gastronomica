

📄 README.md Profissional: Escalonador de Receitas em POO
Copie e cole este conteúdo (formato Markdown) no arquivo README.md do seu repositório.

Markdown

# 🧑‍🍳 Escalonador de Receitas | Python Orientado a Objetos (POO)

Este é um projeto de linha de comando (CLI) desenvolvido em Python 3.x para recalcular automaticamente as quantidades de ingredientes em qualquer receita, com base em fatores de multiplicação, divisão ou na quantidade limitada de um ingrediente disponível pelo usuário.

O principal objetivo deste projeto é demonstrar domínio dos conceitos de **Programação Orientada a Objetos (POO)** e **Engenharia de Software** através da modularização do código.

---

## 🛠️ Tecnologias e Conceitos Aplicados

| Conceito                                  | Aplicação no Projeto                                                                                                                                  |
|:------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Programação Orientada a Objetos (POO)** | Modelagem de entidades do mundo real com as classes `Receita` e `Ingrediente`.                                                                        |
| **Modularização**                         | Divisão do código em arquivos (`main.py`, `receita.py`, `ingrediente.py`) para responsabilidade única e melhor manutenção.                            |
| **Encapsulamento**                        | Lógica de cálculo contida nos métodos das classes, protegendo o estado dos objetos.                                                                   |
| **Estrutura de Dados**                    | Uso de listas de objetos (`self.ingredientes`) para gerenciar ingredientes de forma coesa.                                                            |
| **Tratamento de Erros**                   | Uso extensivo de blocos `try/except` para validar entradas do usuário (números inteiros, floats e formato correto) e garantir a robustez do programa. |
| **Lógica de Negócio**                     | Implementação do algoritmo de **Fator Limitante** (Opção 1) para escalonar a receita com precisão.                                                    |

---

## ✨ Funcionalidades

O programa oferece as seguintes opções no menu principal:

1.  **Escalonar a Receita (Ajuste por Fator Limitante):** O programa solicita a quantidade que o usuário possui de *cada* item. Ele então calcula o **fator limitante** (o ingrediente com menor proporção) e redimensiona a receita inteira com base nesse fator.
2.  **Multiplicar a Receita:** Aumenta a quantidade de todos os ingredientes por um fator fornecido.
3.  **Dividir a Receita:** Diminui a quantidade de todos os ingredientes por um divisor fornecido.

---

## 📁 Estrutura do Projeto

O código está organizado em módulos Python, conforme as boas práticas:

Escalonador_receitas/
├── main.py             # Ponto de entrada, lógica de Menu e interações do usuário.
├── receita.py          # Contém a classe Receita e a lógica de cálculo (multiplicar/dividir/escalonar).
└── ingrediente.py      # Contém a classe Ingrediente, o modelo de dados para cada item.
---

## 🚀 Como Executar

Para rodar este programa em seu ambiente local:

1.  **Pré-requisito:** Certifique-se de ter o **Python 3.x** instalado.
2.  **Clonar o Repositório:**
    ```bash
    git clone [https://github.com/ViniciusAmaralMoraes/Calculadora-Gastronomica.git]
    cd Calculadora-Gastronomica
    ```
3.  **Executar:**
    ```bash
    python main.py
    ```
4.  Siga as instruções do terminal para adicionar os ingredientes e escolher a operação.

---

## 📝 Exemplo de Uso (Opção 1: Escalonamento)

**Cenário:** Você tem 100g de farinha e a receita original pede 500g. Você tem 3 ovos e a receita original pede 2.

1.  O programa identifica que o fator para Farinha é: $100 / 500 = 0.2$
2.  O programa identifica que o fator para Ovos é: $3 / 2 = 1.5$
3.  O **Fator Limitante** é $0.2$ (o menor).
4.  O programa redimensiona a receita inteira multiplicando *todos* os ingredientes por $0.2$.

Este projeto foi desenvolvido por **[SEU NOME AQUI]**.