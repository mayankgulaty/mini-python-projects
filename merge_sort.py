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
MERGED_COLOR = (0, 255, 0)
FPS = 10

# Function to draw bars with numbers
def draw_bars(screen, bars, highlight=None, merged=None):
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 36)

    for i, height in enumerate(bars):
        color = BAR_COLOR
        if highlight and (i == highlight[0] or i == highlight[1]):
            color = MERGED_COLOR  # Highlight for the merged portion
        elif merged and i in range(merged[0], merged[1] + 1):
            color = MERGED_COLOR  # Color bars that are being merged
        pygame.draw.rect(screen, color, (i * (WIDTH // len(bars)), HEIGHT - height, WIDTH // len(bars), height))

        text = font.render(str(height), True, TEXT_COLOR)
        text_rect = text.get_rect(center=(i * (WIDTH // len(bars)) + (WIDTH // len(bars)) // 2, HEIGHT - height // 2))
        screen.blit(text, text_rect)

# Merge Sort Algorithm
def merge_sort(bars, screen, start=0, end=None):
    if end is None:
        end = len(bars) - 1

    if start < end:
        mid = (start + end) // 2

        # Recursively sort both halves
        merge_sort(bars, screen, start, mid)
        merge_sort(bars, screen, mid + 1, end)

        # Merge the sorted halves
        merge(bars, screen, start, mid, end)

# Merge helper function
def merge(bars, screen, start, mid, end):
    left = bars[start:mid+1]
    right = bars[mid+1:end+1]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            bars[k] = left[i]
            i += 1
        else:
            bars[k] = right[j]
            j += 1
        draw_bars(screen, bars, highlight=(start, end), merged=(k-i, k))
        pygame.display.flip()
        pygame.time.delay(500)  # Delay for visualization
        k += 1

    while i < len(left):
        bars[k] = left[i]
        i += 1
        k += 1
        draw_bars(screen, bars, highlight=(start, end), merged=(k-i, k))
        pygame.display.flip()
        pygame.time.delay(500)  # Delay for visualization

    while j < len(right):
        bars[k] = right[j]
        j += 1
        k += 1
        draw_bars(screen, bars, highlight=(start, end), merged=(k-j, k))
        pygame.display.flip()
        pygame.time.delay(500)  # Delay for visualization

# Main function
def main():
    # Generate random bar heights
    bars = [random.randint(50, 500) for _ in range(10)]

    # Create Pygame window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Merge Sort Visualization")

    # Main loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Run merge sort algorithm
        merge_sort(bars, screen)

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
