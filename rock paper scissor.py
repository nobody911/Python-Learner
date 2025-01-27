import random
options = ("rock", "paper", "scissors")
running = True
while running == True:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
    if player == computer:
        print(f"You chose {player}", end=" " f"computer chose {computer}")
        print()
        print("It's a tie !!!")
    elif player == "paper" and computer == "rock":
        print(f"You chose {player}", end=" " f"computer chose {computer}")
        print()
        print("You win!!!")
    elif player == "rock" and computer == "scissors":
        print(f"You chose {player}", end=" " f"computer chose {computer}")
        print()
        print("You win!!!")
    elif player == "scissors" and computer == "paper":
        print(f"You chose {player}", end=" " f"computer chose {computer}")
        print()
        print("You win!!!")
    else:
        print(f"You chose {player}", end=" " f"computer chose {computer}")
        print()
        print("You lose!!!")
    play_again = input("Play again? (y/n): ").lower()
    if play_again == "n":
        running = False
        print("Thanks for playing...")
