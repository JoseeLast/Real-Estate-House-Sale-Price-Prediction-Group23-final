"""Streamlit UI for the Group 23 Ames house price prediction prototype.

Run with: streamlit run app.py
"""
from pathlib import Path
import pandas as pd
import streamlit as st
from predictor import load_model_bundle, predict_from_bundle

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "ames_housing_model.joblib"
DATA_PATH = ROOT / "ames-housing.csv"

st.set_page_config(page_title="Ames House Price Estimator", page_icon="🏠", layout="centered")

@st.cache_resource
def get_bundle():
    return load_model_bundle(MODEL_PATH)

@st.cache_data
def get_data_summary():
    if not DATA_PATH.exists():
        raise FileNotFoundError("ames-housing.csv is required beside app.py for data-range checks and neighborhood choices.")
    data = pd.read_csv(DATA_PATH)
    return {
        "neighborhoods": sorted(data["Neighborhood"].dropna().astype(str).unique().tolist()),
        "built_min": int(data["Year.Built"].dropna().min()),
        "built_max": int(data["Year.Built"].dropna().max()),
        "remod_min": int(data["Year.Remod.Add"].dropna().min()),
        "remod_max": int(data["Year.Remod.Add"].dropna().max()),
        "lot_max": int(max(300000, data["Lot.Area"].dropna().quantile(0.999))),
        "living_max": int(max(10000, data["Gr.Liv.Area"].dropna().quantile(0.999) * 2)),
    }

st.title("🏠 Ames House Sale Price Prediction")
st.caption("YEEAP FUSE AI-201 | Group 23 | Module 6 deployment demonstration")
st.warning(
    "Educational prototype only. The model uses historical Ames, Iowa housing transactions. "
    "It is not a professional appraisal, a guaranteed sale price, or a model validated for Ethiopia or other markets."
)

try:
    bundle = get_bundle()
    summary = get_data_summary()
except Exception as exc:
    st.error(f"Could not load the model or dataset: {exc}")
    st.stop()

st.markdown(
    "Enter the property details below and select **Estimate sale price**. "
    "Fields shown here are only a subset of the model's original features; omitted fields are treated as missing "
    "and processed using the same trained preprocessing pipeline. More complete information may improve usefulness."
)

with st.form("property_form"):
    st.subheader("Property details")
    neighborhoods = summary["neighborhoods"]
    default_neighborhood = "NAmes" if "NAmes" in neighborhoods else neighborhoods[0]
    neighborhood = st.selectbox("Neighborhood", neighborhoods, index=neighborhoods.index(default_neighborhood))
    c1, c2 = st.columns(2)
    with c1:
        quality = st.slider("Overall quality (1–10)", 1, 10, 6)
        overall_cond = st.slider("Overall condition (1–9)", 1, 9, 5)
        living_area = st.number_input("Above-ground living area (sq ft)", min_value=1, max_value=summary["living_max"], value=1500, step=50)
        lot_area = st.number_input("Lot area (sq ft)", min_value=1, max_value=summary["lot_max"], value=8000, step=100)
        year_built = st.number_input("Year built", min_value=summary["built_min"], max_value=summary["built_max"], value=min(1990, summary["built_max"]), step=1)
    with c2:
        bedrooms = st.number_input("Bedrooms above ground", min_value=0, max_value=20, value=3, step=1)
        bathrooms = st.number_input("Full bathrooms", min_value=0, max_value=10, value=2, step=1)
        garage_cars = st.number_input("Garage capacity (cars)", min_value=0, max_value=10, value=2, step=1)
        basement_area = st.number_input("Total basement area (sq ft)", min_value=0, max_value=20000, value=900, step=50)
        remod_default = max(int(year_built), min(1990, summary["remod_max"]))
        remod_year = st.number_input("Year remodeled", min_value=summary["remod_min"], max_value=summary["remod_max"], value=min(max(remod_default, summary["remod_min"]), summary["remod_max"]), step=1)
    submitted = st.form_submit_button("Estimate sale price", type="primary", use_container_width=True)

if submitted:
    if remod_year < year_built:
        st.error("Year remodeled cannot be earlier than the year built. Please correct the dates.")
    else:
        details = {
            "Neighborhood": neighborhood,
            "Overall.Qual": int(quality),
            "Overall.Cond": int(overall_cond),
            "Gr.Liv.Area": float(living_area),
            "Lot.Area": float(lot_area),
            "Year.Built": int(year_built),
            "Year.Remod.Add": int(remod_year),
            "Bedroom.AbvGr": int(bedrooms),
            "Full.Bath": int(bathrooms),
            "Garage.Cars": int(garage_cars),
            "Total.Bsmt.SF": float(basement_area),
        }
        try:
            price = predict_from_bundle(details, bundle)
            st.success("Prediction completed")
            st.metric("Estimated sale price (USD)", f"${price:,.0f}")
            st.caption("This value is a model estimate based on historical data, not a quotation or certified valuation.")
            with st.expander("View inputs used"):
                st.json(details)
        except (TypeError, ValueError) as exc:
            st.error(f"Input validation failed: {exc}")
        except Exception as exc:
            st.error(f"Prediction failed. Record the issue and contact the project support owner. Details: {exc}")

with st.expander("Model information and evaluation"):
    st.write(f"**Selected model:** {bundle.get('selected_model', 'Unknown')}")
    metrics = bundle.get("final_test_metrics", {})
    if metrics:
        m1, m2, m3 = st.columns(3)
        m1.metric("Test RMSE", f"${metrics.get('RMSE (USD)', float('nan')):,.0f}")
        m2.metric("Test MAE", f"${metrics.get('MAE (USD)', float('nan')):,.0f}")
        m3.metric("Test R²", f"{metrics.get('R2', float('nan')):.4f}")
    st.write("The held-out test metrics are from the supplied Ames dataset and the saved Module 5 experiment. They do not establish future or cross-market performance.")

st.divider()
st.caption("Data statement: The project uses a public historical Ames, Iowa housing dataset with recorded sale prices. The dataset is not synthetic. Manually entered values in this form are demonstration inputs, and the displayed output is a prediction, not a real transaction.")
