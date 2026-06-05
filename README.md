# Student Academic Performance Analytics

This project analyzes a 50,000-row student dataset to estimate post-semester GPA and understand whether GenAI usage, study behavior, and academic background add useful signal for academic performance prediction.

The main result is deliberately conservative: prior GPA is by far the strongest predictor. GenAI usage and behavioral variables show only limited independent predictive power once prior academic performance is included.

## Quick Access

- **Live Demo:** [Open Streamlit App](https://fahyi-student-gpa-prediction-appstreamlit-app-wzxesj.streamlit.app/)
- **GitHub Repository:** [View Repository](https://github.com/Fahyi/student-gpa-prediction)
- **EDA Notebook:** [Open EDA Notebook](https://colab.research.google.com/drive/1oNbI6LXfpq-9potzOHDNQZsrkQWdd8Bm)
- **Modeling Notebook:** [Open Modeling Notebook](https://colab.research.google.com/drive/1Et4MUcxHlm4p5U7IjaihO_2uRyZBANhQ)

## Project Question

Can student academic performance be estimated from prior GPA, GenAI usage behavior, study habits, and self-reported academic factors?

The project is framed as an academic advising use case, not as an automated decision system. The model can support discussion and diagnostic review, but it should not be used as the sole basis for intervention.

## Repository Structure

```text
app/
  streamlit_app.py                  # Streamlit demo for GPA estimation
data/
  ai_student_impact_dataset.csv      # Input dataset
docs/
  data_dictionary.md                 # Feature definitions and timing caveats
  experiment_comparison.csv          # Best model comparison by experiment
  model_results_with_pre_gpa.csv     # Model results with prior GPA
  model_results_without_pre_gpa.csv  # Model results without prior GPA
models/
  student_gpa_prediction_model.pkl   # Serialized scikit-learn pipeline
notebooks/
  01_eda.ipynb                       # Exploratory data analysis
  02_modeling.ipynb                  # Modeling, evaluation, and export
```

Use `01_eda.ipynb` and `02_modeling.ipynb` as the publish-ready analysis path.

## Dataset Snapshot

- Rows: 50,000
- Columns: 16
- Target: `Post_Semester_GPA`
- Missing values: 0
- Duplicate rows: 0
- Duplicate `Student_ID`: 0
- GPA range: valid 1.0-4.0 scale in the provided data

The dataset contains student academic background, GenAI usage behavior, study hours, institutional policy context, self-reported anxiety/dependency, skill retention, burnout risk, and post-semester GPA.

## Methodology

The project is split into two modeling experiments:

- Experiment A includes `Pre_Semester_GPA`.
- Experiment B excludes `Pre_Semester_GPA` to test whether GenAI and behavioral variables can predict GPA independently.

Models compared:

- Dummy mean baseline
- Linear Regression
- Ridge Regression
- Random Forest Regressor
- Gradient Boosting Regressor

Evaluation metrics:

- MAE
- RMSE
- R2
- 5-fold cross-validation for the selected model
- Residual and subgroup error analysis
- Tree-based and permutation feature importance

## Key Results

| Experiment | Best model | MAE | RMSE | R2 |
|---|---:|---:|---:|---:|
| With `Pre_Semester_GPA` | Gradient Boosting | 0.114 | 0.144 | 0.914 |
| Without `Pre_Semester_GPA` | Gradient Boosting | 0.389 | 0.474 | 0.070 |

Interpretation:

- Prior GPA explains most of the predictive signal.
- Removing prior GPA causes model performance to collapse.
- GenAI usage features are not strong standalone predictors of post-semester GPA in this dataset.
- The best model only modestly outperforms simpler linear/Ridge models when prior GPA is available, so interpretability should be considered before choosing a more complex model in a real advising workflow.

## Important Caveats

- This is observational analysis. The results do not prove that GenAI usage causes GPA changes.
- `Skill_Retention_Score` and `Burnout_Risk_Level` may be measured during or after the semester. If they are not available before the prediction point, they should be removed for an early-warning version of the model.
- GPA is bounded at 4.0, and many records sit at the upper limit. This ceiling effect can affect residual interpretation.
- The app is a demo for estimation and discussion. It is not a replacement for academic advising judgment.

## Run Locally

Create and activate an environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app/streamlit_app.py
```

To reproduce the analysis, run:

1. `notebooks/01_eda.ipynb`
2. `notebooks/02_modeling.ipynb`

The notebooks are designed to locate the project root from either the repository root or the `notebooks/` directory.

## Portfolio Talking Points

- I separated model performance with and without prior GPA to avoid overstating GenAI's predictive value.
- I used a dummy baseline and multiple regression models before selecting Gradient Boosting.
- I checked whether the model's strong headline performance was mostly driven by historical academic performance.
- I documented temporal leakage risk and app input constraints rather than hiding them.
- The practical takeaway is not "AI improves GPA"; it is "prior GPA dominates prediction, while GenAI behavior adds limited independent signal in this dataset."
