# Real Estate House Sale Price Prediction Using Machine Learning

**Project implementation report**  
**Course:** YEEAP AI Project Implementation  
**Group:** 23  
**Report date:** October 23, 2026

## Executive summary

This project implements the Group 23 Module 4 proposal as a beginner-friendly Google Colab notebook. The goal is to estimate the expected sale price of a residential property using historical house characteristics and location information. The implementation covers data preparation, exploratory data analysis (EDA), a Linear Regression baseline, comparisons with Random Forest and Gradient Boosting, evaluation using RMSE/MAE/R², residual review, saving the trained model, and end-to-end workflow tests.

The uploaded CSV contains **2,930 rows and 82 columns**. After excluding the target (`SalePrice`) and two identifier fields (`Order` and `PID`), the model uses **79 predictor features**. On a validation subset, Random Forest performed best of the three candidates with RMSE **$20,124.77**, MAE **$14,347.72**, and R² **0.9255**. It was refitted on the full 80% training pool and evaluated once on a separate 586-row test set, obtaining RMSE **$26,285.70**, MAE **$15,516.53**, and R² **0.9138**.

These results are specific to the provided dataset and fixed split. Because the records describe historical sales in Ames, Iowa, this solution should not be treated as a price estimator for Ethiopia or other markets without suitable local data and additional validation. `SalePrice` is expressed in **U.S. dollars (USD)** in the Ames dataset documentation [2]; the proposal's illustrative birr output should therefore not be used for this dataset.

## 1. Problem refinement

### Problem statement

Estimating a reasonable residential house sale price is challenging because prices depend on multiple factors, including neighborhood, overall quality, living area, lot area, year built, number of bedrooms and bathrooms, basement characteristics, and garage capacity. Manual analysis can be time-consuming and may not consistently account for relationships among many features.

The project builds a supervised regression model to estimate a house's expected sale price from its recorded characteristics. The intended output supports preliminary comparison, pricing discussions, and human review; it is not a guaranteed sale price or legal valuation.

### Target users

The target users in the Group 23 proposal are real estate agents, property sellers, property buyers, real estate companies, property investors, and lenders performing preliminary property-related analysis. The data/ML team develops, evaluates, and maintains the model.

### Inputs, output, objective

- **Inputs:** property attributes recorded in the supplied dataset, including location/neighborhood and physical characteristics.
- **Output:** predicted `SalePrice` in USD.
- **Objective:** determine whether machine learning provides useful and measurable predictive performance on unseen records from the same data source.

## 2. AI solution design

The target is continuous numerical price, so the task is regression. Three algorithms were compared:

- **Linear Regression (baseline):** a simple reference model that provides a transparent benchmark.
- **Random Forest Regressor:** an ensemble of decision trees able to model nonlinear relationships and feature interactions.
- **Gradient Boosting Regressor:** sequentially builds shallow trees to reduce residual error.

Candidate selection was based on the lowest RMSE on a dedicated validation set. The held-out test set was kept separate from model choice, then used once for the final evaluation. The implementation is in Python using pandas, NumPy, Matplotlib, scikit-learn, and joblib.

## 3. Data preparation

### Dataset summary

| Item | Observed value |
|---|---|
| File | `ames-housing.csv` |
| Rows | 2,930 |
| Original columns | 82 |
| Target | `SalePrice` |
| Missing target values | 0 |
| Exact duplicate rows | 0 |
| Numeric predictor columns | 36 |
| Categorical/text predictor columns | 43 |
| Predictor count after excluding `Order` and `PID` | 79 |
| Geographic/time scope | Historical Ames, Iowa, USA home sales |

The raw file's 82 columns include `SalePrice` and two identifiers. `Order` and `PID` were removed from the feature matrix because they identify records/parcels rather than representing normal house characteristics for general prediction.

### Missing data and preprocessing

The dataset includes substantial missingness in several property features. For example, `Pool.QC` has 2,917 missing values, `Misc.Feature` 2,824, `Alley` 2,732, `Fence` 2,358, `Mas.Vnr.Type` 1,775, and `Fireplace.Qu` 1,422. This likely reflects optional features absent from many properties, but the model does not assume every missing value has the same cause.

