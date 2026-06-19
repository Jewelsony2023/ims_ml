import pandas as pd

results = pd.DataFrame(
    {
        "Model": [
            "ARIMA",
            "Prophet",
            "LightGBM"
        ],
        "MAPE": [
            67.32,
            37.28,
            38.26
        ]
    }
)

results = results.sort_values(
    by="MAPE"
)

print(results)

results.to_csv(
    r"C:\Users\HP\Desktop\IMS_ML\forecasts\model_comparison.csv",
    index=False
)

print("\nSaved:")
print("forecasts/model_comparison.csv")

print(
    "\nBest Model:",
    results.iloc[0]["Model"]
)