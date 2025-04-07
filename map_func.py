celcius_temp = [36, 26.0, 89.5, 100]
fahrenheit_temp = list(map(lambda temp: (temp*9/5)+32, celcius_temp))
print(fahrenheit_temp)