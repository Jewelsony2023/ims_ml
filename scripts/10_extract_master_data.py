import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\Desktop\IMS_ML\data\retail_store_inventory.csv"
)

print("\nCATEGORIES\n")
print(df["Category"].value_counts())

print("\nPRODUCTS\n")
print(sorted(df["Product ID"].unique()))