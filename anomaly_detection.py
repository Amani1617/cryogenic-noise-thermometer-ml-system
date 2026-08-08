import numpy as np


class AnomalyDetector:
    def __init__(self, threshold=3):
        self.threshold = threshold

    def detect_spikes(self, series):
        mean = np.mean(series)
        std = np.std(series)
        z_score = (series - mean) / std
        anomalies = abs(z_score) > self.threshold
        return anomalies

    def assign_status(self, df):
        df["sensor_status"] = "Normal"
        spikes = self.detect_spikes(df["temperature_k"])
        df.loc[spikes, "sensor_status"] = "Spike"
        return df
