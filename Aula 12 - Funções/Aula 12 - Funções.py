# Sintaxe de uma função em Python

# Em Python, uma função é criada usando a palavra-chave def, seguida do nome da função e dos parênteses () — que podem conter parâmetros (opcionais).
# O corpo da função vem indentado (recuado com espaços).

def função_nova():
    return

# Como funciona:

# def indica que estamos definindo uma função.
# função_nova é o nome da função.
# Os parênteses () servem para incluir parâmetros, se necessário.
# O código dentro da função (indentado) é o que será executado quando ela for chamada.
# Para executar a função, usamos:

função_nova()

# Variáveis locais e globais

# Variáveis locais

# São criadas dentro de uma função e só podem ser usadas dentro dessa função.
# Elas deixam de existir assim que a função termina de ser executada.

# Exemplo:

def exemplo():
    mensagem = "Sou uma variável local"
    print(mensagem)

exemplo()
print("mensagem")  # ❌ Erro! 'mensagem' não existe fora da função

# Variáveis globais

# São criadas fora de qualquer função (encostadas na borda esquerda do código) e podem ser usadas em qualquer parte do programa.

# Exemplo:

mensagem = "Sou uma variável global"

def exemplo():
    print(mensagem)  # ✅ Pode acessar a variável global

exemplo()
print(mensagem)  # ✅ Também funciona fora da função

# Exercicios sobre IMC - como podemos usar

# Modo 1

def imc(altura, peso):
    return peso/altura**2


print(imc(1.70,65) + 250)

# Modo 2

def imc2():
    peso = float(input('peso: '))
    altura =  float(input('Altura:'))
    print(peso/altura**2)


print(imc2() + 250)

# Modo 3

peso = float(input('peso: '))
altura =  float(input('Altura:'))

def imc3():
    print(peso/altura**2)
    return peso/altura**2

print(imc3()+ 250)

# Exemplo 2

import statistics

def estatistica(notas):
    media  =  statistics.mean(notas)
    mediana = statistics.median(notas)
    desvio_p = statistics.stdev(notas)
    variancia = statistics.variance(notas)
    moda = statistics.mode(notas)

    return media, moda, mediana, desvio_p, variancia

notas = [10.,9.,5.,6.5,8.,7.,9.,5]
notas1 = [10.,5.,6.5]
notas2 = [8.,7.,9.,5]
notas3 = [10.,9]

print(estatistica(notas))
print(estatistica(notas1))
print(estatistica(notas2))
print(estatistica(notas3))