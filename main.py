import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

rat = pygame.image.load("img/topDown.png")
width, height = rat.get_rect().size
ratColision = rat.get_rect(x=300, y=170)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rat = pygame.image.load("img/topDown.png")
        ratColision.y -= 300 * dt
    if keys[pygame.K_s]:
        rat = pygame.image.load("img/topDown.png")
        ratColision.y += 300 * dt
    if keys[pygame.K_a]:
        rat = pygame.image.load("img/rightLeft.png")
        ratColision.x -= 300 * dt
    if keys[pygame.K_d]:
        rat = pygame.image.load("img/rightLeft.png")
        ratColision.x += 300 * dt

    screen.blit(rat, ratColision)
    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()
