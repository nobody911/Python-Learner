# Python temp conversion

temp = float(input("Enter the temperature: "))
unit = input("Enter the unit of temperature entered (C/F): ")
if unit == "C" or unit == "c":
    temp = round((temp*9/5)+32, 2)
    print(f"The given temperature in fahrenheit is: {temp}°F")
elif unit == "F" or unit == "f":
    temp = round((temp-32)*5/9, 2)
    print(f"The given temperature in celcius is: {temp}°C")
else:
    print(f"{unit} is not a valid unit...")