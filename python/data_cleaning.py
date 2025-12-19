import pandas as pd
import numpy as np
df = pd.read_csv("E:\kaggle data sets\car_prices.csv")
# df.head()
# df.tail()
# df.info()
# df.describe()
df.isnull().sum()

df.duplicated().sum()
df = df.drop_duplicates(subset='vin')
df = df.dropna(subset=['year', 'make', 'model', 'sellingprice', 'saledate'])
numeric_cols = ['year', 'condition', 'odometer', 'mmr', 'sellingprice']

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

categorical_cols = [
    'make', 'model', 'trim', 'body', 'transmission',
    'state', 'color', 'interior', 'seller'
]

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

df['year'] = df['year'].astype(int)
df['sellingprice'] = df['sellingprice'].astype(float)
df['mmr'] = df['mmr'].astype(float)
df['odometer'] = df['odometer'].astype(float)

df['saledate'] = pd.to_datetime(df['saledate'])

df['saledate'] = pd.to_datetime(
    df['saledate'],
    errors='coerce',
    utc=True
)

df = df.dropna(subset=['saledate'])

df['car_age'] = df['saledate'].dt.year - df['year']
df[['year', 'saledate', 'car_age']].head()

df.info()

