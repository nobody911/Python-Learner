import datetime
# DATE
date = datetime.date(2025, 2, 1)
today = datetime.date.today()

# TIME
time = datetime.time(11, 5, 6)
now = datetime.datetime.now()
now = now.strftime("%a %d/%m/%Y - %H:%M:%S")
# print(now)

# TIME MEASURING
target_datetime = datetime.datetime(2026, 5, 4, 12, 30, 0)
current_datetime = datetime.datetime.now()

if current_datetime > target_datetime:
    print("Target date has passed...")
else:
    print("Target date has NOT passed...")