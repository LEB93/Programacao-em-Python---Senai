# Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

lista = list(range(2,21,2))
print(lista)

# Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.

numeros = list(range(1,11))
print(numeros)

# Acesse e imprima o terceiro elemento da lista `numeros`.

print(numeros[2])

# Adicione o número 9 à lista `numeros` e imprima a lista atualizada.

numeros.append (9)
print(numeros)

# Remova o número 5 da lista `numeros` e imprima a lista resultante.

numeros.remove(5)
print(numeros)

# Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.

carros = ["BMW", "Jaguar", "Smart"]
print([carros], [numeros])