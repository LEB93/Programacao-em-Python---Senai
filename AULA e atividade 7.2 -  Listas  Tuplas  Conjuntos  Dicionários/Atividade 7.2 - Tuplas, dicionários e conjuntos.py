# Crie um e-commerce com a estrutura de dicionários. Os produtos vendidos são Livros, tablets e fones de ouvido.
# As ações: Comprar(), Pagar() e mostrar o valor total da compra.

Lojinha = {
    "Livros":{
        "Fisica": 120.00,
        "Quimica": 250.00},
    "Tablets": {
        "TopLing": 1500.00,
        "XingLing": 300.00},
    "Fones": {
        "Sony": 250.00,
        "JBL": 550.00}}

minhas_compras = {
    "Carrinho": [],
    "Valores": []}

Escolha1 = input("Livros, Tablets ou Fones: ")
prod1 = input(f"{Lojinha[Escolha1]}")

Escolha2 = input("Livros, Tablets ou Fones: ")
prod2 = input(f"{Lojinha[Escolha2]}")

Escolha3 = input("Livros, Tablets ou Fones: ")
prod3 = input(f"{Lojinha[Escolha3]}")

minhas_compras["Carrinho"].append(prod1)
minhas_compras["Valores"].append(Lojinha[Escolha1][prod1])

minhas_compras["Carrinho"].append(prod2)
minhas_compras["Valores"].append(Lojinha[Escolha2][prod2])

minhas_compras["Carrinho"].append(prod3)
minhas_compras["Valores"].append(Lojinha[Escolha3][prod3])
print(minhas_compras)

suma = sum(minhas_compras["Valores"])

pagamento = ["", "1 - PIX", "2 - CC", "3 - CB"]
escolha_pagamento = int(input(f"Digite o ID da forma de pagamento: {[pagamento]}"))
print(pagamento[escolha_pagamento])
print("Pagamento realizado com sucesso")

print(f"O valor total da suas compra é R$ {suma}")
