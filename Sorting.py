# I know this is not a game 
# But I want to find a place to save this
# So I put this script in this temporarily
# I will move it to other repo later
numbers = []    
sorted_numbers = []

def main():
    print("Welcome to number sorter!")
    print("Input the numbers and type END when finished.")
    while True:
        x = input()
        if x == "END":
            break
        else:
            try:
                x = float(x)
                numbers.append(x)
            except:
                print("This is not a number!")
    nnumbers = sorted(numbers)
    for i in nnumbers:
        i = str(i)
        if "." in i:                    # case example: 69.0 or 69.6900 or 69.00 or 69.69
            if i.endswith(".0"):        # case example: 69.0
                i = i[:-2]
                sorted_numbers.append(i)
            elif i.endswith("0") and "." in i:      # case example: 69.6900 or 69.00
                while i.endswith("0") == True and "." in i:
                    i = i[:-1]
                if i.endswith(".") == True:         # case example: 69. (Will occur after removing the 0 of 69.00)
                    i = i[:-1]
                    sorted_numbers.append(i)
                else:           # case example: 69.69 (after)
                    sorted_numbers.append(i)
            else:       #case example: 69.69 (is already)
                sorted_numbers.append(i)
        else:           #case example: 69
            sorted_numbers.append(i)
    all_numbers = " < ".join(sorted_numbers)
    print(all_numbers)

if __name__ == "__main__":
    main()
