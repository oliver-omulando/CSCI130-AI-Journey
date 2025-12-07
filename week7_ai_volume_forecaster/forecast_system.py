# Wrapper module to make Week-7 forecaster importable as a clean package
import os
import sys

# Add original Week-7 folder (with hyphens) to sys.path for runtime import
WEEK7_PATH = os.path.join(os.path.dirname(__file__), '..', 'Week-7-ai-volume-forecaster')
sys.path.insert(0, WEEK7_PATH)

# Re-export the original class
from forecast_system import QuantitativeForecaster  # type: ignore

__all__ = ["QuantitativeForecaster"]
