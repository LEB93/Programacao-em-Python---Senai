# https://htmlcolorcodes.com/ site usado para consulta de cores, é bem legal.
# https://www.pygame.org/docs/ref/draw.html - Documentação Pygame

import pygame # modulo .draw é para tela

pygame.init()

tela  = pygame.display.set_mode((300,200))
pygame.display.set_caption('titulo')
run = True

while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run  = False

    tela.fill('#7500BD')
    pygame.draw.rect(tela,'#FFFCFF',(100,60,25,25))
    pygame.draw.circle(tela, ('#BD00A7'), (30,70), 25)
    pygame.draw.ellipse(tela,("#1600BD"), (200, 140, 30, 50))

    pygame.display.flip()
pygame.quit()  