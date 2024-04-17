import pygame
import sys
import random
from pygame.locals import *

# Constantes
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RAT_SIZE = 50
RAT_SPEED = 500
ORIGINAL_RAT_SIZE = 50  # Tamanho original do rato

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Carregar sprites do rato
rat_sprites = {
    "top": pygame.transform.scale(pygame.image.load("img/top.png"), (RAT_SIZE, RAT_SIZE)),
    "down": pygame.transform.scale(pygame.image.load("img/down.png"), (RAT_SIZE, RAT_SIZE)),
    "left": pygame.transform.scale(pygame.image.load("img/left.png"), (RAT_SIZE, RAT_SIZE)),
    "right": pygame.transform.scale(pygame.image.load("img/right.png"), (RAT_SIZE, RAT_SIZE))
}

# Carregar imagem da cobra
boss_image = pygame.transform.scale(pygame.image.load("img/boss1.png"), (RAT_SIZE * 2, RAT_SIZE * 2))

# Fonte para a pontuação
font = pygame.font.Font(None, 36)

# Posição inicial e velocidade da cobra
boss_rect = pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT // 2, RAT_SIZE * 2, RAT_SIZE * 2)
boss_speed = 200  # Velocidade de deslizamento da cobra

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("grey")

    # Atualizar a posição da cobra
    boss_rect.x -= boss_speed * clock.get_time() / 1000

    # Desenhar a cobra na tela
    screen.blit(boss_image, boss_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
