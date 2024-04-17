import pygame
import sys
import random

# const
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RAT_SIZE = 50
CHEESE_SIZE = 50
RAT_SPEED = 500
CHEESE_SPEED = 800
ORIGINAL_RAT_SIZE = 50


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# fotos bombásticas
rat_sprites = {
    "top": pygame.transform.scale(pygame.image.load("img/top.png"), (RAT_SIZE, RAT_SIZE)),
    "down": pygame.transform.scale(pygame.image.load("img/down.png"), (RAT_SIZE, RAT_SIZE)),
    "left": pygame.transform.scale(pygame.image.load("img/left.png"), (RAT_SIZE, RAT_SIZE)),
    "right": pygame.transform.scale(pygame.image.load("img/right.png"), (RAT_SIZE, RAT_SIZE))
}

# foto do queijo
cheese_image = pygame.transform.scale(pygame.image.load("img/queijo.png"), (CHEESE_SIZE, CHEESE_SIZE))

# lomba lomba
pygame.mixer.init()
pickup_sound = pygame.mixer.Sound("sfx/lombalomba.mp3")


font = pygame.font.Font(None, 36)



def generate_position():
    return random.randint(0, SCREEN_WIDTH - CHEESE_SIZE), random.randint(0, SCREEN_HEIGHT - CHEESE_SIZE)


# gerando o rato e sua veloc
rat_rect = pygame.Rect(300, 170, RAT_SIZE, RAT_SIZE)
last_direction = "top"
rat_positions = []
score = 0


cheese_position = generate_position()

# mag de queijo
thrown_cheeses = []

# foto da pitao
snake_image = pygame.transform.scale(pygame.image.load("img/boss1.png"), (RAT_SIZE * 6, RAT_SIZE * 6))

# posição da cobra
snake_rect = snake_image.get_rect()
snake_rect.midright = (SCREEN_WIDTH, SCREEN_HEIGHT // 2)


show_snake = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and score > 0:
                # atirar só se tiver lomba
                cheese_rect = rat_rect.copy()  # cpíando posição e tamanho do rato
                cheese_rect.inflate_ip(10, 10)  # aumentar queijo
                thrown_cheeses.append((cheese_rect, last_direction))  # guardar posição do queijo
                score -= 1  # jogando lombas
                # redefinir o tamanho do rato proporcionalmente à quantidade de lombas coletadas
                RAT_SIZE = max(ORIGINAL_RAT_SIZE, ORIGINAL_RAT_SIZE + score * 10)
                rat_sprites["top"] = pygame.transform.scale(pygame.image.load("img/top.png"), (RAT_SIZE, RAT_SIZE))
                rat_sprites["down"] = pygame.transform.scale(pygame.image.load("img/down.png"), (RAT_SIZE, RAT_SIZE))
                rat_sprites["left"] = pygame.transform.scale(pygame.image.load("img/left.png"), (RAT_SIZE, RAT_SIZE))
                rat_sprites["right"] = pygame.transform.scale(pygame.image.load("img/right.png"), (RAT_SIZE, RAT_SIZE))
                rat_rect = pygame.Rect(rat_rect.x, rat_rect.y, RAT_SIZE, RAT_SIZE)

    screen.fill("GREY") # pelo amor de deus deixa isso em gray

    # andando bombasticamente
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and last_direction != "down":
        last_direction = "top"
    elif keys[pygame.K_s] and last_direction != "top":
        last_direction = "down"
    elif keys[pygame.K_a] and last_direction != "right":
        last_direction = "left"
    elif keys[pygame.K_d] and last_direction != "left":
        last_direction = "right"

    # bombando sozinho
    if last_direction == "top":
        rat_rect.y -= RAT_SPEED * clock.get_time() / 1000
    elif last_direction == "down":
        rat_rect.y += RAT_SPEED * clock.get_time() / 1000
    elif last_direction == "left":
        rat_rect.x -= RAT_SPEED * clock.get_time() / 1000
    elif last_direction == "right":
        rat_rect.x += RAT_SPEED * clock.get_time() / 1000

    rat_rect.x = max(0, min(rat_rect.x, SCREEN_WIDTH - RAT_SIZE))
    rat_rect.y = max(0, min(rat_rect.y, SCREEN_HEIGHT - RAT_SIZE))

    # guardar a direção do rato
    screen.blit(rat_sprites[last_direction], rat_rect)

    # fazer o queijo funcionar
    for cheese_rect, direction in thrown_cheeses:
        if direction == "top":
            cheese_rect.y -= CHEESE_SPEED * clock.get_time() / 1000
        elif direction == "down":
            cheese_rect.y += CHEESE_SPEED * clock.get_time() / 1000
        elif direction == "left":
            cheese_rect.x -= CHEESE_SPEED * clock.get_time() / 1000
        elif direction == "right":
            cheese_rect.x += CHEESE_SPEED * clock.get_time() / 1000

        screen.blit(cheese_image, cheese_rect)

    # deixando o jogo leve
    thrown_cheeses = [(cheese_rect, direction) for cheese_rect, direction in thrown_cheeses if
                      cheese_rect.colliderect(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))]

    # acidente do rato com queijo
    if rat_rect.colliderect(pygame.Rect(cheese_position[0], cheese_position[1], CHEESE_SIZE, CHEESE_SIZE)):
        # *lonba lomba*
        pickup_sound.play()

        score += 1

        # 10 queijos
        if score >= 10:
            show_snake = True
            cheese_position = (-CHEESE_SIZE, -CHEESE_SIZE)
        else:
            cheese_position = generate_position()

        # engordando bombasticamente
        RAT_SIZE = max(ORIGINAL_RAT_SIZE, ORIGINAL_RAT_SIZE + score * 10)
        rat_sprites["top"] = pygame.transform.scale(pygame.image.load("img/top.png"), (RAT_SIZE, RAT_SIZE))
        rat_sprites["down"] = pygame.transform.scale(pygame.image.load("img/down.png"), (RAT_SIZE, RAT_SIZE))
        rat_sprites["left"] = pygame.transform.scale(pygame.image.load("img/left.png"), (RAT_SIZE, RAT_SIZE))
        rat_sprites["right"] = pygame.transform.scale(pygame.image.load("img/right.png"), (RAT_SIZE, RAT_SIZE))
        # ajuste na colision
        rat_rect = pygame.Rect(rat_rect.x, rat_rect.y, RAT_SIZE, RAT_SIZE)

        # gerar queijo se tiver menos que 10 lombas
        if score < 10:
            cheese_position = generate_position()

    # desenhando o queijo
    screen.blit(cheese_image, cheese_position)

    score_text = font.render(f"Lombas: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    if show_snake:
        screen.blit(snake_image, snake_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
