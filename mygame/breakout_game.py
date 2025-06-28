import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick em")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 60)

# Paddle settings
paddle_speed = 7

# Home screen function
def show_home_screen():
    while True:
        screen.fill(BLACK)
        title_text = font.render("Brick em", True, GREEN)
        start_text = pygame.font.SysFont(None, 40).render("Press SPACE to Start", True, WHITE)

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 60))
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # Start game

# Function to create bubbles
def create_bubbles(level):
    bubbles = []
    rows = 4 + level  # more rows each level
    cols = 8
    bubble_width = 80
    bubble_height = 30
    gap = 10

    for row in range(rows):
        for col in range(cols):
            x = col * (bubble_width + gap) + 35
            y = row * (bubble_height + gap) + 40
            bubbles.append(pygame.Rect(x, y, bubble_width, bubble_height))
    return bubbles

# Game loop
while True:
    show_home_screen()

    game_over = False  # track whether player lost

    # 5 level loop
    for level in range(1, 6):
        # Reset game objects
        paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 30, 120, 15)
        ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
        ball_speed_x = 3 + level
        ball_speed_y = -3 - level
        bubbles = create_bubbles(level)

        running = 