from pathlib import Path

import numpy as np
import pandas as pd

from faker import Faker
from matplotlib import pyplot as plt

fake = Faker()


def generate_group_size(n_groups: int, n_students):
    values = np.random.rand(n_groups)
    values = (values / values.sum()) * n_students
    values = values.astype(int)

    if values.sum() < n_students:
        diff = n_students - values.sum()
        values[-1]+=diff

    return values.astype(int)


def make_grades(avg: float | int, std: float | int, n_samples: int):
    grades = np.random.normal(avg, std, n_samples).astype(int)

    grades[grades > 100] = 100
    grades[grades < 55] = 55

    return grades


def draw_data(df, methods, dst_path):
    plt.figure(figsize=(8,6))

    for method in methods:
        plt.hist(df[df["Study_Method"]==method]["Test_Score"].values, bins = 50, alpha = 0.4, label = method)

    plt.legend()
    plt.grid()
    plt.tight_layout()

    plt.savefig(dst_path.stem + '.png')

def make_table(balanced: bool, size: int, dst_path: Path | str) -> None:
    dst_path = Path(dst_path)
    # Generate data
    methods = ["ChatGPT", "Self-Study", "Tutoring", "Group Study"]

    student_names = [fake.name() for _ in range(size)]

    if balanced:
        student_method = [str(np.random.choice(methods)) for _ in range(size)]
        student_grades = make_grades(75, 10, size)

    else:
        student_method = []
        student_grades = []
        n_per_group = generate_group_size(len(methods), size)

        for (idx, method), group_size in zip(enumerate(methods),n_per_group) :
            student_method = student_method + [method] * group_size
            student_grades = student_grades + make_grades(70 + idx * 5, 5, group_size).tolist()

    data = {"Student_Name": student_names,
            "Study_Method": student_method,
            "Test_Score": student_grades}

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv(dst_path, index=False)
    print(f"CSV file {dst_path.name} created successfully!")

    draw_data(df, methods, dst_path)


if __name__ == "__main__":
    make_table(True, 1000, 'balanced_data.csv')
    make_table(False, 1000, 'unbalanced_data.csv')


