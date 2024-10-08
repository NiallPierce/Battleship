import random


# Ship class to represent each ship with a size, hits, and coordinates
class Ship:
    def __init__(self, size):
        self.size = size      # Size of the ship (e.g., 3 for a 3-unit ship)
        self.hits = 0         # Track the number of times the ship has been hit
        self.coordinates = []  # List to store the ship's position

    def place_ship(self, grid, row, col, orientation):
        self.coordinates = []  # Reset the coordinates list
        if orientation == 'H':
            for i in range(self.size):
                self.coordinates.append((row, col + i))
        elif orientation == 'V':
            for i in range(self.size):
                self.coordinates.append((row + i, col))


# GameState class to manage the state of the game
class GameState:
    def __init__(self):
        self.player_turn = True
        self.game_over = False
        self.player_ships = []
        self.ai_ships = []


# Function to create a 10x10 grid for the game, filled with "-" (empty water)
def create_grid():
    return [["-"] * 10 for _ in range(10)]


# Function to print the game grid
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


# Function to check if a ship can be placed on the grid at the given position
def is_valid_placement(grid, ship, row, col, orientation):
    # Check if the ship goes out of bounds horizontally or vertically
    if orientation == 'H' and col + ship.size > 10:
        return False
    if orientation == 'V' and row + ship.size > 10:
        return False
    # Check if the ship overlaps with another ship on the grid
    for i in range(ship.size):
        if orientation == 'H':  # For horizontal placement
            if grid[row][col + i] != "-":
                return False
        elif orientation == 'V':  # For vertical placement
            if grid[row + i][col] != "-":
                return False
    return True  # Placement is valid


# Function for AI to randomly place its ships on the grid
def place_ai_ships(grid, ships):
    for ship in ships:
        while True:  # Repeat until a valid placement is found
            row = random.randint(0, 9)  # Random row (0-9)
            col = random.randint(0, 9)  # Random column (0-9)
            orientation = random.choice(['H', 'V'])  # Random orientation
            if is_valid_placement(grid, ship, row, col, orientation):
                ship.place_ship(grid, row, col, orientation)  # Place the ship
                for coord in ship.coordinates:
                    grid[coord[0]][coord[1]] = "S"  # Mark the ship's location
                break  # Exit loop when a valid placement is done


# Function to handle the player's turn
def player_turn(grid, ships):
    while True:  # Loop until the player makes a valid move
        try:
            move = input("Enter your move (e.g., A5): ").upper()
            row = ord(move[0]) - 65  # Convert letter (A-J) to row index
            col = int(move[1:]) - 1  # Convert number (1-10) to column index
            # Check if the move is out of bounds or already guessed
            if row < 0 or row > 9 or col < 0 or col > 9:
                raise ValueError
            if grid[row][col] in ["X", "M"]:
                print("You already guessed that one. Try again.")
                continue
            break
        except (ValueError, IndexError):  # Catch invalid input
            print(
                "Invalid input. Please enter a letter followed by a number "
                "(1-10)."
            )

    # Check if the player's move hits any AI ship
    hit = False
    for ship in ships:
        if (row, col) in ship.coordinates:
            grid[row][col] = "X"  # Mark a hit on the grid
            ship.hits += 1  # Increment the ship's hit count
            hit = True
            if ship.hits == ship.size:  # Check if the ship is sunk
                print(f"You sunk AI's {ship.size}-unit ship!")
            else:
                print("Hit!")
            break
    if not hit:  # If no hit, mark a miss
        grid[row][col] = "M"
        print("Miss!")

    return hit  # Return whether the move was a hit or not


# Function to handle the AI's turn
def ai_turn(grid, ships):
    while True:  # AI randomly chooses a move
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if grid[row][col] not in ["X", "M"]:
            break

    # Check if the AI's move hits any player's ship
    hit = False
    for ship in ships:
        if (row, col) in ship.coordinates:
            grid[row][col] = "X"  # Mark a hit on the grid
            ship.hits += 1  # Increment the ship's hit count
            hit = True
            if ship.hits == ship.size:  # Check if the ship is sunk
                print(f"AI sunk your {ship.size}-unit ship!")
            else:
                print("AI Hit!")
            break
    if not hit:  # If no hit, mark a miss
        grid[row][col] = "M"
        print("AI Miss!")

    return hit  # Return whether the move was a hit or not


# Function to check if all ships in the list are sunk (game over condition)
def check_game_over(ships):
    return all(ship.hits == ship.size for ship in ships)


# Function to place player's ships manually by asking for input
def place_player_ships(grid, ships):
    for ship in ships:
        while True:  # Repeat until a valid placement is found
            print_grid(grid)  # Show current grid
            print(f"Placing {ship.size}-unit ship")
            try:
                # Ask for the starting position and orientation of the ship
                location = input("Enter start position (e.g A5): ").upper()
                row = ord(location[0]) - 65
                col = int(location[1:]) - 1
                orientation = input(
                    "Enter orientation (H for horizontal, V for vertical): "
                ).upper()
                if orientation not in ['H', 'V']:
                    raise ValueError
                if is_valid_placement(grid, ship, row, col, orientation):
                    ship.place_ship(grid, row, col, orientation)  # Place ship
                    for coord in ship.coordinates:
                        grid[coord[0]][coord[1]] = "S"  # Mark ship's position
                    break
                else:
                    print("Invalid placement. Try again.")
            except (ValueError, IndexError):
                print(
                    "Invalid input. Please enter a letter and number. "
                    "(1-10), and H or V for orientation."
                )


# Main function to play the Battleship game
def play_battleships():
    # Create grids for the player and the AI
    player_grid = create_grid()
    ai_grid = create_grid()
    game_state = GameState()  # Initialize game state

    # Create player's and AI's ships with different sizes
    game_state.player_ships = [Ship(3), Ship(4), Ship(5)]
    game_state.ai_ships = [Ship(3), Ship(4), Ship(5)]

    # Game setup: placing player's and AI's ships
    print("Welcome to Battleships!")
    print("Place your ships:")
    place_player_ships(player_grid, game_state.player_ships)
    place_ai_ships(ai_grid, game_state.ai_ships)

    # Game loop: alternating between player's and AI's turns until game over
    while not game_state.game_over:
        if game_state.player_turn:
            print("Player's turn")
            print_grid(ai_grid, hide_ships=True)
            if player_turn(ai_grid, game_state.ai_ships):
                if check_game_over(game_state.ai_ships):
                    print("Congratulations! You won!")
                    game_state.game_over = True
            game_state.player_turn = False
        else:
            print("AI's turn")
            if ai_turn(player_grid, game_state.player_ships):
                if check_game_over(game_state.player_ships):
                    print("AI won! Better luck next time.")
                    game_state.game_over = True
            game_state.player_turn = True


# Entry point of the script
if __name__ == "__main__":
    play_battleships()