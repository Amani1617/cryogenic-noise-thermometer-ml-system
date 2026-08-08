from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


class ClassificationModel:
    def train(self, df):
        features = [
            "temperature_k",
            "mixture_flow",
            "still_pressure",
            "pid_output_power",
            "water_cooling_inlet",
            "water_cooling_outlet",
            "pt3_pressure",
            "pt4_pressure",
        ]

        X = df[features]
        y = df["sensor_status"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions, zero_division=0)

        output = f"""
Cryogenic Sensor Classification Results
--------------------------------------
Model: Random Forest Classifier
Accuracy: {accuracy:.3f}

Detailed Report:
{report}
"""

        with open("results/classification_results.txt", "w") as file:
            file.write(output)
