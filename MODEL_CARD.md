# Model Card — Ames House Sale Price Prediction

## Model details
- **Project:** YEEAP Group 23, FUSE AI-201 Module 6
- **Model family:** Random Forest regression with a scikit-learn preprocessing pipeline
- **Task:** Estimate historical residential sale price from structured house characteristics
- **Artifact:** `ames_housing_model.joblib`
- **Selection method:** Lowest validation RMSE among Linear Regression, Random Forest, and Gradient Boosting in the recorded experiment

## Data
The supplied Ames Housing CSV contains historical residential transactions from Ames, Iowa, USA. The target is `SalePrice`. The project does not use synthetic training data. Inputs typed in the demo app are illustrative user-provided values and are not verified market transactions.

## Recorded evaluation

| Test metric | Recorded value |
|---|---:|
| RMSE | $26,285.70 |
| MAE | $15,516.53 |
| R² | 0.9138 |

These metrics apply only to the recorded held-out split from this historical dataset. They are not guarantees about future cases, current values, or other geographic markets.

## Intended use
Educational demonstration and preliminary decision support for learning about regression, evaluation, user input validation, and deployment planning.

## Out-of-scope use
- Certified property valuation or appraisal
- Mortgage, credit, legal, or investment decisions
- Pricing properties in Ethiopia or any unsupported market
- Claims about current real estate market value without relevant new validation

## Limitations and risks
- Single-market geographic coverage (Ames, Iowa)
- Historical data may not reflect current economic conditions
- Some values are missing and handled by trained preprocessing
- The simplified web form omits some original dataset fields; missing values are imputed by the pipeline
- Prediction errors may be larger for unusual properties or cases underrepresented in training
- The prototype has no continuous production monitoring, retraining pipeline, model explanation UI, or prediction intervals

## Monitoring and maintenance recommendations
Track prediction errors when verified outcomes become available; monitor input distributions, invalid-input rates, response time, and unusually high/low predictions; document incidents; test changes before release; review dependencies; and retrain only after data quality, validation results, and approval criteria are reviewed.

## Group information

The Module 4 proposal lists six original members and assigns technical roles using generic Member 1–5 labels. Addisu Melkie Tafere is included in the updated Module 6 group information supplied for this submission, with a focus on GitHub repository and deployment documentation. The technical-role mapping is proposed and must be checked by the group against actual participation; update it if responsibilities differ and remove anyone who did not contribute. The proposal names the group leader as Dereje Zerfie, while the roster gives Dereje Zerfie Tadesse.

| Member | Contribution / responsibility |
|---|---|
| Tamirat Aboye Demeke | Problem/domain research: define the problem, target users, objectives, stakeholder needs, and project scope. |
| Behailu Feleke Tabor | Data preparation: inspect the CSV and schema, check data quality and duplicates, and review missing-value handling and preprocessing. |
| Dereje Zerfie Tadesse | Model development/evaluation and coordination: establish the Linear Regression baseline; compare Random Forest and Gradient Boosting using RMSE, MAE, and R². |
| Bekele Molla | Prototype workflow: review prediction inputs, validation, model-to-interface integration, and the user demonstration. |
| Addisu Melkie Tafere | Testing/reproducibility: test complete, partial, unseen-category, and invalid inputs; support model save/load and setup instructions. |
| Beamlak Tessema | Documentation/presentation: review the report, results, charts, limitations, responsible use, and group presentation/demo. |
| Yoseph Tesfaye Tafesse | GitHub and deployment documentation: organize the repository structure, document browser-based GitHub publishing, describe Streamlit Community Cloud deployment, and record post-deployment verification steps. |
