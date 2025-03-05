# List Comprehensions [expression for value in iterable if condition]

# example 1
# doubles = [num*2 for num in range(1, 11)]
# triples = [num*3 for num in range(1, 11)]
# square = [num*num for num in range(1, 11)]
# print(doubles)
# print(triples)
# print(square)

# example 2
# fruits = ["apple", "mango", "coconut", "peach"]
# fruits = [fruit[0].upper() for fruit in fruits]
# print(fruits)

# example 3
# numbers = [-3, -2, -1, 0, 1, 2, 3]
# pos_num = [num for num in numbers if num >= 0]
# print(pos_num)
# neg_num = [num for num in numbers if num < 0]
# print(neg_num)
# even_num = [num for num in numbers if num % 2 == 0]
# print(even_num)

# example 4
# grades = [50, 64, 84, 98, 74, 32]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)