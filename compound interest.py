while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount cannot be less than zero!!!")
    else:
        break
while True:
    interest = float(input("Enter the rate of interest (in percent): "))
    if interest < 0:
        print("Rate of interest cannot be less than zero!!!")
    else:
        break
while True:
    time = int(input("Enter the time in whole years: "))
    if time < 0:
        print("Time cannot be less than zero!!!")
    else:
        break
total = principle*pow((1+interest/100), time)
print(f"Your total balance after {time} year/s is: ₹{total:.2f}")
