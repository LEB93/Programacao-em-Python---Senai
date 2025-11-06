# Em Python, o try e o except servem para tratar erros — ou seja, evitar que o seu programa pare de funcionar quando algo dá errado.
# Quando você coloca um código dentro de um bloco try, o Python tenta executá-lo.
# Se acontecer algum erro, em vez de o programa travar, o Python pula para o bloco except e executa o que estiver lá.

try:
    numero = int(input("Digite um número: "))
    print(f"O dobro do número é {numero * 2}")
except:
    print("Você não digitou um número válido!")

# O que acontece aqui:
# O Python tenta converter o que o usuário digitou em número (int(...)).
# Se o usuário digitar, por exemplo, “abc”, o Python daria erro — mas como usamos try e except, o programa mostra uma mensagem em vez de travar.

# Por que usar try e except?
# Evita que o programa feche por causa de um erro simples.
# Permite dar mensagens mais amigáveis para o usuário.
# Facilita o diagnóstico de erros.

# Exemplo da professora

def display():
    try:
        n  =  1/0
        n  = 10
        l = []
        print(l[10])
        x  = int(input('='))
        print(n + x)
        print("a")
    except NameError as erro:
        print(erro)   
    except ZeroDivisionError as erro:
        print(erro)   
    except ValueError as erro:
        print(erro)  
    except IndexError as erro:
        print(erro)            
    else:
        print('Ocorreu um erro não identificado')
    finally:
        print('fim de carregamento...')        

display()        