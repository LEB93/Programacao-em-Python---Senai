import pygame

# Inicializando o pygame
pygame.init()

# Definindo as cores
BLACK = ("#ff0070")
WHITE = ("#ff7446")

# Configurando a tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Pong')

# Configurando o relógio
clock = pygame.time.Clock()

# Definindo as variáveis do jogo
raquete_largura = 15
raquete_altura = 100
raquete_velocidade = 10

bola_raio = 10
bola_velocidade_x = 5
bola_velocidade_y = 5

# Posicionamento inicial das raquetes e bola
raquete_esquerda = pygame.Rect(30, (altura_tela // 2) - (raquete_altura // 2), raquete_largura, raquete_altura)
raquete_direita = pygame.Rect(largura_tela - 30 - raquete_largura, (altura_tela // 2) - (raquete_altura // 2), raquete_largura, raquete_altura)
bola = pygame.Rect(largura_tela // 2 - bola_raio, altura_tela // 2 - bola_raio, bola_raio * 2, bola_raio * 2)

# Função para desenhar o jogo
def desenhar_jogo():
    tela.fill(BLACK)  # Cor de fundo
    pygame.draw.rect(tela, WHITE, raquete_esquerda)  # Raquete esquerda
    pygame.draw.rect(tela, WHITE, raquete_direita)  # Raquete direita
    pygame.draw.ellipse(tela, WHITE, bola)  # A bola
    pygame.draw.aaline(tela, WHITE, (largura_tela // 2, 0), (largura_tela // 2, altura_tela))  # Linha central

# Função principal para o jogo
def main():
    global bola_velocidade_x, bola_velocidade_y

    run = True
    while run:
        clock.tick(60)  # 60 FPS
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False

        # Movimentação das raquetes
        keys = pygame.key.get_pressed()

        # Raquete esquerda
        if keys[pygame.K_w] and raquete_esquerda.top > 0:
            raquete_esquerda.y -= raquete_velocidade
        if keys[pygame.K_s] and raquete_esquerda.bottom < altura_tela:
            raquete_esquerda.y += raquete_velocidade

        # Raquete direita
        if keys[pygame.K_UP] and raquete_direita.top > 0:
            raquete_direita.y -= raquete_velocidade
        if keys[pygame.K_DOWN] and raquete_direita.bottom < altura_tela:
            raquete_direita.y += raquete_velocidade

        # Movimentação da bola
        bola.x += bola_velocidade_x
        bola.y += bola_velocidade_y

        # Colisões com o topo e fundo da tela
        if bola.top <= 0 or bola.bottom >= altura_tela:
            bola_velocidade_y *= -1

        # Colisão com as raquetes
        if bola.colliderect(raquete_esquerda) or bola.colliderect(raquete_direita):
            bola_velocidade_x *= -1

        # Se a bola sair pela esquerda ou direita (pontuação)
        if bola.left <= 0 or bola.right >= largura_tela:
            bola.x = largura_tela // 2 - bola_raio
            bola.y = altura_tela // 2 - bola_raio
            bola_velocidade_x *= -1
            bola_velocidade_y *= -1

        # Desenhando tudo
        desenhar_jogo()

        # Atualizando a tela
        pygame.display.flip()

    pygame.quit()

# Rodando o jogo
main()

