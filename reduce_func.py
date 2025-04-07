from functools import reduce
prices = [85+64+25.0+56.25]
add = reduce(lambda x, y: x+y, prices)
print(add)