import os

from src.data_loader import DataLoader
from src.preprocessing import Preprocessor
from src.anomaly_detection import AnomalyDetector
from src.analysis import Analyzer
from src.visualization import Visualizer
from src.machine_learning import RegressionModels
from src.classification import ClassificationModel
from src.report_generator import ReportGenerator

# -------------------------
# Create results folder
# -------------------------
os.makedirs("results", exist_ok=True)

# -------------------------
# Load Dataset
# -------------------------
loader = DataLoader("data/cryogenic_data.csv")
df = loader.load_data()
loader.validate_columns(df)
df = loader.preprocess_datetime(df)

# -------------------------
# Preprocessing
# -------------------------
processor = Preprocessor()
df = processor.clean_data(df)
df = processor.create_features(df)

# -------------------------
# Anomaly Detection
# -------------------------
detector = AnomalyDetector()
df = detector.assign_status(df)

# -------------------------
# Statistical Analysis
# -------------------------
analysis = Analyzer()
statistics = analysis.calculate_statistics(df)
analysis.save_statistics(statistics)
analysis.generate_insights(df)

# -------------------------
# Visualization
# -------------------------
visual = Visualizer()
visual.system_timeseries(df)
visual.pressure_monitoring(df)
visual.cooling_analysis(df)
visual.correlation_heatmap(df)
visual.anomaly_plot(df)

# -------------------------
# Machine Learning
# -------------------------
regression = RegressionModels()
regression.train(df)

classification = ClassificationModel()
classification.train(df)

# -------------------------
# Final Report
# -------------------------
report = ReportGenerator()
report.generate(df)

print("Cryogenic Monitoring Pipeline Completed Successfully")
