# # Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:
    n = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número {n}.")

except ValueError:
    print("Erro: você não digitou um número inteiro!")

# # Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

try:
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))
    print(f"A divisão do primeiro número pelo segundo é {n1/n2}")
except ZeroDivisionError:
    print("Você tentou uma divisão por Zero que não é possivel!")

# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

lista = ["Banana","Maça","Morango","Maracuja","Atemoia", "Kiwi", "Pêssego"]

while True:

    try:
        indice = int(input("Digite o indice que deseja consultar: "))
        print(f"A fruta do índice {indice} é {lista[indice]}")
    except:
        print("Você digitou um indice inexistente!")

# Em Python, a palavra-chave raise é usada para lançar (ou gerar) uma exceção durante a execução de um programa.
# Quando uma exceção é levantada, o fluxo normal do programa é interrompido, e o Python procura um bloco try/except (caso exista) para tratar o erro.
# Se o erro não for tratado, o programa é encerrado e uma mensagem de erro é exibida.