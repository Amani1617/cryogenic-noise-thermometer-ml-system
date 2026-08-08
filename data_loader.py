import pandas as pd


class DataLoader:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        df = pd.read_csv(self.path)
        return df

    def validate_columns(self, df):
        required_columns = [
            "datetime",
            "temperature_k",
            "mixture_flow",
            "still_pressure",
            "pid_output_power",
            "water_cooling_inlet",
            "water_cooling_outlet",
            "pt3_pressure",
            "pt4_pressure",
            "sensor_status",
        ]

        missing = []
        for column in required_columns:
            if column not in df.columns:
                missing.append(column)

        if missing:
            raise Exception(f"Missing columns: {missing}")

        return True

    def preprocess_datetime(self, df):
        df["datetime"] = pd.to_datetime(df["datetime"])
        return df
