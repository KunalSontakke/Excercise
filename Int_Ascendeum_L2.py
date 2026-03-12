import random

# Get game size
players = 4
size = int(input("Enter the game size: "))
game_size = size * size
print("Final position:", game_size)

positions = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}

player_order = ["A", "B", "C", "D"]

while True:
    for p in player_order:
        print(f"\nPlayer {p}, your turn...")

        dice = random.randint(1, 6)
        print("Dice rolled:", dice)

        # Move only if within board
        if positions[p] + dice <= game_size:
            positions[p] += dice

        print("Position:", positions[p])

        # Display track
        for i in range(1, positions[p] + 1):
            print(i, end=",")

        # Check winner
        if positions[p] == game_size:
            print(f"\n\nPlayer {p} has won the game!")
            exit()
