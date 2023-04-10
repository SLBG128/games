import random

def main():
    bot = random.randint(1, 100)            # Random number answer
    low_lim = 1             # lower limit?
    high_lim = 100          # upper limit?
    tried = 0       # tries
    while True:
        print(f"The value is between {low_lim} and {high_lim}")   # Remind users the range
        user = input("Guess the number:\n")                    # user input
        try:
            # transfer user input to int (make sure user input is int)
            user = int(float(user))
        except:
            # will show this if user input is not int or float
            print("Only integer is allowed!!!")
        else:
            if user < low_lim or user > high_lim:
                print(f"The value should be between {low_lim} and {high_lim}")
            else:
                while bot != user:
                    if user > bot:
                        print(f"The answer is smaller then {user}")
                        high_lim = user
                        tried += 1
                        break
                    elif user < bot:
                        print(f"The number is larger then {user}")
                        low_lim = user
                        tried += 1
                        break
        if user == bot:
            print("Correct Answer!!")
            print(f"You have guessed {tried} time")
            break

def print_logo():           # The logo
    print("   _____                       _______ _            _   _                 _               ")
    print("  / ____|                     |__   __| |          | \ | |               | |              ")
    print(" | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ ")
    print(" | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|")
    print(" | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_/ |  __/ |   ")
    print("  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   ")

def choices():      #User choice
    print("Press[1] to start the game")
    print("Press[2] to exit the game")

if __name__ == "__main__":
    print_logo()
    choices()
    while True:
        choice = str(input())
        if choice == str(1):
            main()
            break
        elif choice == str(2):
            exit()
        else:
            print("Invalid input")
