import datetime


class ReportGenerator:
    def generate(self, df):
        total = len(df)
        anomalies = df[df["sensor_status"] != "Normal"].shape[0]

        report = f"""
=================================================
Cryogenic Noise Thermometer Monitoring System
Final Automated Report
=================================================

Generated: {datetime.datetime.now()}

Dataset Information
-------------------
Total measurements: {total}

System Analysis
---------------
Detected abnormal events: {anomalies}
Average temperature: {df["temperature_k"].mean():.8f} K
Maximum temperature: {df["temperature_k"].max():.8f} K
Minimum temperature: {df["temperature_k"].min():.8f} K

Status: """

        if anomalies == 0:
            report += "System Stable"
        else:
            report += "System requires attention"

        with open("results/final_report.txt", "w") as file:
            file.write(report)
