import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

st.title("🎓 Student Performance Analysis & Prediction")

st.markdown("""
<p style='font-size:22px;'>
An end-to-end Machine Learning application that analyzes student
academic performance, explores important trends through visualizations,
and predicts final scores using multiple regression models.
</p>
""", unsafe_allow_html=True)

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Dataset Size",
        "500"
    )

with col2:
    st.metric(
        "Features Used",
        "8"
    )

with col3:
    st.metric(
        "Models Trained",
        "6"
    )

with col4:
    st.metric(
        "Best R² Score",
        "0.8009"
    )

st.divider()

# Project Overview

st.header("📖 Project Overview")

st.markdown("""
This project aims to predict a student's final academic score using
Machine Learning techniques.

The system analyzes multiple factors including:

- 📚 Study Hours
- 🏫 Attendance Rate
- 📝 Previous Academic Score
- 👨‍👩‍👧 Parent Education Level
- 🌐 Internet Access
- 🎯 Extracurricular Activities
- 👤 Gender
- 🎂 Age

The application provides:
- Student Score Prediction
- Exploratory Data Analysis (EDA)
- Model Performance Comparison
- Feature Importance Analysis
""")

st.divider()

# Workflow

st.header("⚙️ Project Workflow")

st.markdown("""
```text
Dataset Collection\n
        ↓\n
Data Preprocessing\n
        ↓\n
Exploratory Data Analysis\n
        ↓\n
Feature Engineering\n
        ↓\n
Model Training\n
        ↓\n
Model Evaluation\n
        ↓\n
Prediction Dashboard\n
            """)
st.divider()
st.header("🤖 Machine Learning Models")
col1, col2 = st.columns(2)
with col1:
    st.info("""
        📈 Linear Regression\n
        Best Performing Model
        R² Score = 0.8009
    """)
    st.info("""
        📉 Polynomial Regression\n
        Captures nonlinear relationships.
        """)

    st.info("""
        🧠 MLP Regressor\n
        Neural Network based model.
        """)
with col2:
    st.info("""
        🌳 Random Forest\n
        Ensemble learning approach.
    """)
    st.info("""
        ⚡ XGBoost\n
        Gradient boosting model.
    """)

    st.info("""
        🌲 Decision Tree\n
        Tree based regression model.
    """)
st.divider()
st.header("🏆 Best Model")
st.success("""
Linear Regression achieved the highest performance among all trained models.
R² Score : 0.8009
RMSE : 7.15
""")
st.divider()
st.header("🧭 Navigation Guide")
st.markdown("""
Use the sidebar menu to explore:\n
🎯 Prediction Dashboard\n
📊 Exploratory Data Analysis\n
📈 Model Analysis\n
Each section provides unique insights into student performance and model behavior.
""")
st.divider()
