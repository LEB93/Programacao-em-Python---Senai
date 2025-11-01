import random

perguntas = ["Carregue novamente","O que é o que é: quanto mais você tira, maior fica?","O que é o que é: tem dentes, mas não morde?","O que é o que é: passa diante do sol e não faz sombra?","O que é o que é: anda com os pés na cabeça?","O que é o que é: vive no mar, é redondo e vive dizendo “Oi”?"]
respostas = ["","1 - Um buraco.", "2 - Um pente.", "3 - O vento.", "4 - O piolho.", "5 - O polvo!"]

pergunta_aleatoria = random.choice(perguntas) # random.choice escolhe aleatoriamente apenas 1 valor da lista.
indice = perguntas.index(pergunta_aleatoria) # .index identifica o indice da escolha aleatória apresentada

print(f'''
      PERGUNTA...
      {pergunta_aleatoria}
      ''')

resposta_user = int(input(f'''
{respostas[1]}
{respostas[2]}
{respostas[3]}
{respostas[4]}
{respostas[5]}                        
Qual é sua escolha?: '''))

if indice == resposta_user:
    print("Você acertou")
else:
    print("Errou")