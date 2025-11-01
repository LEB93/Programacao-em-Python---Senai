# Estrutura de Condicionais em Python
# As condicionais são usadas para que o programa tome decisões com base em certas condições.
# A estrutura básica é a seguinte:

idade = 18

if idade >= 18:
    print("Você é maior de idade.")

# if → Verifica uma condição.
# Se for verdadeira, o código dentro do bloco será executado.

# Podemos acrescentar outras verificações usando o elif:

if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 16:
    print("Você pode votar, mas ainda não é maior de idade.")

# elif → Testa uma nova condição se o if for falso.

# E, por fim, usamos o else para tratar o caso em que nenhuma condição anterior é verdadeira:

if idade >= 18:
    print("Maior de idade.")
elif idade >= 16:
    print("Pode votar.")
else:
    print("Menor de idade.")

# else → Executa o código quando todas as condições anteriores são falsas.