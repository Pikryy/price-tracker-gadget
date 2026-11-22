import pandas as pd
df = pd.read_csv("data/raw/cleaned_df.csv")
print(df.shape)
print(df.isna().sum())
print(df.describe())
print(df["price_tier"].value_counts())
print(df["charging_type"].value_counts().head())
print(df.duplicated().sum())