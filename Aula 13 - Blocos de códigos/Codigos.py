# 1 - Crie um número aleatório de 5,10

import random

def numero_aleatório():
    return random.randint(5,11)

# 2 - Crie 3 números aleatórios

import random

def numero_aleatorio_():
    numeros = []
    for i in range (3):
        numeros.append(random.randint(1,10))
    return numeros 

# 3 - Crie um número aleatório entre 10 a 30 utilize o range()

import random

def n_aleatorio ():
    return random.randrange(10,31)

# 4 - Contagem regressiva simples - Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)

def contagem_regressiva ():
    for c in range (10,0,-1):
        print(c)
    print("Fogo")

# 5 - Soma de números pares - Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.

def soma_pares ():
    numero = int(input("Digite um número inteiro positivo: "))
    soma = 0
    for i in range (2, numero+1, 2):
        soma +=1
    return soma

# 6 - Tabuada de multiplicação - Utilize print() na saída. Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10. (while ou for )

def tabuada():
    n = int(input("Digite um número inteiro: "))
    for i in range (1,11):
        print(f"{n} x {i} = {n * i}")

# 7 -  Números ímpares reversos - Exiba uma contagem regressiva de números ímpares de 99 a 1. (for) Chamar todas elas para o arquivo main()

def contagem_regressiva_impares():
    impares = []
    for i in range (99,0,-1):
        if i % 2 != 0:
            impares.append(i)
    return impares