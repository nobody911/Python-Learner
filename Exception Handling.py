try:
    num = int(input("Enter a number: "))
    print(1/num)
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Please enter only numbers")
except Exception:
    print("Something went wrong")
finally:
    print("Task completed")
