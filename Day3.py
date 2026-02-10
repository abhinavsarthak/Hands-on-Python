n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    m = int(input("Enter mark: "))
    marks.append(m)

valid_count = 0
fail_count = 0

print("\nStudent Classification:")

for mark in marks:

    if mark < 0 or mark > 100:
        print(mark, "→ Invalid")

    elif mark >= 90:
        print(mark, "→ Excellent")
        valid_count += 1
        if mark >= 95:
            print("Bonus: High Performance Achieved!")

    elif mark >= 75:
        print(mark, "→ Very Good")
        valid_count += 1

    elif mark >= 60:
        print(mark, "→ Good")
        valid_count += 1

    elif mark >= 40:
        print(mark, "→ Average")
        valid_count += 1

    else:
        print(mark, "→ Fail")
        valid_count += 1
        fail_count += 1

print("\nFinal Summary:")
print("Total Valid Students:", valid_count)
print("Total Failed Students:", fail_count)
