# Cryogenic Noise Thermometer Monitoring Pipeline

A small end-to-end pipeline that simulates cryogenic sensor data, cleans and
engineers features from it, detects anomalies, runs regression/classification
models, produces plots, and writes a final automated report.

## Project Structure

```
├── data/
│   ├── cryogenic_data.csv        # generated dataset
│   └── generate_dataset.py       # synthetic data generator
├── results/                      # all pipeline outputs (plots, reports, stats)
├── src/
│   ├── sensor.py                 # Sensor / NoiseThermometer classes
│   ├── data_loader.py            # CSV loading + column validation
│   ├── preprocessing.py          # cleaning, feature engineering, normalization
│   ├── analysis.py               # summary statistics + insights
│   ├── visualization.py          # all plots
│   ├── anomaly_detection.py      # z-score based spike detection
│   ├── machine_learning.py       # regression models (Linear, Random Forest)
│   ├── classification.py         # Random Forest sensor-status classifier
│   └── report_generator.py       # final text report
├── tests/                        # unit tests (pytest)
├── config/
│   └── config.json               # thresholds
├── main.py                       # runs the full pipeline
└── requirements.txt
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

1. Generate the synthetic dataset:

```bash
python data/generate_dataset.py
```

2. Run the pipeline:

```bash
python main.py
```

All outputs (plots, `statistics.json`, `insights.txt`, `regression_results.txt`,
`classification_results.txt`, `final_report.txt`) are written to `results/`.

## Running Tests

```bash
pytest tests/
```

## Notes

- `AnomalyDetector` uses a z-score threshold (default 3) to flag temperature
  spikes, configurable via `config/config.json`.
- `NoiseThermometer.detect_status()` uses fixed temperature bands
  (Normal / Warning / Spike / Critical) instead of z-scores, useful for
  per-sensor status classification independent of the batch statistics.
