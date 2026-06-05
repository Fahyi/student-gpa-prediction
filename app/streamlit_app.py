import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Student Academic Performance Analytics",
    layout="centered"
)

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "student_gpa_prediction_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

st.title("Prediksi IPK Akhir Semester")
st.write(
    "Isi formulir di bawah sesuai kondisi kamu saat ini. "
    "Sistem akan memperkirakan IPK kamu di akhir semester."
)
st.caption(
    "Catatan: model paling akurat ketika semua input tersedia sebelum prediksi dibuat. "
    "Jika skor retensi atau burnout baru diketahui di akhir semester, gunakan hasil ini "
    "sebagai diagnostic review, bukan early-warning forecast."
)

st.divider()

major_category = st.selectbox(
    "Bidang studi kamu",
    ["Arts", "Business", "Humanities", "Medical", "STEM"]
)

year_of_study = st.selectbox(
    "Tahun perkuliahan saat ini",
    ["Freshman", "Sophomore", "Junior", "Senior", "Graduate"]
)

pre_semester_gpa = st.number_input(
    "IPK semester sebelumnya",
    min_value=0.0,
    max_value=4.0,
    value=3.20,
    step=0.01
)

weekly_genai_hours = st.number_input(
    "Jam per minggu menggunakan AI generatif (ChatGPT, Gemini, dll)",
    min_value=0.0,
    max_value=40.0,
    value=5.0,
    step=0.5
)

primary_use_case = st.selectbox(
    "Kegunaan utama AI generatif dalam kuliah",
    [
        "Copywriting/Drafting",
        "Debugging/Troubleshooting",
        "Direct_Answer_Generation",
        "Ideation",
        "Summarizing_Reading",
    ],
    format_func=lambda value: value.replace("_", " ")
)

prompt_engineering_skill = st.selectbox(
    "Kemampuan kamu dalam menulis prompt ke AI",
    ["Beginner", "Intermediate", "Advanced"]
)

tool_diversity = st.number_input(
    "Jumlah tools AI berbeda yang kamu gunakan",
    min_value=1,
    max_value=5,
    value=3,
    step=1
)

paid_subscription = st.selectbox(
    "Apakah kamu berlangganan versi berbayar tools AI?",
    [True, False]
)

traditional_study_hours = st.number_input(
    "Jam per minggu belajar mandiri (tanpa AI)",
    min_value=1.0,
    max_value=36.0,
    value=12.0,
    step=0.5
)

perceived_ai_dependency = st.slider(
    "Seberapa bergantung kamu pada AI untuk tugas kuliah? (1 = tidak sama sekali, 10 = sangat bergantung)",
    min_value=1,
    max_value=10,
    value=5
)

institutional_policy = st.selectbox(
    "Kebijakan kampus soal penggunaan AI generatif",
    ["Actively_Encouraged", "Allowed_With_Citation", "Strict_Ban"],
    format_func=lambda value: value.replace("_", " ")
)

anxiety_level = st.slider(
    "Seberapa cemas kamu saat menghadapi ujian? (1 = sangat tenang, 10 = sangat cemas)",
    min_value=1,
    max_value=10,
    value=5
)

skill_retention_score = st.number_input(
    "Seberapa baik kamu mempertahankan pemahaman materi setelah belajar (10-100)",
    min_value=10.0,
    max_value=100.0,
    value=75.0,
    step=0.5
)

burnout_risk_level = st.selectbox(
    "Tingkat kelelahan (burnout) kamu saat ini",
    ["Low", "Medium", "High"]
)

input_data = pd.DataFrame({
    "Major_Category": [major_category],
    "Year_of_Study": [year_of_study],
    "Pre_Semester_GPA": [pre_semester_gpa],
    "Weekly_GenAI_Hours": [weekly_genai_hours],
    "Primary_Use_Case": [primary_use_case],
    "Prompt_Engineering_Skill": [prompt_engineering_skill],
    "Tool_Diversity": [tool_diversity],
    "Paid_Subscription": [paid_subscription],
    "Traditional_Study_Hours": [traditional_study_hours],
    "Perceived_AI_Dependency": [perceived_ai_dependency],
    "Institutional_Policy": [institutional_policy],
    "Anxiety_Level_During_Exams": [anxiety_level],
    "Skill_Retention_Score": [skill_retention_score],
    "Burnout_Risk_Level": [burnout_risk_level]
})

st.divider()

if st.button("Lihat Prediksi IPK"):
    prediction = model.predict(input_data)[0]

    # Keep prediction within GPA scale
    prediction = max(0, min(4, prediction))

    st.success(f"Prediksi IPK Akhir Semester: {prediction:.2f}")

    st.caption(
        "Catatan: Hasil ini adalah perkiraan berdasarkan model statistik, "
        "bukan jaminan nilai akhir. Gunakan sebagai bahan evaluasi diri."
    )
