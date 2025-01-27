# String indexing using python 

# credit_num = "0123-4567-8915"
# credit_num = credit_num[-4:]
# print(f"XXXX-XXXX-{credit_num}")
# print(credit_num[::-1])

# email cutter (string indexing)

email = input("Enter your email: ")
index = email.index("@")
username = email[:index]
domain = email[index+1:]
print(f"Your username is {username} and domain is {domain}")