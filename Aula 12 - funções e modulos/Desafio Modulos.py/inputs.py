import modulo as md

def notas():
    notas_lista = []
    notas_ = input("Deseja cadastrar as notas dos alunos? sim/não ").lower()
    
    while notas_ == "sim":
        nota = float(input("Salve a nota do aluno: "))
        notas_lista.append(nota)
        notas_ = input("Deseja cadastrar outra nota? sim/não ").lower()
    
    if notas_lista:
        print("\nEstatísticas das notas cadastradas: ")
        md.exibir_estatisticas(notas_lista)
    else:
        print("Nenhuma nota foi cadastrada. Obrigado.")