import os
import pandas as pd
import numpy as np

np.random.seed(42)

samples = 500
time = pd.date_range(start="2026-01-01", periods=samples, freq="min")

temperature = 0.015 + np.random.normal(0, 0.00003, samples)

# Create abnormal temperature events
temperature[120] = 0.0158
temperature[300] = 0.0162
temperature[420] = 0.0157

df = pd.DataFrame({
    "datetime": time,
    "temperature_k": temperature,
    "mixture_flow": 10 + np.random.normal(0, 0.2, samples),
    "still_pressure": 1.2 + np.random.normal(0, 0.01, samples),
    "pid_output_power": 50 + np.random.normal(0, 1, samples),
    "water_cooling_inlet": 290 + np.random.normal(0, 0.5, samples),
    "water_cooling_outlet": 292 + np.random.normal(0, 0.5, samples),
    "pt3_pressure": 0.8 + np.random.normal(0, 0.01, samples),
    "pt4_pressure": 0.7 + np.random.normal(0, 0.01, samples),
})

df["sensor_status"] = "Normal"
df.loc[df["temperature_k"] > 0.0155, "sensor_status"] = "Spike"

output_path = os.path.join(os.path.dirname(__file__), "cryogenic_data.csv")
df.to_csv(output_path, index=False)

print("Dataset generated successfully")
