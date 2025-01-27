# Shopping cart using python

foods = []
prices = []
total = 0
while True:
    food = input("Enter the name of the food to purchase (q to quit): ")
    if not food.lower() == "q" or food.isalpha() == False or food == "":
        price = float(input("Enter the price of the food: "))
        foods.append(food)
        prices.append(price)
    else:
        break
print("----YOUR CART----")
for food in foods:
    print(food)
for price in prices:
    total += price
print(f"Your total is: ₹{total:02}")

