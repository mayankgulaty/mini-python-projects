{\rtf1\ansi\ansicpg1252\cocoartf2758
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pygame\
import random\
import sys\
\
# Initialize Pygame\
pygame.init()\
\
# Constants\
WIDTH, HEIGHT = 800, 600\
BACKGROUND_COLOR = (255, 255, 255)\
BAR_COLOR = (0, 0, 255)\
TEXT_COLOR = (255, 255, 255)\
HEAP_COLOR = (255, 0, 0)\
FPS = 10\
\
# Function to draw bars with numbers\
def draw_bars(screen, bars, highlight=None, heapify_index=None, sorted_index=None):\
    screen.fill(BACKGROUND_COLOR)\
    font = pygame.font.Font(None, 36)\
\
    for i, height in enumerate(bars):\
        color = BAR_COLOR\
        if highlight and (i == highlight[0] or i == highlight[1]):\
            color = HEAP_COLOR  # Highlight for comparison\
        elif heapify_index is not None and i == heapify_index:\
            color = HEAP_COLOR  # Highlight for heapify\
        elif sorted_index is not None and i >= sorted_index:\
            color = HEAP_COLOR  # Highlight for sorted elements\
        pygame.draw.rect(screen, color, (i * (WIDTH // len(bars)), HEIGHT - height, WIDTH // len(bars), height))\
\
        text = font.render(str(height), True, TEXT_COLOR)\
        text_rect = text.get_rect(center=(i * (WIDTH // len(bars)) + (WIDTH // len(bars)) // 2, HEIGHT - height // 2))\
        screen.blit(text, text_rect)\
\
# Heapify the subtree rooted at index i.\
def heapify(bars, screen, n, i):\
    largest = i  # Initialize largest as root\
    left_child = 2 * i + 1\
    right_child = 2 * i + 2\
\
    # Check if left child of root exists and is greater than the root\
    if left_child < n and bars[largest] < bars[left_child]:\
        largest = left_child\
\
    # Check if right child of root exists and is greater than the largest so far\
    if right_child < n and bars[largest] < bars[right_child]:\
        largest = right_child\
\
    # Change root if needed\
    if largest != i:\
        bars[i], bars[largest] = bars[largest], bars[i]\
        draw_bars(screen, bars, highlight=(i, largest), heapify_index=i)\
        pygame.display.flip()\
        pygame.time.delay(500)  # Delay for visualization\
        heapify(bars, screen, n, largest)\
\
# Heap Sort Algorithm\
def heap_sort(bars, screen):\
    n = len(bars)\
\
    # Build a max heap\
    for i in range(n // 2 - 1, -1, -1):\
        heapify(bars, screen, n, i)\
\
    # Extract elements one by one\
    for i in range(n - 1, 0, -1):\
        bars[i], bars[0] = bars[0], bars[i]\
        draw_bars(screen, bars, highlight=(0, i), sorted_index=n - i)\
        pygame.display.flip()\
        pygame.time.delay(500)  # Delay for visualization\
        heapify(bars, screen, i, 0)\
\
# Main function\
def main():\
    # Generate random bar heights\
    bars = [random.randint(50, 500) for _ in range(10)]\
\
    # Create Pygame window\
    screen = pygame.display.set_mode((WIDTH, HEIGHT))\
    pygame.display.set_caption("Heap Sort Visualization")\
\
    # Main loop\
    running = True\
    clock = pygame.time.Clock()\
\
    while running:\
        for event in pygame.event.get():\
            if event.type == pygame.QUIT:\
                running = False\
\
        # Run heap sort algorithm\
        heap_sort(bars, screen)\
\
        # Draw final state\
        draw_bars(screen, bars)\
        pygame.display.flip()\
\
        # Wait for user to close the window\
        pygame.time.delay(2000)\
        running = False\
\
    pygame.quit()\
    sys.exit()\
\
if __name__ == "__main__":\
    main()\
}