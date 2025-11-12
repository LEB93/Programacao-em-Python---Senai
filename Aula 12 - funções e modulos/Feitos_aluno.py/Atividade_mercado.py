import modulos_criados as md

def mercado():
    nome = input("Nome: ")

    lista_produtos = ["", "a", "b", "c", "d", "e"]
    valores = [0, 55.0, 60.8, 12.88, 9.52, 5.44]
    
    md.mercado_(lista_produtos, valores)
    
    lista_pag = ["", "PIX", "CC", "CD"]

    md.pagamentos(lista_pag)
 
    print(md.despedir(nome))

mercado()
