import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


class RegressionModels:
    def train(self, df):
        features = [
            "mixture_flow",
            "still_pressure",
            "pid_output_power",
            "water_cooling_inlet",
            "water_cooling_outlet",
            "pt3_pressure",
            "pt4_pressure",
        ]

        X = df[features]
        y = df["temperature_k"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        models = {
            "Linear Regression": LinearRegression(),
            "Random Forest": RandomForestRegressor(random_state=42),
        }

        results = ""
        for name, model in models.items():
            model.fit(X_train, y_train)
            prediction = model.predict(X_test)
            rmse = np.sqrt(mean_squared_error(y_test, prediction))
            results += f"{name}\nRMSE: {rmse}\n\n"

        with open("results/regression_results.txt", "w") as file:
            file.write(results)
