# 1 Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.

n1 = float(input("Digite um número: "))
if n1 == 0:
    print("O número é zero.")
elif n1 > 0:
    print ("O número é Positivo.")
else:
    print("O número é negativo")    

# 2 Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.

idade = int(input("Qual é sua idade: "))
if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")

# 3 Declara uma variável com um número qualquer, determine se um número é par ou ímpar.

var = int(input("Digite um número: "))
if var % 2 == 0:
    print("O número é par.")
else: 
    print("O número é impar.")

# 4 Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo é equilátero, isósceles ou escaleno

l1 = int(input("Digite a medida do primeiro lado: "))
l2 = int(input("Digite a medida do segundo lado: "))
l3 = int(input("Digite a medida do tereiro lado: "))

if l1 == l2 == l3:
    print("O triângulo é equilatero.")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("O triângulo é isóceles.")
else: 
    print("O triângulo é escaleno.")

# 5 Determine se um número é múltiplo de 5 e 7.

num = int(input("Digite um número: "))
if num % 5 == 0 or num % 7 == 0:
    print("O valor digitado é multiplo de 5 ou 7")
else:
    print("Não é multiplo de 5 ou 7")

# 6 Verifique se um número é positivo e maior que 10

num1 = int(input("Digite um número: "))
if num1 > 0 and num1 >= 10:
    print("O valor é positivo e maior que 10")
elif num1 > 0 and num1 < 10:
    print("O valor é positivo, mas é menor que 10")
else:
    print("O valor é negativo")

#7 Verifique se um número é divisível por 3 ou 5.

num2 = int(input("Digite um número: "))
if num2 % 3 == 0 or num2 % 5 == 0:
    print("O número é divisível por 3 ou 5")
else:

    print("O valor não é divisivel por 3 ou 5")
