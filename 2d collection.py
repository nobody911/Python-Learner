# keypad using tuples
num_pad = [(1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#")]
for num in num_pad:
    for col in num:
        print(col, end=" ")
    print()