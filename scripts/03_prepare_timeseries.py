import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\Desktop\IMS_ML\data\retail_store_inventory.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

product_sales = (
    df.groupby(["Date", "Product ID"])["Units Sold"]
    .sum()
    .reset_index()
)

print(product_sales.head())

print("\n")

print(product_sales.shape)

print("\n")

print(
    product_sales.groupby("Product ID")
    .size()
)