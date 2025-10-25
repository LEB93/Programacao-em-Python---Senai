# 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

n1 = int(input("Digite um número inteiro: "))
print(f"O quadrado do número é {n1**2}")
print()

# 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))

print(nome+sobrenome)
print()

# 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

p1 = int(input("Digite o primeiro número inteiro: "))
p2 = int(input("Digite o segundo número inteiro: "))

contatenação = str(p1) + str(p2)

print("Resultado da concatenação:", contatenação)
print()

# 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.

A = "Python"
print(A, 10)
print()

# 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

frase = "Minha cor favorita é a cor "
cor = str(input("Digite qual é sua cor favotira: "))

print(frase + cor)