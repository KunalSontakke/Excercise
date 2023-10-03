import random

countA = 0
countB = 0
countC = 0
countD = 0


size = int(input("Enter the game size"))
game_size = size * size
print(game_size)

while countA != game_size or countB != game_size or countC != game_size or countD != game_size:

        print("player A your turn.....")
        playerA = random.randint(1,6)
        print(playerA)
        countA = countA + playerA
        print(countA)
        for i in range(1,countA):
                print(i,end=",")
        if countA == game_size:
            break


        print("player B your turn.....")
        playerB = random.randint(1, 7)
        print(playerB)
        countB = countB + playerB
        print(countB)
        for i in range(1,countB):
                print(i,end=",")
        if countB == game_size:
            break


        print("player C your turn.....")
        playerC = random.randint(1, 7)
        print(playerC)
        countC = countC + playerC
        print(countC)
        for i in (1,countC):
                print(i,end=",")
        if countC == game_size:
            break


        print("player D your turn.....")
        playerD = random.randint(1, 7)
        print(playerD)
        countD = countD + playerD
        print(countD)
        for i in (1,countD):
                print(i,end=",")
        if countD == game_size:
            break

if countA == game_size:
        print("player A has won the game")
elif countB == game_size:
        print("player B has won the game")
elif countC == game_size:
        print("player C has won the game")
else:
        print("player D has won the game")
# ======================================================================================================================




