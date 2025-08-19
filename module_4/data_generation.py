import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

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
base = np.random.normal(loc=50, scale=10, size=n)

# Add effects based on moderator and explanatory variable
effect = (
    (moderator == 'Graduate') * 5 +  # Females score higher
    (explanatory == 'Low-Tech') * 10 +
    (explanatory == 'Hi-Tech') * 15 +
    ((moderator == 'Graduate') & (explanatory == 'Hi-Tech')) * 20  # interaction boost
)

# Dependent variable (e.g., performance score)
outcome = base + effect + np.random.normal(loc=0, scale=5, size=n)

# Create DataFrame
df = pd.DataFrame({
    'Moderator': moderator,
    'Explanatory': explanatory,
    'Outcome': outcome
})

# Preview
print(df.head())

group_A_x = df[df['Explanatory'] == 'Low-Tech']['Moderator'].values
group_A_y = df[df['Explanatory'] == 'Low-Tech']['Outcome'].values

group_B_x = df[df['Explanatory'] == 'Hi-Tech']['Moderator'].values
group_B_y = df[df['Explanatory'] == 'Hi-Tech']['Outcome'].values

# Plot scatter points
plt.scatter(group_A_x, group_A_y, color='blue', label='Moderator A', alpha = 0.5)
plt.scatter(group_B_x, group_B_y, color='green', label='Moderator B', alpha = 0.5)


# Labels and legend
plt.title("Moderation Effect with Pyplot Only")
plt.xlabel("Explanatory Variable")
plt.ylabel("Outcome Variable")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




