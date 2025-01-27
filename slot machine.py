import random
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for x in range(3)]
def print_row(row):
    print(" | ".join(row))
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet*3
        elif row[1] == "🍉":
            return bet*5
        elif row[2] == "🍋":
            return bet*10
        elif row[2] == "🔔":
            return bet*15
        elif row[2] == "⭐":
            return bet*20
    return 0
def main():
    balance = 100
    print("Welcome to python slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    while balance > 0:
        print(f"Current balance: ₹{balance}")
        bet = input("Place your bet amount: ")
        if not bet.isdigit():
            print("Enter a valid bet amount...")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient Funds")
        elif bet <= 0:
            print("Bet amount should be greater than 0")
        else:
            balance -= bet
        row = spin_row()
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You have won : ₹{payout}")
        else:
            print(f"You lost maybe try again....")
        balance += payout
        print(f"Current balance: ₹{balance}")
        play_again = input("Do you want to play again(y/n): ")
        if play_again.lower() != "y":
            break
if __name__ == "__main__":
    main()