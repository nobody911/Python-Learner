import time
user_time = int(input("Enter the time for countdown in seconds: "))
for x in range(user_time, 0, -1):
    secs = int(x % 60)
    mins = int(x/60) % 60
    hrs = int(x/3600)
    print(f"{hrs:02}:{mins:02}:{secs:02}")
    time.sleep(1)
print("Time's Up!!!")