import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control the frame rate
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 35)

# Snake variables
snake_size = 1
snake_speed = GRID_SIZE
snake_direction = (1, 0)  # Initial direction (right)
snake_segments = [(WIDTH // 2, HEIGHT // 2)]

# Food variables
food_position = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                 random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

def draw_snake():
    for segment in snake_segments:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (food_position[0], food_position[1], GRID_SIZE, GRID_SIZE))

def game_over():
    text = font.render('Game Over', True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def main():
    global snake_size
    global food_position
    global snake_direction

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        # Move the snake
        new_head = (snake_segments[0][0] + snake_direction[0] * snake_speed,
                    snake_segments[0][1] + snake_direction[1] * snake_speed)

        # Check for collisions with walls or itself
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake_segments[1:]):
            game_over()

        snake_segments.insert(0, new_head)

        # Check for collision with food
        if new_head == food_position:
            snake_size += 1
            food_position = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                             random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
        else:
            # If no collision with food, remove the last segment
            snake_segments.pop()

        # Draw everything
        screen.fill((0, 0, 0))
        draw_snake()
        draw_food()

        # Display score
        score_text = font.render(f'Score: {snake_size - 1}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
