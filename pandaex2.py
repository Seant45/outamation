import pandas as pd

# load the csv (same folder, so just the filename)
df = pd.read_csv("bank_loan.csv")

# inspect
print(df.head())
print(df.info())
print(df.isna().sum())

# cleaning
df['CCAvg'] = df['CCAvg'].astype(str)
df['ZIP Code'] = df['ZIP Code'].astype(str)

# verify
print(df.dtypes)

# save cleaned file
df.to_csv("bank_loan_cleaned.csv", index=False)
