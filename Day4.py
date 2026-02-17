activity_scores = [10, 45, 78, 120, -5, 30, 99, 150]

register_number = input("Enter your Register Number: ")

last_character = register_number[len(register_number) - 1]
D = int(last_character)

print("Register Digit (D):", D)

low_risk = []
medium_risk = []
high_risk = []
critical_risk = []

ignored_entries = 0
valid_entries = 0

for score in activity_scores:

    if score < 0:
        ignored_entries = ignored_entries + 1

    else:
        valid_entries = valid_entries + 1

        if score >= 0 and score <= 30:
            low_risk.append(score)

        elif score >= 31 and score <= 60:
            medium_risk.append(score)

        elif score >= 61 and score <= 100:
            high_risk.append(score)

        else:
            critical_risk.append(score)


print("\nBefore Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

removed_due_to_personalization = 0

if D % 2 == 0:

    print("\nPersonalized Filter Applied: EVEN digit detected")

    removed_due_to_personalization = len(low_risk)

    low_risk = []

else:

    print("\nPersonalized Filter Applied: ODD digit detected")

    removed_due_to_personalization = len(critical_risk)

    critical_risk = []


print("\nAfter Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

print("\nFinal Security Report:")
print("Total Valid Entries:", valid_entries)
print("Ignored Entries:", ignored_entries)
print("Removed Due to Personalization:", removed_due_to_personalization)
