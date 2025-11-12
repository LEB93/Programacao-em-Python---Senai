def mercado_(lista_produtos, lista_valores):
    carrinho = []
    meus_valores = []
    per = input("Deseja fazer um pedido? (sim/não) ==> ").lower()
    
    while per == "sim":
        
        print("\nEscolha um produto para adicionar ao carrinho: ")
        for i in range(len(lista_produtos)):
            print(f"{i+1}. {lista_produtos[i]} - R$ {lista_valores[i]:.2f}")

        try:
            produto = int(input("\nDigite o número do produto desejado: "))
            if produto < 1 or produto > len(lista_produtos):
                print("Número inválido. Por favor, escolha um número válido.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue
        
        carrinho.append(lista_produtos[produto - 1])
        meus_valores.append(lista_valores[produto - 1])
        
        print(f"\nCarrinho: {carrinho}")
        soma = sum(meus_valores)
        print(f"Total: R$ {soma:.2f}")
        
        per = input("\nDeseja fazer outro pedido? (sim/não) ==> ").lower()

    else:
        print("Obrigado(a), volte sempre.")
        print("Se a compra foi efetuada, vá até a forma de pagamentos.")

def pagamentos(forma_pag):
    print("\nFormas de pagamento disponíveis:")
    for i, forma in enumerate(forma_pag, 1):
        print(f"{i}. {forma}")
    
    try:
        escolha = int(input("\nEscolha a forma de pagamento (número): "))
        if escolha < 1 or escolha > len(forma_pag):
            print("Opção inválida. Por favor, escolha uma opção válida.")
        else:
            print(f"Sua forma de pagamento é: {forma_pag[escolha - 1]}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def despedir(nome):
    return f"Obrigado(a), volte sempre {nome}!"
