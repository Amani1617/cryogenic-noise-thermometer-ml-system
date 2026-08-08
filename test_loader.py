import sys
import os
import pandas as pd
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_loader import DataLoader


REQUIRED_COLUMNS = [
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


def make_valid_df():
    return pd.DataFrame({column: [0] for column in REQUIRED_COLUMNS})


def test_validate_columns_success():
    loader = DataLoader("dummy.csv")
    df = make_valid_df()
    assert loader.validate_columns(df) is True


def test_validate_columns_missing():
    loader = DataLoader("dummy.csv")
    df = make_valid_df().drop(columns=["temperature_k"])
    with pytest.raises(Exception):
        loader.validate_columns(df)


def test_preprocess_datetime():
    loader = DataLoader("dummy.csv")
    df = pd.DataFrame({"datetime": ["2026-01-01 00:00:00"]})
    result = loader.preprocess_datetime(df)
    assert pd.api.types.is_datetime64_any_dtype(result["datetime"])
