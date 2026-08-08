import sys
import os
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocessing import Preprocessor


def test_clean_data_removes_duplicates():
    processor = Preprocessor()
    df = pd.DataFrame({"a": [1, 1, 2], "b": [1, 1, 2]})
    result = processor.clean_data(df)
    assert len(result) == 2


def test_clean_data_fills_missing():
    processor = Preprocessor()
    df = pd.DataFrame({"a": [1, None, 3]})
    result = processor.clean_data(df)
    assert result["a"].isnull().sum() == 0


def test_create_features():
    processor = Preprocessor()
    df = pd.DataFrame({
        "temperature_k": [1.0, 2.0, 3.0],
        "still_pressure": [1.0, 1.5, 2.0],
        "water_cooling_inlet": [290, 290, 290],
        "water_cooling_outlet": [292, 292, 292],
    })
    result = processor.create_features(df)
    assert "temperature_change" in result.columns
    assert "pressure_change" in result.columns
    assert "cooling_difference" in result.columns
    assert result["cooling_difference"].iloc[0] == 2


def test_normalize():
    processor = Preprocessor()
    df = pd.DataFrame({"a": [0, 5, 10]})
    result = processor.normalize(df)
    assert result["a"].min() == 0
    assert result["a"].max() == 1
