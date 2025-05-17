import numpy as np
import pandas as pd 
stu = pd.DataFrame({
    "Name": ["Pikachu", "Lucario", "Greninja", "Eevee", "Gardevoir", 
             "Infernape", "Decidueye", "Togekiss", "Dragapult", "Cinderace"],
    "RollNum": [12, 69, 34, 32, 33, 45, 23, 56, 78, 89],
    "Gender": ["M", "M", "M", "F", "F", "M", "M", "F", "M", "M"],
    "Marks1": [23, 100, 56, 43, 67, 90, 50, 60, 70, 85],
    "Marks2": [56, 100, 45, 23, 78, 88, 67, 77, 89, 92],
    "Marks3": [76, 100, 56, 33, 78, 94, 54, 70, 80, 81]})
stu.index = np.arange(1,len(stu)+1)
stu["Total"] = stu["Marks1"]+stu["Marks2"]+stu["Marks3"]
print(stu)
min_marks1_row = stu.loc[stu["Marks1"].idxmin(), ["Name", "Marks1"]]
max_marks2_row = stu.loc[stu["Marks2"].idxmax(), ["Name", "Marks2"]]
average_marks3 = stu["Marks3"].mean()

print(f"Minimum:\n{min_marks1_row}\n")
print(f"Maximum:\n{max_marks2_row}\n")
print(f"Average Marks3:\n{average_marks3}\n")
average = stu["Total"]/3
print("The higest average :\n")
print(stu.loc[average.idxmax(),["Name"]])
print("The failures according to marks2 are :\n")
print(stu.loc[stu["Marks2"]<40,["Name","Marks2"]])
