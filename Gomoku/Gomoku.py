#!/usr/bin python3
# sudo rm -rf /*
### Function handling the board ###
def boardInitialise(Board):
    for i in range(22):
        if i < 10:
            i = "0" + str(i)
        else:
            i = str(i)
        Board[0].append(i)
    
    for y in range(21):
        if y < 9:
            y = "0" + str(y+1)
        else:
            y = str(y+1)
        Board.append([y])
        for i in range(21):
            Board[int(y)].append(" +")
    return Board

def printBoard(Board):
    for y in range(len(Board)):
        for x in range(len(Board[y])):
            print(Board[y][x], end="")
        print()

### Placing
def place(PlayerX,PlayerY,turn,Board):
    if Board[PlayerY][PlayerX] != " +":
        return False
    if turn%2+1 == 1:
        Board[PlayerY][PlayerX] = " O"
    elif turn%2+1 == 2:
        Board[PlayerY][PlayerX] = " X"

### Check valid
def validInput(PlayerX,PlayerY,Board):
    if Board[PlayerY][PlayerX] == " +":
        return True
    else:
        return False

### Check anyone win ###
def winCheck(Board):
    # Winning condition 1: Horizontally matched
    for y in range(1,len(Board)):
        for x in range(1,len(Board[y])-4):
            if Board[y][x] == Board[y][x+1] == Board[y][x+2] == Board[y][x+3] == Board[y][x+4]:
                if Board[y][x] == " O":
                    return 1
                elif Board[y][x] == " X":
                    return 2
                else:
                    return 0
    # Winning condition 2: Vertically matched
    for y in range(1,len(Board)-4):
        for x in range(1,len(Board)):
            if Board[y][x] == Board[y+1][x] == Board[y+2][x] == Board[y+3][x] == Board[y+4][x]:
                if Board[y][x] == " O":
                    return 1
                elif Board[y][x] == " X":
                    return 2
                else:
                    return 0
    # Winning condition 3: Slope like this \ 
    for y in range(1,len(Board)-4):
        for x in range(1,len(Board[y])-4):
            if Board[y][x] == Board[y+1][x+1] == Board[y+2][x+2] == Board[y+3][x+3] == Board[y+4][x+4]:
                if Board[y][x] == " O":
                    return 1
                elif Board[y][x] == " X":
                    return 2
                else:
                    return 0
    # Winning condition 4: Slope like this /
    for y in range(5,len(Board)):
        for x in range(1,len(Board[y])-4):
            if Board[y][x] == Board[y-1][x+1] == Board[y-2][x+2] == Board[y-3][x+3] == Board[y-4][x+4]:
                if Board[y][x] == " O":
                    return 1
                elif Board[y][x] == " X":
                    return 2
                else:
                    return 0

def main():
    print("Welcome to Gomoku!!!")
    start = input("Press 0 to start playing and other button to exit: ")
    while start == "0":
        Board = [[]]
        boardInitialise(Board)
        printBoard(Board)
        turn = 0
        while winCheck(Board) == 0 and turn <= 441:
            print(f"Player{turn%2+1} turn now!")
            PlayerX = input("What is the X coordinate of the place you want to place: ")
            validX = False
            ## Validating user input
            while validX is False:
                try:
                    PlayerX = int(PlayerX)
                except:
                    print("Invalid input")
                    PlayerX = input("What is the X coordinate of the place you want to place: ")
                else:
                    PlayerX = int(PlayerX)
                    if PlayerX < 1 or PlayerX > 21:
                        print("Invalid input")
                        PlayerX = input("What is the X coordinate of the place you want to place: ")
                    else:
                        validX = True
            PlayerY = input("What is the Y coordinate of the place you want to place: ")
            validY = False
            ## Validating user input
            while validY is False:
                try:
                    PlayerY = int(PlayerY)
                except:
                    print("Invalid input")
                    PlayerY = input("What is the Y coordinate of the place you want to place: ")
                else:
                    PlayerY = int(PlayerY)
                    if PlayerY < 1 or PlayerY > 21:
                        print("Invalid input")
                        PlayerY = input("What is the Y coordinate of the place you want to place: ")
                    else:
                        validY = True
            if validInput(PlayerX,PlayerY,Board) is False:
                print("Invalid input")
            else:
                place(PlayerX,PlayerY,turn,Board)
                printBoard(Board)
                turn += 1
        if winCheck(Board) == 1:
            print("Player1 WIN!")
        elif winCheck(Board) == 2:
            print("Player2 WIN!")
        elif winCheck(Board) == 0 and turn > 441:
            print("Impossible but DRAW!!")
        start = input("Press 0 to play again, other to exit")

if __name__ == "__main__":
    main()
