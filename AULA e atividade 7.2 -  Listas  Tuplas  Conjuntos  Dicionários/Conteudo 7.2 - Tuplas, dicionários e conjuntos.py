# Tupla é imutável, usa parêntese ou não usa nada. Poucos métodos podem ser usados.

tupla = (1,2,3,4,5)
tupla_1 = 1,2,3,4,5
t = tuple(range(1,10)) # uso da função tuple para criar uma tupla

# DESEMPACOTAMENTOS - Em Python, desempacotamento de tuplas (ou tuple unpacking) é o processo de atribuir os elementos de uma tupla
# (ou outra sequência) a variáveis individuais de forma direta e elegante. Atribui os indices de uma tupla a variáveis.

t = 1,2,3,4,5
a,b,c,d,e = t
print(a,b,c,d,e)
print(a)

# Na tupla pode ser usado o += para incluir dados na tupla.

# CONJUNTOS - Um conjunto (set) em Python é uma coleção de elementos únicos e sem ordem. Se cria com chaves {}. Possui poucos métodos para trabalhar com ele.

conjunto_1 = {1,2,3}
conjunto_2 = set(range(1,11)) # set pode ser usado para criar um conjunto

print(conjunto_1 | conjunto_2) # a | é usada para unir conjuntos e valores repetidos não são apresentados. Pode-se usar a palavra .union também
print(conjunto_1.union(conjunto_2))
print(conjunto_1 & conjunto_2) # & ou intersection mostra quais valores dentro do conjunto são comuns
print(conjunto_1.intersection(conjunto_2))
print (conjunto_1 - conjunto_2) # traz quais são os valores diferentes dentro do primeiro conjunto em relação ao segundo
print (conjunto_1.difference(conjunto_2))
print(conjunto_1 ^ conjunto_2) # diferença simetrica, traz todos os valores que não se repetem em ambos conjuntos.
print(conjunto_1.symmetric_difference(conjunto_2))
print({1,2}.issubset(conjunto_1)) # você usa essa função para consultar se os dados que informou no print aparecem no conjunto consultado, a saida será booleana.

# DICIONÁRIOS - é uma estrutura de dados mais detalhada. 
# Dicionários são formados de chaves e valores separados por :.

c = dict(a=10, b=[20,15,22], c=(30,21,12)) # um dicionário pode ser declarado dessa forma, mas é menos versátil, mas pode declarar listas, tuplas, conjuntos, etc.
print(c)

pessoa = {
"Nome": "Jose",
"idade": 25,
"Escolaridade": "Superior completo"
}

print(pessoa["Nome"]) # chama o valor referente a chave solicitada dentro da lista criada
print(pessoa["Escolaridade"])
print(pessoa["idade"])