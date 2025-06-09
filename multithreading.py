import threading
import time

def take_trash():
    time.sleep(2)
    print("The trash has been taken out")

def walk_dog(first, last):
    time.sleep(5)
    print(f"{first} {last} has been walked")

def get_mail():
    time.sleep(3)
    print("You have got the mail")

chore_1 = threading.Thread(target=take_trash)
chore_1.start()

chore_2 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore_2.start()

chore_3 = threading.Thread(target=get_mail)
chore_3.start()

chore_1.join()
chore_2.join()
chore_3.join()

print("Task accomplished")