# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 
# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA, MEDIA e o DESVIO DE PADRÃO DAS NOTAS DE ALUNOS DE UM COLÉGIO
# ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES.
# VOCÊ CRIAR SEUS PRÓPRIOS MÓDULOS OU USAR STATISTICS

import statistics as st

def moda(notas):
    return st.mode(notas)

def media(notas):
    return st.median(notas)

def dp(notas):
    return st.stdev(notas)

def maior(notas):
    return st.max(notas)

def menor(notas):
    return st.min(notas)

def exibir_estatisticas(notas):
    print(f"Notas cadastradas: {notas}")
    print(f"Moda das notas cadastradas: {notas}")
    print(f"Média das notas cadastradas: {notas}")
    print(f"Desvio Padrão das notas cadastradas: {notas}")
    print(f"Nota máxima das notas cadastradas: {notas}")
    print(f"Nota mínima das notas cadastradas: {notas}")