The preprocessing pipeline performs these operations:

1. Numeric missing values are imputed with the median learned from training data.
2. Missing categorical/text values are filled with a distinct `Missing` label.
3. Categorical features are one-hot encoded. `handle_unknown='ignore'` supports new category labels during prediction.
4. Numeric fields are standardized.
5. Preprocessing is encapsulated in a scikit-learn `Pipeline`, so the same transformations are applied when training and predicting.

No price outliers were removed automatically; potentially genuine high-value homes are included and reviewed through residual analysis.

### Split strategy

A fixed random seed of 42 was used. First, 80% of the data was placed in the training pool and 20% held out for the final test (2,344 training-pool rows and 586 test rows). The training pool was split again into model-training and validation sets, creating approximately 64%/16%/20% train/validation/test proportions overall. Model selection used validation results only.

## 4. Exploratory data analysis

The target sale prices have a mean of **$180,796.06**, median of **$160,000**, minimum of **$12,789**, maximum of **$755,000**, and positive skewness of approximately **1.74**. The long right tail indicates a smaller group of much more expensive houses; such records can contribute disproportionately to RMSE.

The strongest numeric correlations with sale price in the supplied data include:

| Feature | Correlation with SalePrice |
|---|---:|
| `Overall.Qual` | 0.7993 |
| `Gr.Liv.Area` | 0.7068 |
| `Garage.Cars` | 0.6479 |
| `Garage.Area` | 0.6404 |
| `Total.Bsmt.SF` | 0.6323 |
| `X1st.Flr.SF` | 0.6217 |

These are pairwise Pearson correlations for numeric features. They indicate association, not causation, and do not capture all categorical or nonlinear effects.

## 5. Baseline model

Linear Regression was trained first and evaluated on the validation subset. It provided a benchmark for later models. Validation RMSE was **$20,862.58**, validation MAE was **$15,485.94**, and validation R² was **0.9200**.

## 6. Model improvement and comparison

The notebook compared the baseline against Random Forest and Gradient Boosting with reproducible starting parameters. Results were sorted by validation RMSE.

| Model | Validation RMSE (USD) | Validation MAE (USD) | Validation R² |
|---|---:|---:|---:|
| Random Forest | $20,124.77 | $14,347.72 | 0.9255 |
| Linear Regression | $20,862.58 | $15,485.94 | 0.9200 |
| Gradient Boosting | $20,971.00 | $15,241.81 | 0.9192 |

Random Forest was selected because its validation RMSE was lowest. Relative to the Linear Regression baseline, it reduced validation RMSE by approximately **3.5%** and validation MAE by approximately **7.3%**. This is an improvement on this particular validation split, not proof that Random Forest is always better or that it will transfer to other markets.

## 7. Final evaluation

After model selection, Random Forest was refitted using the complete 80% training pool. It was evaluated on the untouched 20% test set of 586 records.

| Test metric | Measured result | Interpretation |
|---|---:|---|
| RMSE | $26,285.70 | Penalizes larger prediction errors more strongly; errors are on the order of tens of thousands of dollars. |
| MAE | $15,516.53 | Mean absolute difference between predictions and actual sale prices. |
| R² | 0.9138 | The predictions explain about 91.4% of the test-set variation relative to a mean-only reference. |

The test RMSE is higher than the validation RMSE. This highlights why final evaluation must use a held-out test set: model performance can differ by sample composition and split. The metrics are useful evidence for a course prototype but are insufficient to promise a price for an individual property.

The notebook also generates actual-versus-predicted and residual plots and reports mean residual, median absolute error, 90th percentile absolute error, and maximum absolute error. Those views help identify whether errors are concentrated among high-priced or unusual properties.

## 8. Complete workflow tests

The input-to-output prediction function uses the fitted end-to-end pipeline and applies basic input validation. The notebook completed the following tests:

| Test case | Expected behavior | Outcome |
|---|---|---|
| Complete held-out property | Accept known feature schema and return a finite positive estimate | PASS |
| Partial property details | Impute omitted features and return a finite positive estimate | PASS |
| Unseen neighborhood category | Handle unseen categorical label without crashing | PASS |
| Negative lot area | Reject invalid negative measurement | PASS |

