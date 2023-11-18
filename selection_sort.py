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
SELECT_COLOR = (255, 0, 0)\
FPS = 10\
\
# Function to draw bars with numbers\
def draw_bars(screen, bars, highlight=None, selected_index=None):\
    screen.fill(BACKGROUND_COLOR)\
    font = pygame.font.Font(None, 36)\
\
    for i, height in enumerate(bars):\
        color = BAR_COLOR\
        if highlight and (i == highlight[0] or i == highlight[1]):\
            color = SELECT_COLOR  # Highlight for comparison\
        elif selected_index is not None and i == selected_index:\
            color = SELECT_COLOR  # Highlight for selection\
        pygame.draw.rect(screen, color, (i * (WIDTH // len(bars)), HEIGHT - height, WIDTH // len(bars), height))\
\
        text = font.render(str(height), True, TEXT_COLOR)\
        text_rect = text.get_rect(center=(i * (WIDTH // len(bars)) + (WIDTH // len(bars)) // 2, HEIGHT - height // 2))\
        screen.blit(text, text_rect)\
\
# Selection Sort Algorithm\
def selection_sort(bars, screen):\
    for i in range(len(bars)):\
        min_index = i\
\
        for j in range(i + 1, len(bars)):\
            # Find the index of the minimum element\
            if bars[j] < bars[min_index]:\
                min_index = j\
\
            draw_bars(screen, bars, highlight=(i, j), selected_index=min_index)\
            pygame.display.flip()\
            pygame.time.delay(500)  # Delay for visualization\
\
        # Swap the found minimum element with the first element\
        bars[i], bars[min_index] = bars[min_index], bars[i]\
        draw_bars(screen, bars, selected_index=min_index)\
        pygame.display.flip()\
        pygame.time.delay(500)  # Delay for visualization\
\
# Main function\
def main():\
    # Generate random bar heights\
    bars = [random.randint(50, 500) for _ in range(10)]\
\
    # Create Pygame window\
    screen = pygame.display.set_mode((WIDTH, HEIGHT))\
    pygame.display.set_caption("Selection Sort Visualization")\
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
        # Run selection sort algorithm\
        selection_sort(bars, screen)\
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