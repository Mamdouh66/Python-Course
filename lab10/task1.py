import numpy as np

# Write a program to sort the students’ names and spilt it into two groups each group has 5 students.
# with numpy
# Sample Output:
# group 1: ['Eman' 'Haya' 'Lama' 'Maha' 'Mona']
# group 2: ['Noha' 'Reem' 'Renad' 'Sara' 'Waad']

if __name__ == "__main__":
    full_group = np.array(
        [
            "Eman",
            "Haya",
            "Lama",
            "Maha",
            "Mona",
            "Noha",
            "Reem",
            "Renad",
            "Sara",
            "Waad",
        ]
    )
    print(np.array_split(full_group, 2))
