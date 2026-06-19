import pandas as pd

from prophet import Prophet

df = pd.read_csv(
    r"C:\Users\HP\Desktop\IMS_ML\data\retail_store_inventory.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

top_products = [
    "P0016",
    "P0020",
    "P0014",
    "P0015",
    "P0005"
]

all_forecasts = []

for sku in top_products:

    sales = (
        df[df["Product ID"] == sku]
        .groupby("Date")["Units Sold"]
        .sum()
        .reset_index()
    )

    prophet_df = sales.rename(
        columns={
            "Date": "ds",
            "Units Sold": "y"
        }
    )

    model = Prophet()

    model.fit(prophet_df)

    future = model.make_future_dataframe(
        periods=30
    )

    forecast = model.predict(future)

    next_30 = forecast.tail(30)[
        ["ds", "yhat"]
    ]

    next_30["Product ID"] = sku

    all_forecasts.append(next_30)

final_forecast = pd.concat(
    all_forecasts
)

final_forecast.rename(
    columns={
        "ds": "Date",
        "yhat": "ForecastDemand"
    },
    inplace=True
)

print(final_forecast.head())

final_forecast.to_csv(
    r"C:\Users\HP\Desktop\IMS_ML\forecasts\30_day_forecast.csv",
    index=False
)

print(
    "\nSaved: forecasts/30_day_forecast.csv"
)