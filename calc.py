# Python calculator

operator = input("Enter an operator (+, -, *, /): ")
num_1 = float(input("Enter the 1st number: "))
num_2 = float(input("Enter the 2nd number: "))
if operator == "+":
    print(f"The sum of {num_1} and {num_2} is: ", num_1+num_2)
elif operator == "-":
    print(f"The subtraction of {num_1} and {num_2} is: ", num_1-num_2)
elif operator == "*":
    print(f"The multiplication of {num_1} and {num_2} is: ", num_1*num_2)
elif operator == "/":
    print(f"The division of {num_1} and {num_2} is: ", round(num_1/num_2, 2))
elif operator == "":
    print("Please enter an operator !!!")
else:
    print(f"{operator} is not a valid operator !!!")
    