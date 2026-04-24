import random
import pandas as pd
import numpy as np
import math
import copy


# Function 1
def generate_data(n):
    students=[]

    for i in range(n):
        record={
            "id":i+1,
            "marks":random.randint(40,100),
            "attendance":random.randint(50,100),
            "scores":[
                random.randint(15,30),
                random.randint(15,20)
            ]
        }

        students.append(record)

    return students


# Function 2
def mutate_data(data, divisor):

    for i in range(len(data)):

        if i % divisor == 0:

            data[i]["marks"]=int(
                data[i]["marks"]+
                math.sqrt(data[i]["marks"])
            )

            data[i]["attendance"]-=5

            data[i]["scores"][0]+=5

    return data


# Function 3
def analyze_data(original,modified):

    original_marks=np.array(
        [x["marks"] for x in original]
    )

    modified_marks=np.array(
        [x["marks"] for x in modified]
    )

    mean_original=np.mean(original_marks)
    mean_modified=np.mean(modified_marks)

    median=np.median(modified_marks)

    std=np.std(modified_marks)

    drift=abs(
        mean_original-mean_modified
    )


    # manual metric (without NumPy)
    total=0
    for x in modified_marks:
        total+=x

    manual_mean=total/len(modified_marks)


    # normalize
    mn=min(modified_marks)
    mx=max(modified_marks)

    normalized=[
        (x-mn)/(mx-mn)
        for x in modified_marks
    ]

    return mean_modified,median,std,drift,manual_mean


# Function 4
def detect_pattern(drift,std,original,shallow):

    threshold=5

    copy_failure=False

    for i in range(len(original)):
        if original[i]["scores"]!=deep_original[i]["scores"]:
            copy_failure=True


    if copy_failure:
        return "Copy Failure Detected"

    elif drift>threshold:
        return "Critical Drift"

    elif std<10:
        return "Stable Data"

    else:
        return "Minor Drift"



# MAIN

students=generate_data(10)

deep_original=copy.deepcopy(students)

shallow_copy=copy.copy(students)
deep_copy=copy.deepcopy(students)

divisor=2

mutate_data(shallow_copy,divisor)
mutate_data(deep_copy,divisor)

df_original=pd.DataFrame(students)
df_shallow=pd.DataFrame(shallow_copy)
df_deep=pd.DataFrame(deep_copy)


mean_val,median,std_dev,drift,manual_mean=analyze_data(
deep_original,
deep_copy
)

status=detect_pattern(
drift,
std_dev,
students,
shallow_copy
)


print("\nOriginal Data")
print(df_original)

print("\nShallow Copy")
print(df_shallow)

print("\nDeep Copy")
print(df_deep)

print("\nDrift:",drift)

summary=(
mean_val,
drift,
std_dev
)

print("\nTuple Summary:")
print(summary)

print("\nFinal Classification:")
print(status)