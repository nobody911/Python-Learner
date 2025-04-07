#  ------------ LIST -----------------
'''fruits = ["apple", "cucumber", "orange", "banana"]
fruits.sort(reverse=True)
print(fruits)'''
# -------------TUPLE---------------
'''fruits = ("orange", "banana", "apple", "mango")
fruits = tuple(sorted(fruits, reverse=True))
print(fruits)'''
# -------------DICTIONARY----------
'''fruits = {"banana": 105,
          "apple": 85,
          "coconut": 150,
          "mango": 78}
# fruits = dict(sorted(fruits.items(), key=lambda fruit: fruit[0])) # based on the key in ascending order
# fruits = dict(sorted(fruits.items(), key=lambda fruit: fruit[0], reverse=True)) # based on the key in descending order
# fruits = dict(sorted(fruits.items(), key=lambda fruit: fruit[1])) # based on the value in ascending order
fruits = dict(sorted(fruits.items(), key=lambda fruit: fruit[1], reverse=True)) # based on the value in descending order

print(fruits)'''
# -------------------OBJECT----------------------
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    def __repr__(self):
        return f"{self.name}: {self.calories}"

fruits = [Fruit("banana", 105),
          Fruit("apple", 78),
          Fruit("mango", 85),
          Fruit("coconut", 150)]

# fruits = sorted(fruits, key=lambda fruit: fruit.name)
# fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
# fruits = sorted(fruits, key=lambda fruit: fruit.calories)
fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)
print(fruits)
