import json


class Analyzer:
    def calculate_statistics(self, df):
        statistics = {
            "temperature_mean": float(df["temperature_k"].mean()),
            "temperature_std": float(df["temperature_k"].std()),
            "temperature_min": float(df["temperature_k"].min()),
            "temperature_max": float(df["temperature_k"].max()),
            "pressure_mean": float(df["still_pressure"].mean()),
            "mixture_flow_mean": float(df["mixture_flow"].mean()),
            "number_of_measurements": int(len(df)),
        }
        return statistics

    def save_statistics(self, statistics):
        with open("results/statistics.json", "w") as file:
            json.dump(statistics, file, indent=4)

    def generate_insights(self, df):
        anomalies = df["sensor_status"].value_counts().to_dict()

        text = """
Cryogenic Monitoring System Insights
-----------------------------------
Dataset size: {}
Average temperature: {:.6f} K
Maximum temperature: {:.6f} K
Detected sensor conditions: {}

The system analysis was completed successfully.
""".format(
            len(df),
            df["temperature_k"].mean(),
            df["temperature_k"].max(),
            anomalies,
        )

        with open("results/insights.txt", "w") as file:
            file.write(text)
