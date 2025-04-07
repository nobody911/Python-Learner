# USING FILTER FUNCTION

'''grades = [25, 65, 30, 55, 87]
passed = list(filter(lambda grade: grade >= 30), grades)
print(passed)'''

# USING LIST COMPREHENSION

grades = [25, 65, 30, 55, 87]
passed = [grade for grade in grades if grade >= 30]
print(passed)