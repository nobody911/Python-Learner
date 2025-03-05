def create_name(first_name, last_name):
    first = first_name.capitalize()
    last = last_name.capitalize()
    return first+" "+last

while True:
    consent = input("Are you ready (y/n): ").lower()
    if consent == "y":
        first = input("Enter your first name: ")
        last = input("Enter your last name: ")
        name = create_name(first, last)
        print(f"Your full name is {name}")
    elif consent == "n":
        break
    else:
        print("Please enter a valid input")