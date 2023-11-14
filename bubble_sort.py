import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
BAR_COLOR = (0, 0, 255)
TEXT_COLOR = (255, 255, 255)
SWAP_COLOR = (255, 0, 0)
FPS = 10  # Reduced the frames per second for smoother animation

# Function to draw bars with numbers
def draw_bars(screen, bars, highlight=None):
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 36)

    for i, height in enumerate(bars):
        color = BAR_COLOR
        if highlight and (i == highlight[0] or i == highlight[1]):
            color = SWAP_COLOR
        pygame.draw.rect(screen, color, (i * (WIDTH // len(bars)), HEIGHT - height, WIDTH // len(bars), height))

        text = font.render(str(height), True, TEXT_COLOR)
        text_rect = text.get_rect(center=(i * (WIDTH // len(bars)) + (WIDTH // len(bars)) // 2, HEIGHT - height // 2))
        screen.blit(text, text_rect)

# Bubble Sort Algorithm
def bubble_sort(bars, screen):
    n = len(bars)
    for i in range(n):
        for j in range(0, n-i-1):
            # Draw bars with highlight for comparison
            draw_bars(screen, bars, highlight=(j, j+1))
            pygame.display.flip()
            pygame.time.delay(500)  # Delay for visualization

            if bars[j] > bars[j+1]:
                # Swap bars
                bars[j], bars[j+1] = bars[j+1], bars[j]
                # Draw bars with highlight for swap
                draw_bars(screen, bars, highlight=(j, j+1))
                pygame.display.flip()
                pygame.time.delay(500)  # Delay for visualization

# Main function
def main():
    # Generate random bar heights
    bars = [random.randint(50, 500) for _ in range(10)]

    # Create Pygame window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bubble Sort Visualization")

    # Main loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Run bubble sort algorithm
        bubble_sort(bars, screen)

        # Draw final state
        draw_bars(screen, bars)
        pygame.display.flip()

        # Wait for user to close the window
        pygame.time.delay(2000)
        running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
