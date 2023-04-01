import random

user_won_time = 0

print("____________  _____   ")
print("| ___ \ ___ \/  ___|  ")
print("| |_/ / |_/ /\ `--.   ")
print("|    /|  __/  `--. \  ")
print("| |\ \| |    /\__/ /  ")
print("\_| \_\_|    \____/   ")

while True:                                                     ##########################################
    bot_choice = random.randint(1,3)                            # Let 1 = Rock , 2 = Paper , 3 = Scissors#
    print('You have won',user_won_time,'time(s)')               ##########################################
    user_choice = input('Rock(r), Paper(p), Scissors(s)? \n')   # asking user the input 
    if bot_choice == 1 and user_choice == 'r':                  # I may do documentaion if i have time!
        print('The bot choice is : Rock \n DRAW!')              # 
    elif bot_choice == 1 and user_choice == 'p':                # 
        print('The bot choice is : Rock \n You WIN!!')          #
        user_won_time +=1                                       #
    elif bot_choice == 1 and user_choice == 's':                #
        print('The bot choice is : Rock \n You lose :(')        #
    elif bot_choice == 2 and user_choice == 'r':                #
        print('The bot choice is : Paper \n You lose :(')       #
    elif bot_choice == 2 and user_choice == 'p':                #
        print('The bot choice is : Paper \n DRAW!!')            #
    elif bot_choice == 2 and user_choice == 's':                #
        print('The bot choice is : Paper \n You WIN!!')         #
        user_won_time +=1                                       #
    elif bot_choice == 3 and user_choice == 'r':                #
        print('The bot choice is : Scissors \n You WIN!!')      #
        user_won_time += 1                                      #
    elif bot_choice == 3 and user_choice == 'p':                #
        print('The bot choice is : Scissors \n You lose :(')    #
    elif bot_choice == 3 and user_choice == 's':                #
        print('The bot choice is : Scissors \n Draw!!')         #
    else:                                                       #
        print('Invalid input!')                                 #
