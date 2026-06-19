import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\Desktop\IMS_ML\data\retail_store_inventory.csv"
)

mapping = (
    df.groupby("Product ID")["Category"]
    .first()
    .reset_index()
)

print(mapping)

mapping.to_csv(
    r"C:\Users\HP\Desktop\IMS_ML\forecasts\product_category_mapping.csv",
    index=False
)

print("\nSaved product_category_mapping.csv")