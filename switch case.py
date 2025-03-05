# switch case

# example 1
# def days_of_week(days):
#     match days:
#         case 1:
#             print("Its Sunday")
#         case 2:
#             print("Its Monday")
#         case 3:
#             print("Its Tuesday")
#         case 4:
#             print("Its Wednesday")
#         case 5:
#             print("Its Thrusday")
#         case 6:
#             print("Its Friday")
#         case 7:
#             print("Its Saturday")
#         case _:
#             print("Not a valid day")
# days_of_week(1)

# example 2

def weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thrusday" | "Friday":
            return False
        case _:
            return "Not a valid day"
print(weekend("Monday"))