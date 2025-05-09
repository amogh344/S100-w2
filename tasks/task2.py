import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

email = input("Enter an email: ")

if is_valid_email(email):
    print("Valid email.")
else:
    print("Invalid email.")