import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# --- Configurações da tela ---
LARGURA = 600
ALTURA = 400
TAMANHO_CELULA = 20
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("🐍 Snake Game")

# --- Cores ---
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# --- Fonte ---
fonte = pygame.font.SysFont("Arial", 25)

# --- Função para desenhar a cobrinha ---
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, VERDE, (pixel[0], pixel[1], tamanho, tamanho))

# --- Função para mostrar mensagem ---
def mostrar_mensagem(texto, cor, tamanho=30):
    fonte_local = pygame.font.SysFont("Arial", tamanho)
    mensagem = fonte_local.render(texto, True, cor)
    rect = mensagem.get_rect(center=(LARGURA // 2, ALTURA // 2))
    tela.blit(mensagem, rect)

# --- Função principal ---
def jogar():
    # Posição inicial da cobra
    x = LARGURA // 2
    y = ALTURA // 2
    velocidade_x = 0
    velocidade_y = 0

    # Corpo da cobra
    corpo_cobra = []
    comprimento_inicial = 1

    # Comida
    comida_x = round(random.randrange(0, LARGURA - TAMANHO_CELULA) / 20.0) * 20
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_CELULA) / 20.0) * 20

    # Pontuação
    pontos = 0

    # Controle de tempo
    clock = pygame.time.Clock()
    rodando = True
    game_over = False

    while rodando:
        while game_over:
            tela.fill(PRETO)
            mostrar_mensagem("GAME OVER 😵", VERMELHO, 40)
            mostrar_mensagem(f"Pontuação: {pontos}", BRANCO, 25)
            mostrar_mensagem("Pressione ENTER para jogar de novo ou ESC para sair", BRANCO, 20)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # ENTER para reiniciar
                        jogar()
                    if event.key == pygame.K_ESCAPE:  # ESC para sair
                        rodando = False
                        game_over = False

        # Eventos de movimento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x == 0:
                    velocidade_x = -TAMANHO_CELULA
                    velocidade_y = 0
                elif event.key == pygame.K_RIGHT and velocidade_x == 0:
                    velocidade_x = TAMANHO_CELULA
                    velocidade_y = 0
                elif event.key == pygame.K_UP and velocidade_y == 0:
                    velocidade_y = -TAMANHO_CELULA
                    velocidade_x = 0
                elif event.key == pygame.K_DOWN and velocidade_y == 0:
                    velocidade_y = TAMANHO_CELULA
                    velocidade_x = 0

        # Atualiza a posição
        x += velocidade_x
        y += velocidade_y

        # Verifica colisões com bordas
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            game_over = True

        # Atualiza corpo da cobra
        corpo_cobra.append([x, y])
        if len(corpo_cobra) > comprimento_inicial:
            del corpo_cobra[0]

        # Verifica colisão com o próprio corpo
        for parte in corpo_cobra[:-1]:
            if parte == [x, y]:
                game_over = True

        # Desenha fundo e objetos
        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, (comida_x, comida_y, TAMANHO_CELULA, TAMANHO_CELULA))
        desenhar_cobra(TAMANHO_CELULA, corpo_cobra)

        # Mostra pontuação
        texto_pontos = fonte.render(f"Pontuação: {pontos}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))

        pygame.display.update()

        # Cobra come a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, LARGURA - TAMANHO_CELULA) / 20.0) * 20
            comida_y = round(random.randrange(0, ALTURA - TAMANHO_CELULA) / 20.0) * 20
            comprimento_inicial += 1
            pontos += 10

        # Controla velocidade (quanto menor, mais rápido)
        clock.tick(10)

    pygame.quit()
    sys.exit()

# --- Iniciar o jogo ---
jogar()
