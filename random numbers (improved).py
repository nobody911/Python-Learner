import random
low_num = 1
high_num = 100
guesses = 0
number = random.randint(low_num, high_num)
while True:
    guess = input(f"Enter a number between ({low_num} - {high_num}): ")
    guesses += 1
    if guess.isdigit():
        guess = int(guess)
        if guess > high_num or guess < low_num:
            print("The number entered is out of range...")
        elif guess < number:
            print("Oops !!! Too low... Try again")
        elif guess > number:
            print("Oops !!! Too high... Try again")
        else:
            print(f"Great !!! You got the correct guess which was {number}...")
            print(f"It took you {guesses} guesses to clear this game")
            break
    else:
        print("Please enter a valid input !!!")