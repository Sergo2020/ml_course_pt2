## Moderator

### Data

For this assignment I generated data. In this hypothetical experiment presented data from salary analysis of `Low-Tech`
and `Hi-Tech` industry based on education level (`Graduate` and `Undergraduate`). In addition, control group salary is collected.
### Dataset info:
Observe that `Graduate` within `Hi-Tech` industry have slightly higher salary.
![image](module_4/chart.png)

### Exploring the data
Assume that we have zero prior knowledge about the data.
1. Relation between industry groups by ad-hoc method. Based on result below (Tab. 1), there is no significant difference between populations.
2. Effect on industry, education and their combined effect. As we see from results only combination of both makes difference. 

#### Table 1:

| Industry A | Industry B | Mean Diff | p-adj  | Lower    | Upper    | Reject |
|------------|------------|-----------|--------|----------|----------|--------|
| Control    | Hi-Tech    | 2.034     | 0.058  | -0.0533  | 4.1212   | False  |
| Control    | Low-Tech   | 0.4374    | 0.8683 | -1.5970  | 2.4717   | False  |
| Hi-Tech    | Low-Tech   | -1.5966   | 0.168  | -3.6742  | 0.4810   | False  |

#### $p$ values per relation:

- 0.00: The industry and education combined method significantly affects outcome. ('Outcome' ~ 'C(Moderator) * C(Explanatory)')
- 0.06: No significant difference between education levels . ('Outcome' ~ C(Explanatory)')
- 0.06: No significant difference between industry . ('Outcome' ~ 'C(Explanatory)')
