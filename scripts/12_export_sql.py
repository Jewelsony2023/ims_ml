import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\Desktop\IMS_ML\forecasts\reorder_recommendations.csv"
)

with open(
    r"C:\Users\HP\Desktop\IMS_ML\forecasts\forecast_insert.sql",
    "w",
    encoding="utf-8"
) as f:

    for _, row in df.iterrows():

        sql = (
            f"INSERT INTO ForecastResults "
            f"(ProductCode, ForecastDemand, RecommendedOrder, RiskLevel) "
            f"VALUES "
            f"('{row['Product ID']}', "
            f"{row['Forecast Demand']}, "
            f"{row['Recommended Order']}, "
            f"'{row['Risk Level']}');\n"
        )

        f.write(sql)

print("forecast_insert.sql created")