import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns


class Visualizer:
    def __init__(self, output_dir="results"):
        self.output_dir = output_dir
        sns.set_theme(style="whitegrid")

    def system_timeseries(self, df):
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(df["datetime"], df["temperature_k"], color="tab:blue", linewidth=0.9)
        ax.set_title("System Temperature Time Series")
        ax.set_xlabel("Time")
        ax.set_ylabel("Temperature (K)")
        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(f"{self.output_dir}/system_timeseries.png", dpi=150)
        plt.close(fig)

    def pressure_monitoring(self, df):
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(df["datetime"], df["still_pressure"], label="Still Pressure", linewidth=0.9)
        ax.plot(df["datetime"], df["pt3_pressure"], label="PT3 Pressure", linewidth=0.9)
        ax.plot(df["datetime"], df["pt4_pressure"], label="PT4 Pressure", linewidth=0.9)
        ax.set_title("Pressure Monitoring")
        ax.set_xlabel("Time")
        ax.set_ylabel("Pressure")
        ax.legend()
        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(f"{self.output_dir}/pressure_monitoring.png", dpi=150)
        plt.close(fig)

    def cooling_analysis(self, df):
        fig, axes = plt.subplots(1, 2, figsize=(13, 5))

        axes[0].plot(df["datetime"], df["water_cooling_inlet"], label="Inlet", linewidth=0.9)
        axes[0].plot(df["datetime"], df["water_cooling_outlet"], label="Outlet", linewidth=0.9)
        axes[0].set_title("Water Cooling Inlet/Outlet")
        axes[0].set_xlabel("Time")
        axes[0].set_ylabel("Temperature")
        axes[0].legend()

        if "cooling_difference" in df.columns:
            axes[1].plot(df["datetime"], df["cooling_difference"], color="tab:orange", linewidth=0.9)
        axes[1].set_title("Cooling Difference (Outlet - Inlet)")
        axes[1].set_xlabel("Time")
        axes[1].set_ylabel("Delta")

        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(f"{self.output_dir}/cooling_analysis.png", dpi=150)
        plt.close(fig)

    def correlation_heatmap(self, df):
        numeric_df = df.select_dtypes(include="number")
        corr = numeric_df.corr()

        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=False, cmap="coolwarm", center=0, ax=ax)
        ax.set_title("Correlation Heatmap")
        fig.tight_layout()
        fig.savefig(f"{self.output_dir}/correlation_heatmap.png", dpi=150)
        plt.close(fig)

    def anomaly_plot(self, df):
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(df["datetime"], df["temperature_k"], color="tab:blue", linewidth=0.8, label="Temperature")

        anomalies = df[df["sensor_status"] != "Normal"]
        if not anomalies.empty:
            ax.scatter(
                anomalies["datetime"],
                anomalies["temperature_k"],
                color="red",
                s=25,
                zorder=5,
                label="Anomaly",
            )

        ax.set_title("Anomaly Detection")
        ax.set_xlabel("Time")
        ax.set_ylabel("Temperature (K)")
        ax.legend()
        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(f"{self.output_dir}/anomaly_detection.png", dpi=150)
        plt.close(fig)
