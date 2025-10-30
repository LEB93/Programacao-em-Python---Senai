#Listas são mutaveis e podemos atribuir vários valores a ela, diferentemente de variáveis que aceitam apenas um valor
#lista vazia

lista_vazia = []
print(lista_vazia)

#lista com valores inteiros

lista = [1,2,3]
print(lista[1]) # imprime o valor referente ao indice selecionado na lista
print(lista) # imprime a lista completa

n1 = lista[0] # acessa o indice na lista
n2 = lista[1] # acessa o indice na lista

print(n1 + n2) # soma dos indices dentro da lista

# MÉTODOS DE LISTAS

# dir mostra as funções/Métodos que podemos usar dentro da lista que criamos, pode variar de acordo com o objeto, por exemplo, lista, tupla, etc.

print(dir(lista))

# FUNÇÕES DAS LISTAS - usa o nome da função, abre e fecha parênteses e dentro dela insere o nome da lista

print(len(lista)) # mostra o tamanho da lista (quantidade de indices)
print(sum(lista)) # suma dos valores que compõe a lista
print(max(lista)) # mostra o maior númera lista
print(min(lista)) # mostra o menor númera lista

lista_t = ["Z", "A", "J"]
print(sorted(lista_t)) # sorted ordena os dados string em ordem alfabética

# .append adiciona um valor desejado ao final da lista

lista.append(10)
print(lista)

# .insert - Adiciona um valor na lista

lista.insert(0,25)
print(lista)

# .count - conta a quantidade de determinado dado dentro da lista

lista.count(2)

# .extend - inclui vários números ao final de uma lista original

lista.extend([13, 15, 16])
print(lista)

# Métodos para remover dados da lista

lista.remove(13) # remove o primeiro valor informado da esquerda para a direita
print(lista)

del lista[0] # Apagará o indice informado manualmente
print(list)

lista.pop() # apaga o ultimo valor da lista
lista.pop(2) # apaga o valor referente ao indice informado dentro da lista
lista.sort() # ordena a lista
lista.sort(reverse=True) # ordena a lista de maior para menor

x = lista.copy
print(x)  # Copia a lista

indice = lista.index(15) # apresta a indice do valor informado dentro da lista, informa apenas a posição do primeiro número, contando da esquerda para a direita. Valores repetidos são ingnorados

x = "Texto"
print(x.split()) # transforma o texto numa lista

# Clear limpa os dados da lista

lista.clear()
print(lista)


# CRIAÇÃO DE LISTAS COM A FUNÇÃO RANGE

lista_r1 = list(range(11)) # Cria uma lista de 0 a 10, com o valor padrão de start (0) e step (1)
lista_r1 = list(range(1,11)) # Cria uma lista a partir do número 1 até 10 (não inclusivo), com o step padrão de 1
lista_r1 = list(range(1,11,2)) # Cria uma lista de 1 até 10 (não inclusivo), pulando de 2 em 2