# while loop in python
# example 1 

# food = input("Enter a food you like (q to quit): ")
# while not food == "q":
#     print(f"{food} is your favourite food...")
#     food = input("Enter a food you like (q to quit): ")
# print("bye!!!")

#example 2

num = int(input("Enter a number between 1-10: "))
while num < 1 or num > 10:
    print(f"{num} is not a valid number")
    num = int(input("Enter a number between 1-10: "))
print(f"The number you entered is {num}.")