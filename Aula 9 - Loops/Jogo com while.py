import random

per = input('Dseseja jogar? sim ou não')

while per == 'sim':
    print('DIVINHE O NÚMERO: 🔢❓ ')
    numero = random.randrange(1,20000)
    escolha1 =  int(input('ecolha um número de 1 à 2000 --> '))

    if numero == escolha1:
        print('Você ganhou o jogo!🫵 😁 ')
        print('O numero aleatrorio é ', numero)
        break
    else:
        print('Errou feio! ☠️🧐')    
        print('O numero aleatrorio é ', numero)
        per = input('Deseja continuar? sim ou não')       

else:
    print('Até logo ')          