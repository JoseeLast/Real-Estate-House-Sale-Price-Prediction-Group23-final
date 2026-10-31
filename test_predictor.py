import pytest
from pathlib import Path
from predictor import load_model_bundle, predict_from_bundle

ROOT = Path(__file__).resolve().parent

@pytest.fixture(scope="module")
def bundle():
    return load_model_bundle(ROOT / "ames_housing_model.joblib")


def sample_details():
    return {
        "Neighborhood": "NAmes",
        "Gr.Liv.Area": 1500,
        "Lot.Area": 8000,
        "Overall.Qual": 6,
        "Overall.Cond": 5,
        "Year.Built": 1990,
        "Year.Remod.Add": 1990,
        "Bedroom.AbvGr": 3,
        "Full.Bath": 2,
        "Garage.Cars": 2,
        "Total.Bsmt.SF": 900,
    }


def test_valid_partial_input_returns_positive_finite_price(bundle):
    result = predict_from_bundle(sample_details(), bundle)
    assert result > 0
    assert result < float("inf")


def test_negative_lot_area_rejected(bundle):
    with pytest.raises(ValueError, match="cannot be negative"):
        predict_from_bundle({"Lot.Area": -500}, bundle)


def test_unknown_feature_rejected(bundle):
    with pytest.raises(ValueError, match="Unknown feature"):
        predict_from_bundle({"This.Is.Not.A.Feature": 2}, bundle)


def test_invalid_year_rejected(bundle):
    with pytest.raises(ValueError, match="between 1800 and 2100"):
        predict_from_bundle({"Year.Built": 1700}, bundle)


def test_unseen_category_is_handled(bundle):
    details = sample_details()
    details["Neighborhood"] = "NotInTrainingSet"
    result = predict_from_bundle(details, bundle)
    assert result > 0
