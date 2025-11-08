# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

def compara ():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    if a % 2 == 0:
        print(f"{a} é um número par.")
    else:
        print(f"{a} é um número impar.")
    
    if b % 2 == 0:
        print(f"{b} é um número par.")
    else:
        print(f"{b} é um número impar.")

    if a > b:
        print(f"{a} é maior de {b}")
    elif b > a:
        print(f"{b} é maior de {a}")
    else:
        print(f"{a} e {b} são iguais")

compara()

# CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

def mult ():

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))

    op = (n1*n2*n3)

    print(f"A multiplicação dos 3 números é: {op}")

mult()

# CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

def potencia ():

    base = int(input("Digite um número: "))
    expoente = int(input("Digite o expoente: "))
    resultado = base ** expoente

    print(f"O resultado da potenciação é {resultado}")

potencia()

# CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.

def message ():

    idade = int(input("Digite sua idade: "))

    if idade == 18:
        print("Você atingiu a maioridade! Bem-vindo ao mundo adulto!")
    else:
        print("Você ainda não tem 18 anos. Continue aproveitando a juventude!")

message()

# DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.

def idade():

    ano_atual = int(input("Em que ano estamos: "))
    ano_nascimento = int(input("Em que ano você nasceu: "))

    idade_1 = ano_atual - ano_nascimento

    print(f"Aham, descobri, você tem {idade_1} anos.")

idade()

# DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.

anos = [2022, 2018, 2014, 2010, 2006, 2002, 1998, 1994]
ganhadores = ["Argentina", "França", "Alemanha", "Espanha", "Itália", "Brasil", "França", "Brasil"]

def brasil():
    ano = int(input("Escolha o ano da copa: "))
    
    if ano in anos:
        indice = anos.index(ano)
        print(f"O ganhador da Copa de {ano} foi {ganhadores[indice]}.")
    else:
        print("Não houve copa no ano escolhido.")

brasil()

# DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999. (Solução correta)

anos_vitoria_brasil = [1958, 1962, 1970, 1994, 2002]
anos_copa = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]

def brasil_campeao():
    ano = int(input("Digite um ano para saber se o Brasil ganhou a copa: "))

    if ano in anos_copa:
        if ano in anos_vitoria_brasil:
            print("O Brasil ganhou a copa nesse ano.")
        else:
            print("O Brasil não ganhou a copa nesse ano.")
    else:
        print("Não houve Copa do Mundo nesse ano.")

brasil_campeao()

# # DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.

# 1 - Função -  cumprimentar o cliente
# 2 - Função - restaurante
# 3 - Sugestão utilize listas  e loops

opções = ["Salada", "Macarronada", "Sandwich", "Sorvete"]

def saudação ():
    print("\nSeja bem vindo ao restaurant Dona Benta.")

def restaurante ():
    escolha = input(f"\nO que você que pedir: {opções}==> ").lower()
    print(f"\nSeu pedido foi um(a) {escolha} e já está sendo preparado.")

saudação()
restaurante()