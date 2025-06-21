from pathlib import Path

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi

from module_1.data_generation import draw_data

def print_results(p_val):
    if p_val >= 0.05:
        print(f'{p_val:.2f}: No significant difference between study methods.')
    else:
        print(f'{p_val:.2f}: The study method significantly affects test scores.')


def test_anova(df):
    smf_results = smf.ols(formula='Test_Score ~ C(Study_Method)', data=df).fit()
    p_value = smf_results.f_pvalue
    return p_value

def test_tukey(df):
    mc1 = multi.MultiComparison(df['Test_Score'], df['Study_Method'])
    res1 = mc1.tukeyhsd()
    print(res1.summary())

balanced_data = pd.read_csv('balanced_data.csv')
unbalanced_data = pd.read_csv('unbalanced_data.csv')

# p_val1 = test_anova(balanced_data)
# print_results(p_val1)
#
# p_val2 = test_anova(unbalanced_data)
# print_results(p_val2)

balanced_spe_data = balanced_data.copy()
balanced_spe_data.loc[balanced_spe_data['Study_Method'] == 'ChatGPT', 'Test_Score'] = balanced_spe_data[balanced_spe_data['Study_Method'] == 'ChatGPT']['Test_Score'] - 20

unbalanced_spe_data = unbalanced_data.copy()
unbalanced_spe_data.loc[unbalanced_spe_data['Study_Method'] == 'ChatGPT', 'Test_Score'] = unbalanced_spe_data[unbalanced_spe_data['Study_Method'] == 'ChatGPT']['Test_Score'] - 20

draw_data(balanced_spe_data, ["ChatGPT", "Self-Study", "Tutoring", "Group Study"], Path('balanced_spe_data.png'))
draw_data(unbalanced_spe_data, ["ChatGPT", "Self-Study", "Tutoring", "Group Study"], Path('unbalanced_spe_data.png'))

p_val3 = test_anova(balanced_spe_data)
print_results(p_val3)

p_val4 = test_anova(unbalanced_spe_data)
print_results(p_val4)

test_tukey(balanced_data)
test_tukey(unbalanced_data)
test_tukey(balanced_spe_data)
test_tukey(unbalanced_spe_data)






