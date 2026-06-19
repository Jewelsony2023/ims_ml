import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\Desktop\IMS_ML\data\retail_store_inventory.csv"
)
print("\nSHAPE")
print(df.shape)

print("\nCOLUMNS")
print(df.columns.tolist())

print("\nDATE RANGE")
print(df["Date"].min())
print(df["Date"].max())

print("\nUNIQUE PRODUCTS")
print(df["Product ID"].nunique())

print("\nUNIQUE STORES")
print(df["Store ID"].nunique())

print("\nMISSING VALUES")
print(df.isnull().sum())