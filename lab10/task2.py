import numpy as np

# Write program to print the following:
# •	students’ names who got above 90 in the homework.
# •	Highest grade
# •	Lowest grade
# •	Randomly pick a student name to solve the homework.
# First you should create two arrays :
# Array 1: students’ names
# Array 2: to hold the students' grades.

if __name__ == "__main__":
    students = np.array(["Mamdouh", "Ali", "Omar"])
    grades = np.array([76, 99, 100])
    print(
        f"Students 90+: {np.array([students[idx] for idx, i in enumerate(grades) if i>=90])}"
    )
    print(f"Highest Grade: {grades.max()}")
    print(f"Highest Grade: {grades.min()}")
    print(f"{np.random.choice(students)} will solve the homework")
