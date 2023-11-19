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
SHELL_COLOR = (255, 0, 0)\
FPS = 10\
\
# Function to draw bars with numbers\
def draw_bars(screen, bars, highlight=None, shell_index=None):\
    screen.fill(BACKGROUND_COLOR)\
    font = pygame.font.Font(None, 36)\
\
    for i, height in enumerate(bars):\
        color = BAR_COLOR\
        if highlight and (i == highlight[0] or i == highlight[1]):\
            color = SHELL_COLOR  # Highlight for comparison\
        elif shell_index is not None and i % shell_index == 0:\
            color = SHELL_COLOR  # Highlight for shell gap\
        pygame.draw.rect(screen, color, (i * (WIDTH // len(bars)), HEIGHT - height, WIDTH // len(bars), height))\
\
        text = font.render(str(height), True, TEXT_COLOR)\
        text_rect = text.get_rect(center=(i * (WIDTH // len(bars)) + (WIDTH // len(bars)) // 2, HEIGHT - height // 2))\
        screen.blit(text, text_rect)\
\
# Shell Sort Algorithm\
def shell_sort(bars, screen):\
    n = len(bars)\
    gap = n // 2\
\
    while gap > 0:\
        for i in range(gap, n):\
            temp = bars[i]\
            j = i\
\
            while j >= gap and bars[j - gap] > temp:\
                bars[j] = bars[j - gap]\
                j -= gap\
\
            bars[j] = temp\
            draw_bars(screen, bars, highlight=(j, i), shell_index=gap)\
            pygame.display.flip()\
            pygame.time.delay(500)  # Delay for visualization\
\
        gap //= 2\
\
# Main function\
def main():\
    # Generate random bar heights\
    bars = [random.randint(50, 500) for _ in range(10)]\
\
    # Create Pygame window\
    screen = pygame.display.set_mode((WIDTH, HEIGHT))\
    pygame.display.set_caption("Shell Sort Visualization")\
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
        # Run shell sort algorithm\
        shell_sort(bars, screen)\
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