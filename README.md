# Real Estate House Sale Price Prediction — YEEAP Group 23

**Course:** FUSE AI-201: AI Model Development and Implementation  
**Assignment:** Module 6 — AI Deployment, Monitoring, Support & Maintenance  
**Project type:** Regression / educational prototype  
**Dataset:** Historical Ames Housing transactions, Ames, Iowa, USA

This repository continues the Group 23 project proposed in Module 4 and implemented in Module 5. It includes a saved model, a Streamlit prediction interface, a Colab notebook, experiment logs, testing evidence, and Module 6 documentation.

> **Responsible-use notice:** The model predicts a historical Ames-market price in US dollars. It is not a certified appraisal, guaranteed sale price, investment recommendation, or model validated for Ethiopia or other housing markets.

## Quick start

### 1. Requirements
- Python 3.11 recommended
- Internet connection for installing Python packages the first time

### 2. Install dependencies

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

macOS/Linux:

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Run the Streamlit prototype

```bash
streamlit run app.py
```

Open the local URL printed in the terminal (normally `http://localhost:8501`). Enter property details and choose **Estimate sale price**. The app validates relevant inputs and returns a price estimate in USD.

### 4. Run automated tests

```bash
pytest -q
```

The repository includes a GitHub Actions workflow at `.github/workflows/tests.yml` to run the automated tests on pushes and pull requests. A passing CI check validates the test suite; it does not establish production-grade valuation accuracy.

## Google Colab notebook

Open the notebook in Colab after the repository has been pushed to GitHub. Replace `OWNER` and `REPOSITORY` with the actual GitHub owner and repository name:

`https://colab.research.google.com/github/OWNER/REPOSITORY/blob/main/Real_Estate_House_Sale_Price_Prediction_Colab.ipynb`

Upload `ames-housing.csv` when prompted, if required, then choose **Runtime → Run all**.

## Repository contents

- `app.py` — Streamlit user interface.
- `predictor.py` — model loading, input validation, and prediction logic.
- `test_predictor.py` — automated tests for validation and prediction.
- `ames_housing_model.joblib` — saved preprocessing and Random Forest model bundle.
- `ames-housing.csv` — historical Ames Housing dataset used for model development and interface reference checks.
- `Real_Estate_House_Sale_Price_Prediction_Colab.ipynb` — Module 5 notebook covering all eight implementation tasks.
- `Project_Implementation_Report.docx` and `project_report.md` — prior implementation report.
- `project_outputs/` — model comparison and workflow test results.
- `module6/docs/` — Module 6 report, maintenance plan, data statement, retrospective, and recording script.
- `module6/evidence/` — recorded metrics, validation/testing evidence, plots, sample predictions, and implementation status.
- `module6/experiment_logs/` — CSV/JSON model experiment records.
- `module6/slides/Module6_Capstone_Presentation.pptx` — presentation slides to use while recording the capstone video.
- `PUBLISH_TO_GITHUB.md` — concise GitHub publishing notes.
- `GITHUB_AND_STREAMLIT_DEPLOYMENT_GUIDE.md` — detailed browser-based GitHub and Streamlit Community Cloud deployment walkthrough.
- `GITHUB_AND_STREAMLIT_DEPLOYMENT_GUIDE.docx` — editable Word version of the same guide.
- `GROUP_CONTRIBUTIONS.md` — group roster and proposed responsibilities.
- `MODEL_CARD.md` — model purpose, metrics, intended use, and limitations.

## Model and recorded test results

Random Forest was selected because it achieved the lowest RMSE on the validation split among the tested models. The recorded held-out test metrics are:

| Metric | Test result |
|---|---:|
| RMSE | $26,285.70 |
| MAE | $15,516.53 |
| R² | 0.9138 |

The metrics describe the provided dataset and the saved evaluation split only. See `module6/experiment_logs/` and `module6/evidence/` for experiment and evaluation records. Lightweight CSV/JSON logging is implemented; MLflow is not implemented.

## Data disclosure

The project uses the supplied public historical Ames Housing dataset, not synthetic training data. Values entered manually into the interface are demonstration inputs, not verified new property sales. The dataset represents Ames, Iowa, and does not establish performance for present-day prices or other countries.

## Implementation status and limitations

- Implemented in this repository: saved model pipeline, local Streamlit source, input checks, automated prediction tests, notebook, experiment logs, reports, and deployment/maintenance plan.
- Not claimed as already deployed: no public Streamlit link, active remote GitHub repository, production API, Docker image, MLflow server, or continuous monitoring service is included by default.
- Before public deployment: verify the app in the target environment, review package versions and model compatibility, check data licensing/attribution, and inspect the repository for confidential content.
- Group responsibilities are documented in the report as a proposed mapping; the team must verify that it accurately reflects actual participation.

## Group members and contributions

The Module 4 proposal lists six original members and assigns technical roles using generic Member 1–5 labels. Addisu Melkie Tafere is included in the updated Module 6 group information supplied for this submission, with a focus on GitHub repository and deployment documentation. The technical-role mapping is proposed and must be checked by the group against actual participation; update it if responsibilities differ and remove anyone who did not contribute. The proposal names the group leader as Dereje Zerfie, while the roster gives Dereje Zerfie Tadesse.

| Member | Contribution / responsibility |
|---|---|
| Tamirat Aboye Demeke | Problem/domain research: define the problem, target users, objectives, stakeholder needs, and project scope. |
| Behailu Feleke Tabor | Data preparation: inspect the CSV and schema, check data quality and duplicates, and review missing-value handling and preprocessing. |
| Dereje Zerfie Tadesse | Model development/evaluation and coordination: establish the Linear Regression baseline; compare Random Forest and Gradient Boosting using RMSE, MAE, and R². |
| Bekele Molla | Prototype workflow: review prediction inputs, validation, model-to-interface integration, and the user demonstration. |
| Addisu Melkie Tafere  | Testing/reproducibility: test complete, partial, unseen-category, and invalid inputs; support model save/load and setup instructions. |
| Beamlak Tessema | Documentation/presentation: review the report, results, charts, limitations, responsible use, and group presentation/demo. |
| Yoseph Tesfaye Tafesse | GitHub and deployment documentation: organize the repository structure, document browser-based GitHub publishing, describe Streamlit Community Cloud deployment, and record post-deployment verification steps. |

For the web-based publish and deployment steps, see `GITHUB_AND_STREAMLIT_DEPLOYMENT_GUIDE.md`. The project must be published to the team's GitHub account and deployed to Streamlit Community Cloud before a real public URL can be recorded.
