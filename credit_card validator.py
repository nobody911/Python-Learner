# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
# (If result is a two-digit number,
# add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

sum_odd = 0
sum_digit = 0
total = 0
num_double = 0
card_num = input("Enter your credit card number: ")

# Step - 1

card_num = card_num.replace("-", "")
card_num = card_num.replace(" ", "")
card_num = card_num[::-1]

# Step - 2

for num in card_num[::2]:
    sum_odd += int(num)

# Step - 3

for num in card_num[1::2]:
    num_double = int(num)*2
    if num_double >= 10 and num_double <= 18:
        for digit in str(num_double):       
            sum_digit += int(digit)
    else:
        sum_digit += num_double

# Step - 4

total = sum_odd + sum_digit

# Step - 5

if total % 10 == 0:
    print("The credit card is valid...")
else:
    print("The credit card is invalid...")