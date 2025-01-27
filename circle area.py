import math
radius = float(input("Enter the radius of the circle (in m): "))
area = math.pi*radius**2
# area = math.pi*pow(radius, 2)   # either can be used for squaring the radius
print(f"The area of the given circle is: {round(area, 2)} m")