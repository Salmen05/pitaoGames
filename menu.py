import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definições de tela
WIDTH = 1280
HEIGHT = 720
FPS = 30

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

# Inicialização da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lomba Lomba RUSH")
clock = pygame.time.Clock()

# Carregar imagem de fundo
background_image = pygame.image.load("img/background.png").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Carregar música de fundo
pygame.mixer.music.load("music/background_music.mp3")
pygame.mixer.music.play(-1)  # -1 para tocar em loop


# Classe para botões
class Button:
    def __init__(self, x, y, width, height, text, text_color, button_color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.button_color = button_color
        self.hover_color = hover_color
        self.action = action

    def draw(self, surface):
        # Verificar se o mouse está sobre o botão
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.button_color, self.rect)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# Função para o menu de escolha
def menu():
    button_width = 200
    button_height = 50
    button_x = (WIDTH - button_width) // 2

    buttons = []
    # Adicionando botões para as opções
    options = ["New Game", "Options", "Exit"]
    for i, option in enumerate(options):
        # Ajuste de posição y dos botões para a parte inferior da tela
        button_y = HEIGHT - 50 - len(options) * (button_height + 20) + i * (button_height + 20)
        button = Button(button_x, button_y, button_width, button_height, option, BLACK, WHITE, GRAY, option.lower())
        buttons.append(button)

    while True:
        # Desenhar imagem de fundo
        screen.blit(background_image, (0, 0))

        # Desenhar botões
        for button in buttons:
            button.draw(screen)

        pygame.display.flip()

        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Verificar se o clique foi em um botão
                for button in buttons:
                    if button.is_clicked(mouse_pos):
                        if button.action == "exit":
                            pygame.quit()
                            sys.exit()
                        else:
                            print(f"Você selecionou a opção: {button.text}")
                            # Aqui você pode chamar a função correspondente à opção selecionada
                            # Por exemplo, se for a "New Game", você pode chamar uma função para iniciar o jogo principal
                            # Ou se for "Options", você pode chamar uma função para exibir as opções do jogo, etc.
                            # Substitua o print acima com chamadas de função apropriadas.


# Função principal
def main():
    menu()


if __name__ == "__main__":
    main()
