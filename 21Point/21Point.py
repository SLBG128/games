#!/usr/bin python3
from random import randint

def drawCard(Cards):
    # simulate the card drawing action
    cardSymbol = randint(0,3)
    cardValue = randint(0,len(Cards[cardSymbol])-1)
    choice = Cards[cardSymbol][cardValue]
    Cards[cardSymbol].remove(choice)
    return cardValue, cardSymbol, choice

def winCheck(Player,Computer):
    # check who win the game or draw
    if Player > Computer or Player == 21:      # Player Win
        return 1
    elif Player < Computer or Computer == 21:       # Computer Win
        return 2
    elif Player == Computer:        # DRAW
        return 0

def specialValueCheck(choice):
    # convert the value of some special card
    if choice == "A":       # A can be 1 or 11, my rule: 1 or 11 is unchangable
        A_Value = input("Since the card you draw is A, what value you want it to be(1 or 11): ")
        while not (A_Value != "1" or A_Value != "11"):
            print("Invalid value")
            A_Value = input("Since the card you draw is A, what value you want it to be(1 or 11): ")
        cardValue = int(A_Value)
        return cardValue
    elif choice == "J" or choice == "Q" or choice == "K":   # Face card value = 10
        cardValue = 10
        return cardValue
    else:
        return int(choice)

def compValueCheck(compChoice,computerTotal):
    # comvert the value of some special card for computer (same rule as above)
    if compChoice == "A":
        if computerTotal <= 10:
            compValue = 11
            return compValue
        else:
            compValue = 1
            return compValue
    elif compChoice == "J" or compChoice == "Q" or compChoice == "K":
        compValue = 10
        return compValue
    else:
        return int(compChoice)

def compAction(computerTotal):
    if computerTotal > 19:
        return "N"
    else:
        return "Y"

def main():
    print("Welcome to 21pt!")
    start = input("Enter 0 to play, or other button to exit: ")
    while start == "0":
        CardsSymbol = ["Clubs","Diamonds","Hearts","Spades"]
        Cards = [["A","2","3","4","5","6","7","8","9","10","J","Q","K"],  # Clubs
                 ["A","2","3","4","5","6","7","8","9","10","J","Q","K"],  # Diamonds
                 ["A","2","3","4","5","6","7","8","9","10","J","Q","K"],  # Hearts
                 ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]]  # Spades
        ### Player draw card ###
        cardValue , cardSymbol , choice = drawCard(Cards)
        playerLose = False        
        playerTotal = 0
        print(f"Your first card is: {CardsSymbol[cardSymbol]} {choice}")
        ### Computer draw card ###
        compValue , compSymbol , compChoice = drawCard(Cards)
        compLose = False
        computerTotal = 0
        print(f"Computer first card is {CardsSymbol[compSymbol]} {compChoice}")
        print("="*20)
        ### Value adding/converting -Player
        playerValue = specialValueCheck(choice)
        playerTotal += int(playerValue)
        ### Value adding/converting -Computer
        compValue = compValueCheck(compChoice,computerTotal)
        computerTotal += int(compValue)
        # Second card drawing, adding + converting
        cardValue , cardSymbol , choice = drawCard(Cards)
        cardValue = specialValueCheck(choice)
        playerTotal += int(cardValue)
        print(f"You just draw a {CardsSymbol[cardSymbol]} {choice}")
        print(f"The total value of your cards are: {playerTotal}")
        ## Backend computer doing calc
        compValue , compSymbol , compChoice = drawCard(Cards)
        compValue = compValueCheck(compChoice,computerTotal)
        computerTotal += int(compValue)
        print("Computer just draw a card")
        compPlay = compAction(computerTotal)
        print("="*20)
        play = input("Do you still want to draw card(Y/N): ")
        while not(play != "Y" or play != "N" or play != "y" or play != "n"):
            # do-while loop validating the user input
            print("Invalid input")
            play = input("Do you still want to draw card(Y/N): ")
        while (play == "Y" or play == "y") and playerLose is False and compLose is False:
            ## Card drawing, adding + converting
            cardValue , cardSymbol , choice = drawCard(Cards)
            playerValue = specialValueCheck(choice)
            playerTotal += int(playerValue)
            print(f"You just draw a {CardsSymbol[cardSymbol]} {choice}")
            print(f"The total value of your cards are: {playerTotal}")
            if playerTotal > 21:
                playerLose = True
            # Backend computing
            if compPlay == "Y" and playerLose is False and compLose is False:
                compValue , compSymbol , compChoice = drawCard(Cards)
                compValue = compValueCheck(compChoice,computerTotal)
                computerTotal += int(compValue)
                print("Computer just draw a card")
                compPlay = compAction(computerTotal)
                if computerTotal > 21:
                    compLose = True
            elif compPlay == "N" and playerLose is False and compLose is False:
                pass            
            if playerLose is False and compLose is False:
                print("="*20)
                play = input("Do you still want to draw card(Y/N): ")
                while not (play != "Y" or play != "N" or play != "y" or play != "n"):
                    # do-while loop validating user input
                    print("Invalid input")
                    play = input("Do you still want to draw card(Y/N): ")
        while compPlay == "Y" and playerLose is False and compLose is False:
            # Computer keep drawing card if player don't want to draw
            compValue , compSymbol , compChoice = drawCard(Cards)
            compValue = compValueCheck(compChoice,computerTotal)
            computerTotal += int(compValue)
            print("Computer just draw a card")
            if computerTotal > 21:
                compLose = True
            compPlay = compAction(computerTotal)

        print("="*20)
        ## Win check
        print(f"Your total card value: {playerTotal}")
        print(f"Computer total card value: {computerTotal}")

        if playerLose is True:
            print("You LOSE and Computer WIN")
        elif compLose is True:
            print("Computer LOSE and You WIN")
        elif winCheck(playerTotal,computerTotal) == 0:
            print("DRAW")
        elif winCheck(playerTotal,computerTotal) == 1:
            print("You WIN")
        elif winCheck(playerTotal,computerTotal) == 2:
            print("Computer WIN")
        start = input("Enter 0 to play again (other button to exit): ")

if __name__ == "__main__":
    main()
