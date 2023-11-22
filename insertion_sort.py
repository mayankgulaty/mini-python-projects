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
INSERT_COLOR = (255, 0, 0)
FPS = 10

# Function to draw bars with numbers
def draw_bars(screen, bars, highlight=None, insert_index=None):
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 36)

    for i, height in enumerate(bars):
        color = BAR_COLOR
        if highlight and (i == highlight[0] or i == highlight[1]):
            color = INSERT_COLOR  # Highlight for comparison
        elif insert_index is not None and i == insert_index:
            color = INSERT_COLOR  # Highlight for insertion
        pygame.draw.rect(screen, color, (i * (WIDTH // len(bars)), HEIGHT - height, WIDTH // len(bars), height))

        text = font.render(str(height), True, TEXT_COLOR)
        text_rect = text.get_rect(center=(i * (WIDTH // len(bars)) + (WIDTH // len(bars)) // 2, HEIGHT - height // 2))
        screen.blit(text, text_rect)

# Insertion Sort Algorithm
def insertion_sort(bars, screen):
    for i in range(1, len(bars)):
        key = bars[i]
        j = i - 1

        while j >= 0 and key < bars[j]:
            # Move the elements greater than key one position ahead
            bars[j + 1] = bars[j]
            draw_bars(screen, bars, highlight=(j, j + 1), insert_index=j + 1)
            pygame.display.flip()
            pygame.time.delay(500)  # Delay for visualization
            j -= 1

        bars[j + 1] = key
        draw_bars(screen, bars, insert_index=j + 1)
        pygame.display.flip()
        pygame.time.delay(500)  # Delay for visualization

# Main function
def main():
    # Generate random bar heights
    bars = [random.randint(50, 500) for _ in range(10)]

    # Create Pygame window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Insertion Sort Visualization")

    # Main loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Run insertion sort algorithm
        insertion_sort(bars, screen)

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
