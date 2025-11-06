# Semelhante as condicionais o Match Case, faz o computador fazer escolhas.
# Conhecido também como Strutural Pattern Matching. Estrutura Padrão Correspondente.

# ***EXERCÍCIOS com match/ case

# Verificando se o número é par ou ímpar

def n_escolhido (numero):
    match numero % 2:
        case 0:
            print(f"{numero} é par")
        case _:
            print(f"{numero} é ímpar")

numero = int(input("Digite um número: "))
n_escolhido(numero)

# Verificando se um número é positivo, negativo ou zero

n = int(input("Digite um número: "))

match n:
    case 0:
        print("O número é zero.")
    case x if x > 0:
        print("Número positivo.")
    case x if x < 0:
        print("Número negativo")   
        
# Verificando se uma string é vazia ou não

texto = input("Digite um texto: ")

match texto:
    case "":
        print("String vazio")
    case _: # _: é usado para representar qualquer resultado diferente dos anteriores 
        print("String não vazia")

# Verificando se um número é maior, menor ou igual a 10

n = int(input("Digite um número: "))

match n:
    case x if x == 10:
        print(f"O número digitado, {n}, é igual a 10")
    case x if x > 10:
        print(f"O número digitado, {n}, é maior a 10")
    case x if x < 10:
        print(f"O número digitado, {n}, é menor a 10")

# Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)

idade = int(input("Digite sua idade: "))

match idade:
    case x if x <= 12:
        print("Você é uma criança.")
    case x if x > 12 and x <= 17:
        print("Você é um adolescente.")
    case x if x > 17 and x <= 35:
        print("Você é um jovem.")
    case x if x > 35 and x <= 64:
        print("Você é um adulto.")
    case x if x > 65:
        print("Você é um idoso.")