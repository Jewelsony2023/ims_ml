import pandas as pd

from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_percentage_error

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

product_data = (
    sales[sales["Product ID"] == sku]
    .sort_values("Date")
)

series = product_data["Units Sold"]

train_size = int(len(series) * 0.8)

train = series[:train_size]
test = series[train_size:]

print("Train:", len(train))
print("Test:", len(test))

model = ARIMA(
    train,
    order=(5,1,0)
)

model_fit = model.fit()

forecast = model_fit.forecast(
    steps=len(test)
)

mape = (
    mean_absolute_percentage_error(
        test,
        forecast
    ) * 100
)

print("\nSKU:", sku)
print("ARIMA MAPE:", round(mape,2), "%")