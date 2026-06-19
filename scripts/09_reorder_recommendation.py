import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\Desktop\IMS_ML\data\retail_store_inventory.csv"
)

forecast = pd.read_csv(
    r"C:\Users\HP\Desktop\IMS_ML\forecasts\30_day_forecast.csv"
)

latest_inventory = (
    df.sort_values("Date")
    .groupby("Product ID")
    .tail(1)
)

inventory = (
    latest_inventory
    .groupby("Product ID")["Inventory Level"]
    .sum()
)

forecast_30 = (
    forecast
    .groupby("Product ID")["ForecastDemand"]
    .sum()
)

results = []

for sku in forecast_30.index:

    current_stock = inventory.get(
        sku,
        0
    )

    demand = forecast_30[sku]

    safety_stock = demand * 0.2

    recommended_order = max(
        0,
        demand + safety_stock - current_stock
    )

    if current_stock < demand:
        risk = "HIGH"
    elif current_stock < demand * 1.2:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    results.append(
        {
            "Product ID": sku,
            "Current Inventory": round(current_stock),
            "Forecast Demand": round(demand),
            "Safety Stock": round(safety_stock),
            "Recommended Order": round(
                recommended_order
            ),
            "Risk Level": risk
        }
    )

recommendations = pd.DataFrame(
    results
)

print(recommendations)

recommendations.to_csv(
    r"C:\Users\HP\Desktop\IMS_ML\forecasts\reorder_recommendations.csv",
    index=False
)

print(
    "\nSaved: forecasts/reorder_recommendations.csv"
)