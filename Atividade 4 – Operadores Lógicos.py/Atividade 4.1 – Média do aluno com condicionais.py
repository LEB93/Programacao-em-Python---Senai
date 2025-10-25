# SISTEMA DE MÉDIA DE ALUNO

# 1  -  Criar 3 variáveis, notas, tipo float()***
# 2 -   Mostre no console a média das 3 variáveis***
# 3 - Passou de ano?  -  media >= 7***

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

média = (n1+n2+n3)/3
print(média)

if média >=7:
    print("Aluno aprovado")
elif média >=5 and média <7:
    print("Aluno em recuperação")
else:
    print("Reprovado")