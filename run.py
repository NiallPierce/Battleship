import random

# Ship class to represent individual ships with a size, number of hits, and coordinates
class Ship:
    def __init__(self, size):
        self.size = size      # Size of the ship (e.g., 3 for a 3-unit ship)
        self.hits = 0         # Track the number of times the ship has been hit
        self.coordinates = [] # List to store the ship's position (coordinates)

    # Place the ship on the grid based on the given starting row, column, and orientation (horizontal or vertical)
    def place_ship(self, grid, row, col, orientation):
        self.coordinates = []  # Reset the coordinates list
        if orientation == 'H': # If orientation is horizontal
            for i in range(self.size):
                self.coordinates.append((row, col + i)) # Add each coordinate to the right
        elif orientation == 'V': # If orientation is vertical
            for i in range(self.size):
                self.coordinates.append((row + i, col)) # Add each coordinate downwards

# GameState class to manage the state of the game
class GameState:
    def __init__(self):
        self.player_turn = True # Boolean to track if it's the player's turn
        self.game_over = False  # Boolean to check if the game is over
        self.player_ships = []  # List to hold player's ships
        self.ai_ships = []      # List to hold AI's ships

# Function to create a 10x10 grid for the game, filled with "路" (empty water)
def create_grid():
    return [["-"] * 10 for _ in range(10)]

# Function to print the game grid. Optionally, hide the ships by displaying "路" instead of "S"
def print_grid(grid, hide_ships=False):
    print("  1 2 3 4 5 6 7 8 9 10")  # Print column numbers
    for i, row in enumerate(grid):
        print(chr(65 + i), end=" ")  # Print row letters (A-J)
        for cell in row:
            if hide_ships and cell == "S":  # Hide ships if the flag is set
                print("-", end=" ")
            else:
                print(cell, end=" ")
        print()
