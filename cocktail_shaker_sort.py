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
SHAKER_COLOR = (255, 0, 0)\
FPS = 10\
\
# Function to draw bars with numbers\
def draw_bars(screen, bars, highlight=None, shaker_index=None):\
    screen.fill(BACKGROUND_COLOR)\
    font = pygame.font.Font(None, 36)\
\
    for i, height in enumerate(bars):\
        color = BAR_COLOR\
        if highlight and (i == highlight[0] or i == highlight[1]):\
            color = SHAKER_COLOR  # Highlight for comparison\
        elif shaker_index is not None and i == shaker_index:\
            color = SHAKER_COLOR  # Highlight for shaker movement\
        pygame.draw.rect(screen, color, (i * (WIDTH // len(bars)), HEIGHT - height, WIDTH // len(bars), height))\
\
        text = font.render(str(height), True, TEXT_COLOR)\
        text_rect = text.get_rect(center=(i * (WIDTH // len(bars)) + (WIDTH // len(bars)) // 2, HEIGHT - height // 2))\
        screen.blit(text, text_rect)\
\
# Cocktail Shaker Sort Algorithm\
def cocktail_shaker_sort(bars, screen):\
    n = len(bars)\
    swapped = True\
    start = 0\
    end = n-1\
\
    while (swapped == True):\
        # Reset the swapped flag on entering the loop,\
        # because it might be true from a previous\
        # swap.\
        swapped = False\
\
        # Loop from left to right same as the bubble\
        # sort\
        for i in range(start, end):\
            if (bars[i] > bars[i + 1]):\
                bars[i], bars[i + 1] = bars[i + 1], bars[i]\
                draw_bars(screen, bars, highlight=(i, i + 1), shaker_index=i + 1)\
                pygame.display.flip()\
                pygame.time.delay(500)  # Delay for visualization\
                swapped = True\
\
        # If nothing moved, then array is sorted.\
        if (swapped == False):\
            break\
\
        # Otherwise, reset the swapped flag so that it\
        # can be used in the next stage\
        swapped = False\
\
        # Decrement the end point, because the last\
        # element is in its rightful spot.\
        end = end-1\
\
        # From right to left, doing the same\
        # comparison as in the previous stage\
        for i in range(end-1, start-1, -1):\
            if (bars[i] > bars[i + 1]):\
                bars[i], bars[i + 1] = bars[i + 1], bars[i]\
                draw_bars(screen, bars, highlight=(i, i + 1), shaker_index=i + 1)\
                pygame.display.flip()\
                pygame.time.delay(500)  # Delay for visualization\
                swapped = True\
\
        # Increment the starting point, because\
        # the last element is in its rightful spot.\
        start = start + 1\
\
# Main function\
def main():\
    # Generate random bar heights\
    bars = [random.randint(50, 500) for _ in range(10)]\
\
    # Create Pygame window\
    screen = pygame.display.set_mode((WIDTH, HEIGHT))\
    pygame.display.set_caption("Cocktail Shaker Sort Visualization")\
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
        # Run cocktail shaker sort algorithm\
        cocktail_shaker_sort(bars, screen)\
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