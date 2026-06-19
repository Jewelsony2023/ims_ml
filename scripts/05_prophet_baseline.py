import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error
from prophet import Prophet


df = pd.read_csv(r"C:\Users\HP\Desktop\IMS_ML\data\retail_store_inventory.csv")
df["Date"] = pd.to_datetime(df["Date"])

sales = (
    df.groupby(["Date", "Product ID"])["Units Sold"]
    .sum()
    .reset_index()
)

sku = "P0016"
product_data = sales[sales["Product ID"] == sku].sort_values("Date")

prophet_data = product_data[["Date", "Units Sold"]].rename(
    columns={"Date": "ds", "Units Sold": "y"}
)

train_size = int(len(prophet_data) * 0.8)
train = prophet_data.iloc[:train_size].copy()
test = prophet_data.iloc[train_size:].copy()

print("Train size:", len(train))
print("Test size:", len(test))

model = Prophet()
model.fit(train)

future = model.make_future_dataframe(periods=len(test), freq="D", include_history=True)
forecast = model.predict(future)

predictions = forecast.iloc[-len(test):][["ds", "yhat"]].copy()
comparison = test[["ds", "y"]].merge(predictions, on="ds", how="left")

mape = mean_absolute_percentage_error(comparison["y"], comparison["yhat"]) * 100

print("SKU:", sku)
print("Prophet MAPE:", round(mape, 2), "%")
