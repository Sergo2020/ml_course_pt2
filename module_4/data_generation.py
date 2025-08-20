import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import statsmodels.formula.api as smf

# Set seed for reproducibility
np.random.seed(42)

# Sample size
n = 300

# Categorical moderator variable (e.g., gender: Male, Female)
moderator = np.random.choice(['Undergraduate', 'Graduate'], size=n)

# Explanatory variable with 3 levels (e.g., treatment group)
explanatory = np.random.choice(['Control', 'Low-Tech', 'Hi-Tech'], size=n)

# Create interaction effect
# Base outcome

# Add effects based on moderator and explanatory variable
effect = np.ones(n)
effect[(moderator == 'Graduate') & (explanatory == 'Hi-Tech')] = 7.
# Dependent variable (e.g., performance score)
outcome = np.random.normal(loc=50, scale=2, size=n) + effect + np.random.normal(loc=0, scale=5, size=n)

# Create DataFrame
df = pd.DataFrame({
    'Moderator': moderator,
    'Explanatory': explanatory,
    'Outcome': outcome
})


df.to_csv('graduate_moderator.csv')
# Preview
print(df.head())

group_A_x = df[df['Explanatory'] == 'Low-Tech']['Moderator'].values
group_A_y = df[df['Explanatory'] == 'Low-Tech']['Outcome'].values

group_B_x = df[df['Explanatory'] == 'Hi-Tech']['Moderator'].values
group_B_y = df[df['Explanatory'] == 'Hi-Tech']['Outcome'].values

group_C_x = df[df['Explanatory'] == 'Control']['Moderator'].values
group_C_y = df[df['Explanatory'] == 'Control']['Outcome'].values

# Plot scatter points
plt.scatter(group_A_x, group_A_y, color='blue', label='Low-Tech', alpha = 0.5)
plt.scatter(group_B_x, group_B_y, color='green', label='Hi-Tech', alpha = 0.5)
plt.scatter(group_C_x, group_C_y, color='red', label='Control', alpha = 0.5)


# Labels and legend
plt.title("Moderation Effect with Pyplot Only")
plt.xlabel("Explanatory Variable")
plt.ylabel("Outcome Variable (Salary)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('chart.png')
plt.close()

moderator_df = pd.read_csv('graduate_moderator.csv')
smf_results = smf.ols(formula='Outcome ~ C(Moderator) * C(Explanatory)', data=moderator_df).fit()
p_value = smf_results.f_pvalue
print('C(Moderator) * C(Explanatory)\n', p_value)

smf_results = smf.ols(formula='Outcome ~ C(Explanatory)', data=moderator_df).fit()
p_value = smf_results.f_pvalue
print('C(Explanatory)\n', p_value)
smf_results = smf.ols(formula='Outcome ~ C(Moderator)', data=moderator_df).fit()
p_value = smf_results.f_pvalue
print('C(Moderator)\n', p_value)






