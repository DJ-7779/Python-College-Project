import pandas as pd

n = int(input("Enter the number of students: "))

data = {
    "Name": [],
    "Department": [],
    "Attendance": [],
    "Mark": []
}

for i in range(n):
    print(f"\nEnter details of student {i + 1}")

    name = input("Enter Name: ")
    department = input("Enter Department: ")

    attendance = input("Enter Attendance (press Enter if missing): ")
    mark = input("Enter Mark (press Enter if missing): ")

    data["Name"].append(name)
    data["Department"].append(department)

    data["Attendance"].append(
        float(attendance) if attendance.strip() else None
    )

    data["Mark"].append(
        float(mark) if mark.strip() else None
    )

df = pd.DataFrame(data)

print("\n--- Original Dataset ---")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Missing value treatment
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

# Remove duplicate records
df = df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(df)

print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))

print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))