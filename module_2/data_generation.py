from pathlib import Path

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


# Define categories

def generate_group_size(n_groups: int, n_students):
    values = np.random.rand(n_groups)
    values = (values / values.sum()) * n_students
    values = values.astype(int)

    if values.sum() < n_students:
        diff = n_students - values.sum()
        values[-1] += diff

    return values.astype(int)


def make_table(balanced: bool, size: int, dst_path: Path | str) ->  pd.DataFrame:
    education_levels = ["High School", "Bachelor's", "Master's", "PhD"]
    job_satisfaction = ["Low", "Medium", "High"]

    if balanced:
        edu_level_list = [random.choice(education_levels) for _ in range(size)]
        sate_list = [random.choice(job_satisfaction) for _ in range(size)]

        data = {"Education_Level": edu_level_list,
                "Job_Satisfaction": sate_list}

    else:
        n_levels = len(education_levels)
        n_per_group = generate_group_size(n_levels, size)

        edu_level_list = []
        sate_list = []

        probs_list = [
            [0.7, 0.2, 0.1],  # Lowest education level – mostly low satisfaction
            [0.4, 0.4, 0.2],  # Next level – more medium satisfaction
            [0.2, 0.4, 0.4],  # Higher level – now mostly high satisfaction
            [0.1, 0.2, 0.7]  # Highest education – predominantly high satisfaction
        ]

        for (idx, edu_level), group_size, probs in zip(enumerate(education_levels), n_per_group, probs_list):
            edu_level_list += [edu_level] * group_size
            sate_list += [random.choices(job_satisfaction, weights=probs)[0] for _ in range(group_size)]

        data = {"Education_Level": edu_level_list,
                "Job_Satisfaction": sate_list}

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save dataset to CSV
    df.to_csv(dst_path)

    return df


def draw_data(df, dst_path):
    counts = df.groupby(["Education_Level", "Job_Satisfaction"]).size().unstack()
    x_labels = counts.index
    x = np.arange(len(x_labels))

    # Set the theme for better visuals

    # Create count plot
    plt.figure(figsize=(10, 5))

    width = 0.3
    plt.bar(x - width, counts["Low"], width, label="Low")
    plt.bar(x, counts["Medium"], width, label="Medium")
    plt.bar(x + width, counts["High"], width, label="High")

    # Formatting
    plt.xticks(x, labels=x_labels)
    plt.xlabel("Education Level")
    plt.ylabel("Count")
    plt.title("Job Satisfaction by Education Level")
    plt.legend(title="Job Satisfaction")

    # Show the plot
    plt.savefig(dst_path)
    plt.close()


if __name__ == '__main__':
    balanced_df = make_table(True, 1000, 'balanced.csv')
    unbalanced_df = make_table(False, 1000, 'unbalanced.csv')

    draw_data(balanced_df, 'balanced.png')
    draw_data(unbalanced_df, 'unbalanced.png')