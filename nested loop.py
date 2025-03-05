rows = int(input("Enter the nunber of rows: "))
columns = int(input("Enter the nunber of columns: "))
symbol = input("Enter the symbol: ")
for x in range(columns):
    for y in range(rows):
        print(symbol, end="")

    print()