# Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias. OK

# Cadastro de Cliente: O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes. OK
# Reservas de Quartos: O sistema deve oferecer 3 tipos de quartos:"Simples", "Duplo" e "Luxo". OK
# Cada cliente deve escolher um quarto para sua estadia. OK
# O preço da diária varia conforme o tipo de quarto: OK dados apresentado em um dicionário.

# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.

# Cálculo da Estadia: O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.
# Pagamento: O sistema deve exibir o valor total a ser pago por cada cliente.
# Regras Adicionais: Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.***
# O sistema não deve usar loops (for, while) nem funções. O código deve considerar todos os casos possíveis de escolha dos clientes.

print("\nSeja bem-vindo ao Hotel AVENGERS!!!") # \n para pular uma linha e deixar o retorno mais visual

clientes = [] # O cadastro dos clientes será guardado na lista clientes

clientes.append({'nome': input("\nDigite o nome do cliente 1: "), 'idade': int(input("Digite a idade do cliente 1: "))}) # Cadastro do primeiro cliente, usei \n para separar dados em blocos para cada cliente
clientes.append({'nome': input("\nDigite o nome do cliente 2: "), 'idade': int(input("Digite a idade do cliente 2: "))}) # Cadastro do segundo cliente com uso de \n
clientes.append({'nome': input("\nDigite o nome do cliente 3: "), 'idade': int(input("Digite a idade do cliente 3: "))}) # Cadastro do terceiro cliente com uso de \n

print("\nClientes cadastrados:") # Cabeçalho para que o cliente entenda o que será printado abaixo.
print(clientes) # Mostra a lista dos clientes cadastrados e suas idades.

# Abaixo crio um dicionário com dados do tipo de quartos e dos preços respectivos.

quartos = {
    "simples": 100,
    "duplo": 150,
    "luxo": 250}

# Dados referentes a reserva do cliente 1

print(f"\n{clientes[0]['nome']}, escolha o tipo de quarto:")
quarto1 = input("Deseja o quarto simples, duplo ou luxo): ").lower() # com o método .lower, mesmo que o cliente digite em maiusculas, o valor será transformado em minuscula para não dar erro.
dias1 = int(input("Quantos dias você ficará hospedado(a)? ")) # entrada para declarar a Qtde. de dias que o primeiro cliente ficará hospedado.

if quarto1 == "simples":
    total1 = quartos["simples"] * dias1
elif quarto1 == "duplo":
    total1 = quartos["duplo"] * dias1
elif quarto1 == "luxo":
    total1 = quartos["luxo"] * dias1
else:
    total1 = 0
    print("Opção inválida de quarto para o cliente 1.")

# Dados referentes a reserva do cliente 2

print(f"\n{clientes[1]['nome']}, escolha o tipo de quarto:")
quarto2 = input("Deseja o quarto simples, duplo ou luxo: ").lower() # idem linha 39
dias2 = int(input("Quantos dias você ficará hospedado(a)? ")) # entrada para declarar a Qtde. de dias que o segundo cliente ficará hospedado.

if quarto2 == "simples":
    total2 = quartos["simples"] * dias2
elif quarto2 == "duplo":
    total2 = quartos["duplo"] * dias2
elif quarto2 == "luxo":
    total2 = quartos["luxo"] * dias2
else:
    total2 = 0
    print("Opção inválida de quarto para o cliente 2.")

# Dados referentes a reserva do cliente 3

print(f"\n{clientes[2]['nome']}, escolha o tipo de quarto:")
quarto3 = input("Deseja o quarto simples, duplo ou luxo: ").lower() # idem linha 39
dias3 = int(input("Quantos dias você ficará hospedado(a)? ")) # entrada para declarar a Qtde. de dias que o terceiro cliente ficará hospedado.

if quarto3 == "simples":
    total3 = quartos["simples"] * dias3
elif quarto3 == "duplo":
    total3 = quartos["duplo"] * dias3
elif quarto3 == "luxo":
    total3 = quartos["luxo"] * dias3
else:
    total3 = 0
    print("Opção inválida de quarto para o cliente 3.")

# Dados referentes a reserva dos clientes 1,2 e 3.

print("\n===== RESUMO DAS RESERVAS =====")
print(f"{clientes[0]['nome']} - Total a pagar: R$ {total1:.2f}")
print(f"{clientes[1]['nome']} - Total a pagar: R$ {total2:.2f}")
print(f"{clientes[2]['nome']} - Total a pagar: R$ {total3:.2f}")

print("\nObrigado por escolher o Hotel Avengers!")


