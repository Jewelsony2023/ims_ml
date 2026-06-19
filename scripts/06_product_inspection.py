#for sanity check 
import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\Desktop\IMS_ML\data\retail_store_inventory.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

sales = (
    df.groupby(["Date", "Product ID"])["Units Sold"]
    .sum()
    .reset_index()
)

sku = "P0016"

product = (
    sales[sales["Product ID"] == sku]
    .sort_values("Date")
)

print(product.head())

print("\n")

print(product.tail())

print("\n")

print(product["Units Sold"].describe())