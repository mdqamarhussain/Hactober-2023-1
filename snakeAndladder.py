import random

# Initialize player positions
player1_position = 0
player2_position = 0

# Define the Snake and Ladder board
snake_ladder = {
    3: 20,
    17: 7,
    21: 1,
    30: 5,
    45: 25,
    52: 15,
    65: 42,
    88: 50,
    90: 60,
}

# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# Function to update player position
def update_position(player, roll):
    new_position = player + roll

    # Check for snakes and ladders
    if new_position in snake_ladder:
        new_position = snake_ladder[new_position]

    return new_position

# Main game loop
while player1_position < 100 and player2_position < 100:
    input("Player 1, press Enter to roll the dice...")
    roll = roll_dice()
    print(f"Player 1 rolled a {roll}.")
    player1_position = update_position(player1_position, roll)
    print(f"Player 1 is now at position {player1_position}.\n")

    if player1_position >= 100:
        print("Player 1 wins!")
        break

    input("Player 2, press Enter to roll the dice...")
    roll = roll_dice()
    print(f"Player 2 rolled a {roll}.")
    player2_position = update_position(player2_position, roll)
    print(f"Player 2 is now at position {player2_position}.\n")

    if player2_position >= 100:
        print("Player 2 wins!")

