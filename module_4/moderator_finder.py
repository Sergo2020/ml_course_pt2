from pathlib import Path
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi


def test_anova(df,  outcome_col, explanatory_relation):
    smf_results = smf.ols(formula=f'{outcome_col} ~ {explanatory_relation}', data=df).fit()
    p_value = smf_results.f_pvalue
    return p_value

def test_tukey(df, outcome_col, explanatory_col):
    mc1 = multi.MultiComparison(df[outcome_col], df[explanatory_col])
    res1 = mc1.tukeyhsd()
    print(res1.summary())


def print_results(p_val, explanatory_var:str):
    if p_val >= 0.05:
        print(f'{p_val:.2f}: No significant difference between {explanatory_var} .')
    else:
        print(f'{p_val:.2f}: The {explanatory_var} method significantly affects outcome.')

if __name__ == '__main__':

    moderator_df = pd.read_csv('graduate_moderator.csv')

    p_val_ome = test_anova(moderator_df, 'Outcome', 'C(Moderator) * C(Explanatory)')
    p_val_oe = test_anova(moderator_df, 'Outcome', 'C(Explanatory)')
    p_val_om = test_anova(moderator_df, 'Outcome', 'C(Moderator)')

    print_results(p_val_ome, 'industry and education combined')
    print_results(p_val_oe, 'education levels')
    print_results(p_val_om, 'industry')

    test_tukey(moderator_df, 'Outcome', 'Explanatory')



