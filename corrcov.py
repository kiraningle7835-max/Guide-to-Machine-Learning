import pandas as pd
df = pd.DataFrame({
    'Maths': [70, 80, 90, 100,110],
    'Physics': [9,8,7,6,5],
    'Chemistry': [68, 78, 92, 55, 70]
})
print(df.quantile(0.2),df.corr(),df.cov())
