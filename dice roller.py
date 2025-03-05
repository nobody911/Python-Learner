import random
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
dice = []
total = 0
dice_num = int(input("Enter the number of dice: "))
for die in range(dice_num):
    dice.append(random.randint(1, 6))

# for die in range(dice_num):
#     for line in dice_art.get(dice[die]):             # vertical dice formation
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")         # horizontal dice formation
    print()
    
for die in dice:
    total += die

print(f"Total: {total}")