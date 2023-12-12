import pandas as pd
from scipy.stats import f_oneway

# Read CSV files into pandas DataFrames
df = pd.read_csv('merged_file_2.csv')

import pandas as pd

# Assuming 'data' is your DataFrame
# Replace this with your DataFrame or read from a CSV file


# Print unique columns of the DataFrame
unique_values = df['party'].unique()
print("Unique columns:", unique_values)

keys=['inc','tdp','trs','aimim','audf','bopf','bjp','jd(u)','rjd','ind','shs',
 'hjcbl','bsp','jkn','jd(s)','cpm','mul','kec(m)','ncp','bjd','sad','admk',
 'dmk','mdmk','rld','sp','aitc','jmm','jvm']
df['fmcg'] = pd.to_numeric(df['fmcg'],errors='coerce')
group1 = df[df['values'] == 0]['fmcg'].dropna()
group2 = df[df['values'] == 1]['fmcg'].dropna()
group3 = df[df['values'] == 2]['fmcg'].dropna()
print(group2)
f_statistic, p_value = f_oneway(group1,  group3)

print("Results of ANOVA test:")
print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")
# 0 right, 1 center, 2 left
# bopf
# values=[1,2,1,0,2,1,0,2,1,1,0,1,1,1,1,2,0,1,1,1,0,2,1,1,1,2,2,1,0]
"""
Name Literacy: 

Results of ANOVA test:
F-statistic: 3.200786150001297
P-value: 0.041975178773782096
 p- value < 0.05 implies statistical significance
"""

# mean for each groups
print(group1.mean())
print(group2.mean())
print(group3.mean())
"""
Name: water, Length: 180, dtype: float64
Results of ANOVA test:
F-statistic: 2.4014892717754934
P-value: 0.09225025621137035

Name: electricity, Length: 168, dtype: float64
Results of ANOVA test:
F-statistic: 11.790383847176496
P-value: 1.1786672594459991e-05

Name: fmcg, Length: 174, dtype: float64
Results of ANOVA test:
F-statistic: 2.457962765793805
P-value: 0.08732600617027239


"""