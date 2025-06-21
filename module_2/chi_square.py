import pandas as pd
from scipy.stats import chi2_contingency
from itertools import combinations
from statsmodels.stats.multitest import multipletests

def preform_chi_square_test(data_df:pd.DataFrame):


    # Create a contingency table
    contingency_table = pd.crosstab(data_df['Education_Level'], data_df['Job_Satisfaction'])

    # Perform the Chi-Square test
    _, p_value, _, _ = chi2_contingency(contingency_table)

    return p_value

def post_hoc(data_df:pd.DataFrame):
    edu_levels = data_df['Education_Level'].unique()
    pairs = list(combinations(edu_levels, 2))

    p_values = []
    pair_labels = []

    for pair in pairs:
        subset = data_df[data_df['Education_Level'].isin(pair)]
        table = pd.crosstab(subset['Education_Level'], subset['Job_Satisfaction'])
        chi2, p, _, _ = chi2_contingency(table)
        p_values.append(p)
        pair_labels.append(f"{pair[0]} vs {pair[1]}")


    # Show results
    for label, p_val in zip(pair_labels, p_values):
        reject = p_val <= 0.05
        print(f"{label}: raw p = {p_val:.4f}, reject null-hypothesis: {reject}")

def print_results(p_val):
    if p_val >= 0.05:
        print(f'p={p_val:.2f}: No effect of education level to job satisfaction.')
    else:
        print(f'p={p_val:.2f}: Education level has an effect to job satisfaction.')

if __name__ == '__main__':

    balanced_df = pd.read_csv('balanced.csv')
    p_balanced = preform_chi_square_test(balanced_df)
    print_results(p_balanced)
    post_hoc(balanced_df)

    unbalanced_df = pd.read_csv('unbalanced.csv')
    p_balanced = preform_chi_square_test(unbalanced_df)
    print_results(p_balanced)
    post_hoc(unbalanced_df)