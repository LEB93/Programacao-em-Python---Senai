# Claro! O loop while é uma estrutura de repetição em programação que executa um bloco de código enquanto uma determinada condição for verdadeira.
# É um loop infinito, mas que pode ser parada precisa de um contator.

n = 0
while n <= 10:
    print(n)
    n = n + 1

#Como funciona:

# Avaliação da condição: Antes de cada iteração, o Python verifica se a condição especificada é verdadeira ou falsa.
# Execução do código: Se a condição for verdadeira, o código dentro do bloco while é executado.
# Repetição: Após a execução, a condição é verificada novamente. Se continuar verdadeira, o bloco de código será executado novamente.
# Interrupção: Quando a condição se torna falsa, o loop é interrompido e o programa segue para o próximo código após o loop.

# Exemplo simples:
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Explicação: Nesse exemplo, o loop começa com contador igual a 0 e continua enquanto contador for menor que 5.
# A cada iteração, o valor de contador aumenta de 1. Quando contador chega a 5, a condição contador < 5 se torna falsa, e o loop é interrompido.
# É importante garantir que a condição eventualmente se torne falsa, caso contrário, o loop pode se tornar um loop infinito, 
# o que significa que o código nunca vai parar de rodar!