import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\Desktop\IMS_ML\data\retail_store_inventory.csv"
)

print("\nSHAPE")
print(df.shape)

print("\nDATE RANGE")
print(df["Date"].min())
print(df["Date"].max())

print("\nUNIQUE PRODUCTS")
print(df["Product ID"].nunique())

print("\nUNIQUE STORES")
print(df["Store ID"].nunique())

print("\nCATEGORIES")
print(df["Category"].value_counts())

print("\nTOP PRODUCTS")
print(
    df.groupby("Product ID")["Units Sold"]
    .sum()
    .sort_values(ascending=False)
    .head(20)
)

print("\nROWS PER PRODUCT")
print(
    df.groupby("Product ID")
    .size()
    .describe()
)