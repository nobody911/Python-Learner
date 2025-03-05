import math
base = float(input("Enter the base of the triangle (in m): "))
height = float(input("Enter the height of the triangle (in m): "))
hypo = math.sqrt(pow(base, 2)+pow(height, 2))
print(f"The hypo of the given triangle is: {hypo} m")