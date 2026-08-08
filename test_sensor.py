import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.sensor import NoiseThermometer


def test_get_temperature():
    sensor = NoiseThermometer("2026-01-01T00:00:00", 0.0150)
    assert sensor.get_temperature() == 0.0150


def test_detect_status_normal():
    sensor = NoiseThermometer("2026-01-01T00:00:00", 0.0150)
    assert sensor.detect_status() == "Normal"


def test_detect_status_warning():
    sensor = NoiseThermometer("2026-01-01T00:00:00", 0.0153)
    assert sensor.detect_status() == "Warning"


def test_detect_status_spike():
    sensor = NoiseThermometer("2026-01-01T00:00:00", 0.0158)
    assert sensor.detect_status() == "Spike"


def test_detect_status_critical():
    sensor = NoiseThermometer("2026-01-01T00:00:00", 0.0165)
    assert sensor.detect_status() == "Critical"