For the sample run, the partial input case (NAmes neighborhood, 1,500 sq ft living area, 8,000 sq ft lot, quality 6, year built 1990, three bedrooms, two full bathrooms, and two-car garage) produced an estimate of approximately **$171,625 USD**. This is an example output from the trained model, not a market quotation.

The notebook saves a serialized model bundle (`ames_housing_model.joblib`) and writes test results, validation metrics, sample predictions, and plots into `project_outputs/`.

## 9. Limitations and responsible use

1. **Geographic representativeness:** this data represents Ames, Iowa, and is not representative by default of Ethiopian or other housing markets.
2. **Historical data:** recorded sales are from earlier years; current economic conditions and market prices can differ.
3. **Prediction error:** even a strong aggregate R² does not guarantee accuracy for an individual property. Unusual property combinations and high-priced homes may have larger errors.
4. **Data limitations:** missing fields are imputed; imputations may hide meaningful differences in data collection or property characteristics.
5. **Evaluation scope:** one fixed validation/test split is suitable for a prototype. Repeated cross-validation, external validation, and further hyperparameter tuning would provide stronger evidence.
6. **Bias and fairness:** error patterns should be checked across neighborhoods and property groups. Historical data may reproduce historical market patterns.
7. **Transparency:** the system should explain that results are estimates and should encourage review by local professionals.
8. **Currency:** values should remain labeled USD when using this dataset. They must not be labeled birr without an explicitly defined and validated currency-conversion method, and currency conversion alone would not make the model suitable for Ethiopia.

The project is a decision-support prototype and does not provide legal appraisal, investment advice, mortgage approval, or guaranteed selling prices.

## 10. Conclusion and future work

The notebook implements the requested eight-stage workflow. Random Forest was the best of the three evaluated algorithms by validation RMSE and reached a test R² of 0.9138 on the supplied split. The system can load a record or partial input, apply consistent preprocessing, generate a price estimate, and reject selected invalid inputs.

Recommended next steps are: repeat model evaluation with cross-validation; tune model hyperparameters in a controlled way; examine error by neighborhood and sale-price band; add uncertainty intervals and model explanations; validate on current, locally representative data before real-world use; and then build a secured web interface/API if Module 6 requires deployment.

## Group members and contributions

The Module 4 proposal lists six original members and assigns technical roles using generic Member 1–5 labels.The technical-role mapping is proposed and must be checked by the group against actual participation; update it if responsibilities differ and remove anyone who did not contribute. The proposal names the group leader as Dereje Zerfie, while the roster gives Dereje Zerfie Tadesse.

| Member | Contribution / responsibility |
|---|---|
| Tamirat Aboye Demeke | Problem/domain research: define the problem, target users, objectives, stakeholder needs, and project scope. |
| Behailu Feleke Tabor | Data preparation: inspect the CSV and schema, check data quality and duplicates, and review missing-value handling and preprocessing. |
| Dereje Zerfie Tadesse | Model development/evaluation and coordination: establish the Linear Regression baseline; compare Random Forest and Gradient Boosting using RMSE, MAE, and R². |
| Bekele Molla | Prototype workflow: review prediction inputs, validation, model-to-interface integration, and the user demonstration. |
| Addisu Melkie Tafere  | Testing/reproducibility: test complete, partial, unseen-category, and invalid inputs; support model save/load and setup instructions. |
| Beamlak Tessema | Documentation/presentation: review the report, results, charts, limitations, responsible use, and group presentation/demo. |
| Yoseph Tesfaye Tafesse| GitHub and deployment documentation: organize the repository structure, document browser-based GitHub publishing, describe Streamlit Community Cloud deployment, and record post-deployment verification steps. |

## References

1. Group 23. *Real Estate House Sale Price Prediction Using Machine Learning*. YEEAP AI Project Proposal, Module 4, submitted September 30, 2026. Uploaded proposal PDF.
2. CMU Statistics & Data Science Data Repository. *House prices in Ames, Iowa*. https://cmustatistics.github.io/data-repository/money/ames-housing.html
3. Kaggle. *House Prices: Advanced Regression Techniques*. https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques
4. Scikit-learn documentation. https://scikit-learn.org/stable/
