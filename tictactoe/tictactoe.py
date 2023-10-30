#!/usr/bin python3

def printBoard(game_board):         # perfection for noob like me
    print("+ - + - + - +")
    for i in range(3):
        print("| ",end="")
        for j in range(3):
            print(game_board[i][j],end=" | ")
        print("\n+ - + - + - +")

def place(playerInput, turn, game_board):
    validInput = False
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == playerInput:
                validInput = True
                if turn == 1:
                    game_board[i][j] = "O"
                    break
                elif turn == 2:
                    game_board[i][j] = "X"
                    break
    if validInput == False:
        return -1

def checkWin(game_board):
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2]:
            if game_board[i][0] == "O":
                print("Player1 WIN!")
            elif game_board[i][0] == "X":
                print("Player2 WIN!")
            return True
        if game_board[0][i] == game_board[1][i] == game_board[2][i]:
            if game_board[0][i] == "O":
                print("Player1 WIN!")
            elif game_board[0][i] == "X":
                print("Player2 WIN!")
            return True
    if game_board[0][0] == game_board[1][1] == game_board[2][2]:
        if game_board[0][0] == "O":
            print("Player1 WIN!")
        elif game_board[0][0] == "X":
            print("Player2 WIN!")
        return True
    elif game_board[0][2] == game_board[1][1] == game_board[2][0]:
        if game_board[0][2] == "O":
            print("Player1 WIN!")
        elif game_board[0][2] == "X":
            print("Player2 WIN!")
        return True
    else:
        return False

def main():
    start = input("Welcome to TicTacToe, enter 0 to start the game and any other button to exit:\n")
    while start == "0":
        game_board = [[1,2,3],[4,5,6],[7,8,9]]
        turn = 0
        while checkWin(game_board) is False and turn <= 8:
            printBoard(game_board)
            playerInput = input(f"Player{turn%2+1} turn now: ")
            try:
                playerInput = int(playerInput)
            except:
                print("Invalid input!")
            else:
                playerInput = int(playerInput)
                if playerInput < 1 or playerInput > 9:
                    print("Invalid input!")
                elif place(int(playerInput),turn%2+1,game_board) == -1:
                    print("Invalid input!")
                else:
                    place(playerInput,turn%2+1,game_board)
                    turn += 1
        if turn > 8 and checkWin(game_board) is False:
            print("DRAW!!")
            start = input("Enter 0 to play again and any other button to exit")
        elif turn <= 8 and checkWin(game_board) is True:
            checkWin(game_board)
            start = input("Enter 0 to play again and any other button to exit")

if __name__ == "__main__":
    main()
