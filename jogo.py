import pygame
import random

# Inicialização do Pygame
pygame.init()

# Dimensões da tela
LARGURA = 600
ALTURA = 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Carro")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (200, 0, 0)

# Relógio
clock = pygame.time.Clock()
FPS = 60

# Carregar imagem do carro
carro_img = pygame.Surface((50, 100))
carro_img.fill(VERMELHO)

# Posição inicial do carro
carro_x = LARGURA // 2 - 25
carro_y = ALTURA - 120
velocidade_carro = 5

# Obstáculos
obstaculos = []
velocidade_obstaculo = 5
tamanho_obstaculo = (50, 100)

# Fonte
fonte = pygame.font.SysFont(None, 40)
pontos = 0

# Função para mostrar texto
def mostrar_texto(texto, x, y):
    img = fonte.render(texto, True, BRANCO)
    tela.blit(img, (x, y))

# Função para detectar colisão
def colidiu(rect1, rect2):
    return rect1.colliderect(rect2)

# Loop principal do jogo
rodando = True
while rodando:
    tela.fill(PRETO)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimentação
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and carro_x > 0:
        carro_x -= velocidade_carro
    if teclas[pygame.K_RIGHT] and carro_x < LARGURA - 50:
        carro_x += velocidade_carro

    # Criar obstáculos
    if random.randint(1, 30) == 1:
        obst_x = random.randint(0, LARGURA - 50)
        obstaculos.append(pygame.Rect(obst_x, -100, 50, 100))

    # Mover obstáculos
    for obst in obstaculos[:]:
        obst.y += velocidade_obstaculo
        pygame.draw.rect(tela, BRANCO, obst)

        if obst.y > ALTURA:
            obstaculos.remove(obst)
            pontos += 1

        # Colisão
        carro_rect = pygame.Rect(carro_x, carro_y, 50, 100)
        if colidiu(carro_rect, obst):
            mostrar_texto("Game Over!", LARGURA//2 - 100, ALTURA//2)
            pygame.display.update()
            pygame.time.wait(2000)
            rodando = False

    # Desenhar carro
    tela.blit(carro_img, (carro_x, carro_y))

    # Mostrar pontuação
    mostrar_texto(f"Pontos: {pontos}", 10, 10)

    # Atualizar tela
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
