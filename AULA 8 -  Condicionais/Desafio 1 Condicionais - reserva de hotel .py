# Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias.

# Cadastro de Cliente: O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.
# Reservas de Quartos: O sistema deve oferecer 3 tipos de quartos:"Simples", "Duplo" e "Luxo". OK
# Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:

# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.

# Cálculo da Estadia: O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.
# Pagamento: O sistema deve exibir o valor total a ser pago por cada cliente.
# Regras Adicionais: Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.***
# O sistema não deve usar loops (for, while) nem funções. O código deve considerar todos os casos possíveis de escolha dos clientes.

print("Seja bem vindo ao hotel com H")

clientes = []

clientes.append({'nome': input("Digite o nome do cliente 1: "), 'idade': int(input("Digite a idade do cliente 1: "))})
clientes.append({'nome': input("Digite o nome do cliente 2: "), 'idade': int(input("Digite a idade do cliente 2: "))})
clientes.append({'nome': input("Digite o nome do cliente 3: "), 'idade': int(input("Digite a idade do cliente 3: "))})

print(clientes)

quartos = {
""
"Simples": 100,
"Duplo": 150,
"Luxo": 250}

escolha_de_quarto = input("Escolha o tipo de quarto que deseja reservar: 1 - Simples R$ 100,00, 2 - Duplo R$ 150,00, 3 - Luxo R$ 250,00: ")

