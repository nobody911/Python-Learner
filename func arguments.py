# Positional arguments depends on position of arguments already done in function,py

# DEFAULTS ARGUMENTS

# import time
# def count (end, start = 1):
#     for sec in range(start, end+1):
#         time.sleep(1)
#         print(sec)
#     print("Done !!!")

# count(5, 3)

# KEYWORD ARGUMENTS

# def greeting(greet, title, first_name, last_name):
#     return f"{greet} {title} {first_name.capitalize()} {last_name.capitalize()}"

# intro = greeting(title = "Mr.", greet = "Hello", last_name="sakai", first_name="jin")
# print(intro)

# ARBITRARY KEYWORDS

# *args

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     print(total)
# add(5, 5)

# **kwargs

# def address(**address):
#     for key, value in address.items():
#         print(f"{key}: {value}")
# address(State="Assam", District="Cachar", City="Silchar", House_No =36, Road="1st Link Road")

# KWARGS (exercise 1)

def shipping_address(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for key, values in kwargs.items():
    #     print(f"{key}: {values}")
    if "house_no" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('dist')}")
        print(f"{kwargs.get('house_no')}")
    else:
        print(kwargs.get("street"))
        
shipping_address("Lord", "Jin", "Sakai",
                street = "1st Link Road",
                house_no = 36,
                dist = "Cachar")