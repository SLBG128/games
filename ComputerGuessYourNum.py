from random import randint

def compGuess(user):
    tries = 0
    lowLim = 0
    highLim = 100
    guessed = False
    while guessed == False:
        comp = randint(lowLim,highLim)
        print(f"The computer guessed {comp} ")
        tries += 1
        if comp == user:
            print(f"The computer guessed {tries} time(s) to sucess")
            guessed = True
        elif comp < user:
            lowLim = comp
        elif comp > user:
            highLim = comp
        else:
            print("This part of code should be unreachable!!!")

def main():
    while True:
        user = input("Input an integer (0-100): ")
        try:
            user = int(user)
        except:
            print("Only integer is accepted")
        else:
            compGuess(user)

if __name__ == "__main__":
    main()
