n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

média = (n1+n2+n3)/3

print(f'''
      
      Situação do aluno:

      Aprovado? - {média >=7}
      recuperação? - {média >=5 and média <=6.99}
      Reprovado? - {média<5}
''')