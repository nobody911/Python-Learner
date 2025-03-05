def name_splitter(name):
    index = name.index(" ")
    first_name = name[:index].capitalize()
    last_name = name[index+1:].capitalize()
    print(f"Your first name is: {first_name}")
    print(f"Your last name is: {last_name}")

full_name = input("Enter your full name: ")
name_splitter(full_name)

