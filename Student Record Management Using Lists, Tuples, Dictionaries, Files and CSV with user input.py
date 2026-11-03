import csv

students = []

# Get student details from user
n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of Student {i + 1}")

    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    mark = int(input("Enter Mark: "))

    students.append({
        "RollNo": roll,
        "Name": name,
        "Department": dept,
        "Mark": mark
    })

# Tuple example: fixed course details
course = ("Python", 4)
print("\nCourse Tuple:", course)

# Write text file
with open("students.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")

# Write CSV file
with open("students.csv", "w", newline="") as file:
    fields = ["RollNo", "Name", "Department", "Mark"]

    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

# Read CSV file
print("\n--- Records from CSV ---")

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["RollNo"], row["Name"],
              row["Department"], row["Mark"])