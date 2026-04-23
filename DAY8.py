import random
import numpy as np
import pandas as pd
import math

def generate_data(n):
    students = []
    for i in range(n):
        sid = f"S{i+1}"
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)

        performance_index = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)

        students.append((sid, marks, attendance, assignment, performance_index))
    return students


def classify_students(data):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }

    for student in data:
        sid, marks, attendance, assignment, pi = student

        if marks < 40 or attendance < 50:
            categories["At Risk"].append(sid)
        elif 40 <= marks <= 70:
            categories["Average"].append(sid)
        elif 71 <= marks <= 90:
            categories["Good"].append(sid)
        elif marks > 90 and attendance > 80:
            categories["Top Performer"].append(sid)

    return categories



def analyze_data(df):
    marks = df["Marks"].values

    mean_val = np.mean(marks)
    median_val = np.median(marks)
    std_val = np.std(marks)


    max_val = marks[0]
    for m in marks:
        if m > max_val:
            max_val = m

    correlation = np.corrcoef(df["Marks"], df["Attendance"])[0][1]


    min_val = np.min(marks)
    max_val2 = np.max(marks)
    df["Normalized Marks"] = [(x - min_val) / (max_val2 - min_val2) for x in marks]

    return mean_val, median_val, std_val, max_val, correlation



num_students = 10
data = generate_data(num_students)

df = pd.DataFrame(data, columns=[
    "ID", "Marks", "Attendance", "Assignment", "Performance Index"
])

categories = classify_students(data)

mean_m, median_m, std_m, max_m, corr = analyze_data(df)


consistent = std_m < 15
attendance_risk = len(df[df["Attendance"] < 50]) > 3
top_perf = len(categories["Top Performer"]) >= 2

if consistent and not attendance_risk and top_perf:
    insight = "Stable Academic System"
elif attendance_risk:
    insight = "Critical Attention Required"
else:
    insight = "Moderate Performance"


print(df)
print(categories)
print((mean_m, std_m, max_m))
print("Final Insight:", insight)