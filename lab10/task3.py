import numpy as np


def classify_rainfall(average):
    if average >= 6:
        return "High"
    elif average > 3:
        return "Medium"
    else:
        return "Low"


if __name__ == "__main__":
    rainfall_data = np.array(
        [
            [9, 8, 6, 9, 7, 6, 8],
            [2, 1, 2, 3, 2, 3, 5],
            [3, 5, 5, 7, 3, 2, 6],
            [4, 3, 5, 6, 7, 3, 2],
        ]
    )
    averages = rainfall_data.mean(axis=1)
    classifications = np.vectorize(classify_rainfall)(averages)

    for i, (average, classification) in enumerate(
        zip(averages, classifications), start=1
    ):
        print(
            f"Week#{i} - Average Rainfall: {average:.2f}, Classification: {classification}"
        )
