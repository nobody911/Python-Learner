# Food Stall automated menu using Python

menu = {"Pizza":299,
        "Maggi":150,
        "Burger":99,
        "Pepsi":50,
        "Popcorn":499}

cart = []
total = 0
print("--------------MENU----------------")
for food, price in menu.items():
    print(f"{food:10}: ₹{price:,.2f}")
print("----------------------------------")

while True:
    food = input("What do you like to have? (Q to quit): ").capitalize()
    if food == "Q":
        break
    elif not menu.get(food) == None:
        cart.append(food)
    else:
        print(f"{food} not available !!! Enter something from the menu above ...")
print("--------------YOUR ORDER-----------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Your total is: ₹{total:,.2f} only")