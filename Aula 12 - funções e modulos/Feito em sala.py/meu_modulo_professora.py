def mercado_ (lista_produtos, lista_valores):
    
    carrinho = []
    meus_valores = []
    per = input("Deseja fazer um pedido? ==> ").lower()
    
    while per == "sim":
    
        produto = int(input(f'''
                            1{lista_produtos [1]} - R$ {lista_valores [1]}
                            2{lista_produtos [2]} - R$ {lista_valores [2]}
                            3{lista_produtos [3]} - R$ {lista_valores [3]}
                            4{lista_produtos [4]} - R$ {lista_valores [4]}
                            5{lista_produtos [5]} - R$ {lista_valores [5]}
                            '''))
        
        carrinho.append(lista_produtos[produto])
        meus_valores.append(lista_valores[produto])
        
        print(carrinho)
        soma = sum(meus_valores)
        print("Total R$ ", soma)
       
        per = input("Deseja fazer um pedido? ==> ")

    else:
        print("Obrigado(a), volte sempre.")
        print ("Se a compra foi efetuada vá ate a forma de pagamentos")

def pagamentos (forma_pag):
    
    print (forma_pag)
    escolha = int(input("Escolha a forma de pagamento"))
    print("Sua forma de pagamento é", forma_pag[escolha])

def despedir (nome):
    return f"Obrigado(a), volte sempre {nome}"
