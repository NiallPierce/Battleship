# Battleships Game

This is my take on the classic Battleships game. Placing your ships on a 10x10 grid and taking turns against the AI to see who can sink the other players ship by guessing their locations faster.

## How to Play
1. **Setup**: 
   - You and the AI will place ships on separate 10x10 grids.
   - Each player has ships of varying sizes (3, 4, and 5 units).
   - You will manually place your ships by entering a starting coordinate and specifying horizontal (H) or vertical (V) orientation.
   - The AI randomly places its ships on its grid.

2. **Gameplay**:
   - Players take turns to guess a location on the opponent's grid.
   - Enter a coordinate (e.g., A5) to attack that position.
   - The game will notify you if it's a **hit** (successful attack) or a **miss**.
   - If all segments of a ship are hit, the ship is sunk.
   - The AI also takes turns trying to sink your ships.

3. **Winning the Game**:
   - The game ends when all ships of either the player or the AI are sunk.
   - The first player to sink all the enemy ships wins.

## Features

### Existing Features:
- **10x10 Grids**: Both the player and AI use grids for ship placement and attacks.
- **Manual Ship Placement**: The player can choose where to place ships and their orientation.
- **AI Ship Placement**: The AI randomly places its ships on the grid, ensuring no overlap or out-of-bounds ships.
- **Turn-Based Attacks**: Each turn, the player and AI take turns guessing a location to attack.
- **Hit/Miss Feedback**: The game informs the player whether they hit, missed, or sunk an enemy ship.
- **Game Over Detection**: The game automatically detects when all ships on one side have been sunk.

### Future Features:
- **Ship Randomization Option**: Allow players to randomize ship placement if they prefer not to place manually.
- **Difficulty Levels**: Add AI difficulty settings (e.g., easy, medium, hard) for smarter move strategies.
- **Multiplayer Mode**: Implement an option for two players to play against each other.
- **Replay Option**: Add a feature to restart the game after a match is over without exiting the program.
- **Visual Effects**: Incorporate animations or enhanced visuals to show hits, misses, and sunk ships.

## Data Model

### Classes:
1. **Ship**: 
   - `size`: The length of the ship (e.g., 3, 4, or 5 units).
   - `hits`: Tracks how many times the ship has been hit.
   - `coordinates`: Stores the ship's position on the grid.
   
