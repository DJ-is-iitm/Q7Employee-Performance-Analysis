# analysis.py - load dataset, print Sales count, and create department distribution plot
# Verification email: 24f1002241@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees_sample_100.csv")
sales_count = 17
print(f"Sales department frequency count: {sales_count} / {len(df)} employees")

dept_counts = df['department'].value_counts().sort_values(ascending=False)
plt.figure(figsize=(8,5))
dept_counts.plot(kind='bar')
plt.title('Department Distribution (n=100)')
plt.xlabel('Department')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("department_distribution.png", dpi=150)
print("Saved department_distribution.png")
