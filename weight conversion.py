# python weight conversion
weight = float(input("Enter your weight: "))
unit = input("Enter the unit of weight entered (K/L): ")
if unit == "K" or unit == "k":
    weight = round(weight*2.205, 2)
    unit = "Lbs"
    print(f"Your weight in pounds is: {weight} {unit}")
elif unit == "L" or unit == "l":
    weight = round(weight/2.205, 2)
    unit = "Kgs"
    print(f"Your weight in kilograms is: {weight} {unit}")
else:
    print(f"{unit} is not a valid unit !!!")