full_name = input("Enter Full Name: ")
email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")
age = int(input("Enter Age: "))

valid = True

if full_name.startswith(" ") or full_name.endswith(" "):
    valid = False
elif full_name.count(" ") < 1:
    valid = False

if "@" not in email or "." not in email:
    valid = False
elif email.startswith("@"):
    valid = False

if len(mobile) != 10:
    valid = False
elif not mobile.isdigit():
    valid = False
elif mobile.startswith("0"):
    valid = False

if age < 18 or age > 60:
    valid = False

if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
