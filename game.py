import pygame
import numpy as np
import time

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (in pixels)
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600

# Set the dimensions of the grid (number of rows and columns)
GRID_SIZE = 50
def greet(name):
	print("Hello, " + name + "!")

greet("Alex")

CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game grid
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Define the initial state of the grid (for testing)
# Example: Blinker
grid[5, 4:7] = 1

# Define the initial state of the grid (for testing)
# Example: Glider
# grid[1:4, 1] = 1
# grid[2, 2:4] = 1
# grid[0, 3] = 1

# Function to update the grid based on the rules of Conway's Game of Life
def update_grid(grid):
    new_grid = np.copy(grid)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            neighbors = np.sum(grid[max(0, i-1):min(GRID_SIZE, i+2), max(0, j-1):min(GRID_SIZE, j+2)]) - grid[i, j]
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1
    return new_grid

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the grid
    grid = update_grid(grid)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the grid
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, WHITE, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the display
    pygame.display.flip()

    # Add a short delay
    time.sleep(0.1)

# Quit Pygame
pygame.quit()
