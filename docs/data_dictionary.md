# Data Dictionary

This file documents the fields used by the notebooks and Streamlit app. The timing column is important because a forecasting model should only use information available at the prediction point.

| Column | Type | Description | Timing / leakage note |
|---|---|---|---|
| `Student_ID` | integer | Unique row identifier | Dropped before modeling |
| `Major_Category` | categorical | Student's broad academic field | Usually known before prediction |
| `Year_of_Study` | categorical | Academic year level | Usually known before prediction |
| `Pre_Semester_GPA` | numeric | GPA before the semester | Known before prediction; dominant predictor |
| `Weekly_GenAI_Hours` | numeric | Weekly hours using GenAI tools | Should be measured before or during the prediction window |
| `Primary_Use_Case` | categorical | Main purpose for GenAI use | Should be measured before or during the prediction window |
| `Prompt_Engineering_Skill` | categorical | Self-reported prompting skill | Should be measured before or during the prediction window |
| `Tool_Diversity` | integer | Number of different GenAI tools used | Training range: 1-5 |
| `Paid_Subscription` | boolean | Whether the student uses paid GenAI tools | Usually known before prediction |
| `Traditional_Study_Hours` | numeric | Weekly non-AI study hours | Training range: 1-36 |
| `Perceived_AI_Dependency` | integer | Self-reported dependency on AI, 1-10 | Should be measured before or during the prediction window |
| `Institutional_Policy` | categorical | Campus GenAI policy context | Usually known before prediction |
| `Anxiety_Level_During_Exams` | integer | Self-reported exam anxiety, 1-10 | Timing must match the use case |
| `Skill_Retention_Score` | numeric | Retention score, 10-100 | Potential temporal leakage if measured after the target period |
| `Burnout_Risk_Level` | categorical | Low, Medium, or High burnout risk | Potential temporal leakage if measured after the target period |
| `Post_Semester_GPA` | numeric | GPA after the semester | Target variable; never used as a feature |

## Prediction Timing

The current model uses all fields except `Student_ID` and `Post_Semester_GPA`. For a true early-warning system, confirm that `Skill_Retention_Score`, `Burnout_Risk_Level`, and `Anxiety_Level_During_Exams` are available before the prediction is made. If not, retrain a strict pre-outcome model without those fields and report its metrics separately.
