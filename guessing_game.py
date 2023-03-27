import random

bot = random.randint(1,100)  # Random number answer
low_lim = 1                  #lower limit?
high_lim = 100               #upper limit?
tried = 0                    #tries

while True:
    print('The value is between',low_lim,'and',high_lim)   # Remind users the range
    user = input('Guess the number:\n')                    # user input
    try:
        user = int(float(user))                            # transfer user input to int (make sure user input is int)
    except:
        print('Only integer is allowed!!!')                # will show this if user input is not int or float
    else:
        if user < low_lim or user > high_lim:
            print('The value should be between',low_lim,'and',high_lim)
        else:
            while bot != user:
                if user > bot:
                    print('The answer is smaller then', user)
                    high_lim = user
                    tried +=1
                    break
                elif user < bot:
                    print('The number is larger then', user)
                    low_lim = user
                    tried +=1
                    break
    if user == bot:
        print('Correct Answer!!')
        print('You have guessed',tried,'time')
        break
