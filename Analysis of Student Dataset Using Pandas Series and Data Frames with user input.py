
import pandas as pd

n = int(input("Enter the number of students: "))

roll_no = []
names = []
departments = []
marks_list = []

for i in range(n):
    print(f"\nEnter details of student {i + 1}")

    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    mark = float(input("Enter Mark: "))

    roll_no.append(roll)
    names.append(name)
    departments.append(department)
    marks_list.append(mark)

# Pandas Series
marks = pd.Series(marks_list, index=names)

print("\n--- Pandas Series ---")
print(marks)

# Pandas DataFrame
data = {
    "RollNo": roll_no,
    "Name": names,
    "Department": departments,
    "Mark": marks_list
}

df = pd.DataFrame(data)

print("\n--- DataFrame ---")
print(df)

# Average Mark
print("\nAverage Mark:", round(df["Mark"].mean(), 2))

# Students scoring above 85
print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])
