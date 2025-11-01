import random 

ppt_m =  ['🪨','🧻','✂️'] # ppt_m = pedra, papel, tesoura da máquina
ppt_usuario =  ['🪨','🧻','✂️'] # ppt_usuário = pedra, papel, tesoura do usuário, o que ele escolherá

maquina =  random.choice(ppt_m)
escolha =  int(input('''
0 - 🪨
1 - 🧻
2 - ✂️                                          
'''))

if maquina == ppt_usuario[escolha]:
    print('EMPATE')
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)    

elif maquina == '🪨'  and ppt_usuario[escolha] =='✂️':
    print('O computador ganhou')  
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)

elif maquina == '✂️'   and ppt_usuario[escolha] =='🧻':
    print('O computador ganhou')  
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)    
elif maquina == '🧻'   and ppt_usuario[escolha] =='🪨':
    print('O computador ganhou')   
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)

elif ppt_usuario[escolha] == '🪨'   and maquina =='✂️':
    print('Você ganhou!')  
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)

elif ppt_usuario[escolha] == '✂️'   and maquina =='🧻':
    print('Você ganhou!')  
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)    

elif ppt_usuario[escolha] == '🧻'   and maquina =='🪨':
    print('Você ganhou!')
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)    

else:
    print('Digite algo válido')    