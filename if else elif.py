status = True
age = int(input("Enter your age: "))
if age >= 100:
    print("You are too old to sign in!!")
elif age >= 18:
    print("You are eligible to sign up!")
elif age <=0:
    print("You are not born yet!!")
else:
    print("You need to be 18+ to get signed up!")

if status:
    print("The servers are online...")
else: 
    print("The servers are offline...")