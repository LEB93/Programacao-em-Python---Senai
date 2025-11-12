# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 
# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA, MEDIA e o DESVIO DE PADRÃO DAS NOTAS DE ALUNOS DE UM COLÉGIO
# ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES.
# VOCÊ CRIAR SEUS PRÓPRIOS MÓDULOS OU USAR STATISTICS

import statistics as st

def cadastrar_notas():
    notas = []
    while True:
        resposta = input("Deseja cadastrar uma nota? (sim/não): ").lower()
        if resposta != "sim":
            break
        try:
            nota = float(input("Digite a nota do aluno: "))
            notas.append(nota)
        except ValueError:
            print("Por favor, digite um número válido.")
    return notas

def mostrar_estatisticas(notas):
    if not notas:
        print("Nenhuma nota cadastrada.")
        return
    
    print(f"Notas: {notas}")
    print(f"Média: {st.mean(notas):.2f}")
    print(f"Moda: {st.mode(notas):.2f}")
    print(f"Mediana: {st.median(notas):.2f}")
    print(f"Maior nota: {max(notas)}")
    print(f"Menor nota: {min(notas)}")
    
    if len(notas) > 1:
        print(f"Desvio padrão: {st.stdev(notas):.2f}")
    else:
        print("Desvio padrão: Não é possível calcular com apenas uma nota.")

# Programa principal
notas = cadastrar_notas()
mostrar_estatisticas(notas)
