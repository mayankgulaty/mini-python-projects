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
PIVOT_COLOR = (255, 0, 0)
FPS = 10

# Function to draw bars with numbers
def draw_bars(screen, bars, pivot_index=None, highlight=None):
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 36)

    for i, height in enumerate(bars):
        color = BAR_COLOR
        if pivot_index is not None and i == pivot_index:
            color = PIVOT_COLOR
        elif highlight and (i == highlight[0] or i == highlight[1]):
            color = PIVOT_COLOR  # Highlight for comparison
        pygame.draw.rect(screen, color, (i * (WIDTH // len(bars)), HEIGHT - height, WIDTH // len(bars), height))

        text = font.render(str(height), True, TEXT_COLOR)
        text_rect = text.get_rect(center=(i * (WIDTH // len(bars)) + (WIDTH // len(bars)) // 2, HEIGHT - height // 2))
        screen.blit(text, text_rect)

# Quicksort Algorithm
def quicksort(bars, screen, low=0, high=None):
    if high is None:
        high = len(bars) - 1

    if low < high:
        # Partition the array, get pivot index
        pivot_index = partition(bars, screen, low, high)

        # Recursively sort the sub-arrays
        quicksort(bars, screen, low, pivot_index - 1)
        quicksort(bars, screen, pivot_index + 1, high)

# Partition helper function
def partition(bars, screen, low, high):
    pivot_index = low
    pivot_value = bars[high]

    for i in range(low, high):
        draw_bars(screen, bars, pivot_index, highlight=(i, high))
        pygame.display.flip()
        pygame.time.delay(500)  # Delay for visualization

        if bars[i] < pivot_value:
            bars[i], bars[pivot_index] = bars[pivot_index], bars[i]
            pivot_index += 1

    bars[pivot_index], bars[high] = bars[high], bars[pivot_index]
    draw_bars(screen, bars, pivot_index)
    pygame.display.flip()
    pygame.time.delay(500)  # Delay for visualization

    return pivot_index

# Main function
def main():
    # Generate random bar heights
    bars = [random.randint(50, 500) for _ in range(10)]

    # Create Pygame window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Quicksort Visualization")

    # Main loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Run quicksort algorithm
        quicksort(bars, screen)

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
