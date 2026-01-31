student_id = input().strip()
email = input().strip()
password = input().strip()
referral = input().strip()

valid = True

if len(student_id) != 7:
    valid = False
elif student_id[0:3] != "CSE":
    valid = False
elif student_id[3] != "-":
    valid = False
elif not (student_id[4].isdigit() and student_id[5].isdigit() and student_id[6].isdigit()):
    valid = False

if valid:
    if "@" not in email or "." not in email:
        valid = False
    elif email[0] == "@" or email[-1] == "@":
        valid = False
    elif not email.endswith(".edu"):
        valid = False

if valid:
    if len(password) < 8:
        valid = False
    elif not password[0].isupper():
        valid = False
    elif not (
        "0" in password or "1" in password or "2" in password or
        "3" in password or "4" in password or "5" in password or
        "6" in password or "7" in password or "8" in password or
        "9" in password
    ):
        valid = False

if valid:
    if len(referral) != 6:
        valid = False
    elif referral[0:3] != "REF":
        valid = False
    elif not (referral[3].isdigit() and referral[4].isdigit()):
        valid = False
    elif referral[5] != "@":
        valid = False

if valid:
    print("APPROVED")
else:
    print("REJECTED")
