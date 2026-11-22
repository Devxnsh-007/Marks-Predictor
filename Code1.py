import streamlit as st

pg = st.navigation([
    st.Page(
        "home.py",
        title="Home",
        icon="🏠"
    ),
    st.Page(
        "pages/prediction_dashboard.py",
        title="Prediction Dashboard",
        icon="🎯"
    ),
    st.Page(
        "pages/EDA.py",
        title="Exploratory Data Analysis",
        icon="📊"
    ),
    st.Page(
        "pages/Model_Analysis.py",
        title="Model Analysis",
        icon="📈"
    )
])

pg.run()