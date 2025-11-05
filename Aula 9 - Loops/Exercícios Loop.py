# # Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.

# n = 0
# while n < 101:
#     print(n)
#     n = n + 1

# # Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

# lista = []
# n = 0

# while n < 10:
#     nome = input("Digite um nome: ")
#     lista.append(nome)
#     n = n + 1

# print(lista)

## Crie um sistema de notas alunos, com as seguintes operações:
# ***Utilize While ou for***

# **Sistema de notas de alunos**

# ***Visão do professor***
# Acesso a conta com condicionais
# 3 chances de acessar o sistema

# Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# Inserir notas (se Senha correta)
# Fazer a média

# Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***

login_professor = "ABC"
senha_professor = 12345
tentativas = 0

alunos = []

print("\nSeja bem vindo ao Sistema de Notas de Alunos")

while tentativas < 3:
    
    login = input("\nDigite seu login: ")
    senha = int(input("Digite sua senha: "))

    if login == login_professor and senha == senha_professor:
        print("\nAcesso concedido.")
    else:
        tentativas+=1
        print(print(f"\nLogin ou senha incorretos. Você tem {3 - tentativas} tentativas restantes."))