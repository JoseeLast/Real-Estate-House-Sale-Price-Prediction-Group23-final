"""Prediction and validation helpers for the Ames house-price prototype.

The model is an educational decision-support tool. It is not an appraisal and
has not been validated for markets outside historical Ames, Iowa transactions.
"""
from pathlib import Path
from typing import Mapping, Any
import numpy as np
import pandas as pd
import joblib

DEFAULT_MODEL_PATH = Path(__file__).resolve().parent / "ames_housing_model.joblib"
NON_NEGATIVE_FEATURES = {
    "Lot.Frontage", "Lot.Area", "Mas.Vnr.Area", "BsmtFin.SF.1", "BsmtFin.SF.2",
    "Bsmt.Unf.SF", "Total.Bsmt.SF", "X1st.Flr.SF", "X2nd.Flr.SF", "Low.Qual.Fin.SF",
    "Gr.Liv.Area", "Bsmt.Full.Bath", "Bsmt.Half.Bath", "Full.Bath", "Half.Bath",
    "Bedroom.AbvGr", "Kitchen.AbvGr", "TotRms.AbvGrd", "Fireplaces", "Garage.Cars",
    "Garage.Area", "Wood.Deck.SF", "Open.Porch.SF", "Enclosed.Porch", "X3Ssn.Porch",
    "Screen.Porch", "Pool.Area", "Misc.Val",
}
YEAR_FEATURES = {"Year.Built", "Year.Remod.Add", "Garage.Yr.Blt"}


def load_model_bundle(model_path=DEFAULT_MODEL_PATH):
    """Load the serialized preprocessing + estimator bundle."""
    model_path = Path(model_path)
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found: {model_path}. Keep ames_housing_model.joblib beside app.py."
        )
    bundle = joblib.load(model_path)
    required = {"pipeline", "feature_columns", "selected_model", "final_test_metrics"}
    missing = required - set(bundle)
    if missing:
        raise ValueError(f"Model bundle is missing required keys: {sorted(missing)}")
    return bundle


def predict_from_bundle(property_details: Mapping[str, Any], bundle: dict) -> float:
    """Validate a dictionary of original Ames feature names and return USD estimate.

    Unspecified features become missing and are handled by the preprocessing pipeline
    learned from training data. Unknown field names and invalid non-negative values fail.
    """
    if not isinstance(property_details, Mapping):
        raise TypeError("Property details must be supplied as a mapping of field names to values.")
    feature_columns = list(bundle["feature_columns"])
    unknown = set(property_details) - set(feature_columns)
    if unknown:
        raise ValueError(f"Unknown feature name(s): {sorted(unknown)}")

    for col in NON_NEGATIVE_FEATURES.intersection(feature_columns):
        value = property_details.get(col)
        if value is not None and not pd.isna(value):
            try:
                numeric_value = float(value)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{col} must be numeric.") from exc
            if numeric_value < 0:
                raise ValueError(f"{col} cannot be negative.")

    for col in YEAR_FEATURES.intersection(feature_columns):
        value = property_details.get(col)
        if value is not None and not pd.isna(value):
            try:
                numeric_value = float(value)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{col} must be a year between 1800 and 2100.") from exc
            if not 1800 <= numeric_value <= 2100:
                raise ValueError(f"{col} must be between 1800 and 2100 when supplied.")

    row = {col: np.nan for col in feature_columns}
    row.update({str(k): v for k, v in property_details.items() if v is not None})
    frame = pd.DataFrame([row], columns=feature_columns)
    estimate = float(bundle["pipeline"].predict(frame)[0])
    if not np.isfinite(estimate):
        raise ValueError("The model did not return a finite prediction.")
    if estimate <= 0:
        raise ValueError("The model returned a non-positive price estimate. Review the input details.")
    return estimate


def predict_house_price(property_details, model_path=DEFAULT_MODEL_PATH) -> float:
    """Convenience wrapper: load a model bundle and return an estimate."""
    return predict_from_bundle(property_details, load_model_bundle(model_path))
