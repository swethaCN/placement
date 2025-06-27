# app.py
import streamlit as st
import pandas as pd
from database import PlacementDatabase

st.set_page_config(layout="wide")
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>PLACEMENT ELIGIBILITY DASHBOARD</h1>
""", unsafe_allow_html=True)

# Initialize DB
if 'db' not in st.session_state:
    st.session_state.db = PlacementDatabase()

db = st.session_state.db


insight_options = {
    "Top 5 Students Ready For Placement": {
        "func": db.get_top_5_placement_ready,
        "columns": ["Name", "Company Name", "Placement Package", "Mock Score"]
    },
    "Average Programming Performance Per Batch": {
        "func": db.average_programming_per_batch,
        "columns": ["Batch", "Avg Problems", "Avg Assessments", "Avg Project Score"]
    },
    "Students With High Mock Interview Scores (>80)": {
        "func": db.students_with_high_mock_scores,
        "columns": ["Name", "Mock Interview Score"]
    },
    "Students With At Least 2 Internships": {
        "func": db.students_with_min_internships,
        "columns": ["Name", "Internships Completed"]
    },
    "Students Placed In Infosys": {
        "func": lambda: db.students_placed_in_company("Infosys"),
        "columns": ["Name", "Company Name", "Placement Package"]
    },
    "Students With Strong Soft Skills (>75)": {
        "func": db.students_with_strong_soft_skills,
        "columns": ["Name", "Communication", "Teamwork", "Leadership"]
    },
    "Students Ready But Not Yet Placed": {
        "func": db.students_ready_but_not_placed,
        "columns": ["Name", "Placement Status"]
    },
    "Strong Programmers (200+ Problems & 2+ Certs)": {
        "func": db.strong_programmers,
        "columns": ["Name", "Problems Solved", "Certifications Earned"]
    },
    "Placed Students Who Cleared >3 Interviews": {
        "func": db.students_cleared_multiple_interviews,
        "columns": ["Name", "Interview Rounds", "Company Name"]
    },
    "Graduating in 2025 But Not Placed": {
        "func": lambda: db.graduating_unplaced_students(2025),
        "columns": ["Name", "Graduation Year", "Placement Status"]
    },
    "Students With Many Mini Projects (>=3)": {
        "func": db.students_with_many_projects,
        "columns": ["Name", "Mini Projects"]
    },
    "Hyderabad Students With High Mock Score (>=85)": {
        "func": lambda: db.students_from_city_with_high_score("Hyderabad", 85),
        "columns": ["Name", "City", "Mock Interview Score"]
    },
    "Top 5 Certified Students": {
        "func": db.top_certified_students,
        "columns": ["Name", "Certifications Earned"]
    }
}

selected_insight = st.selectbox("Select Criteria", list(insight_options.keys()), key="insight_select")

if st.button("Show Result"):
    insight = insight_options[selected_insight]
    result = insight["func"]()
    st.markdown(f"#### Result: {selected_insight}")
    if result:
        df_result = pd.DataFrame(result, columns=insight["columns"])
        df_result.index += 1
        st.dataframe(df_result.reset_index(drop=False).rename(columns={'index': 'S.No'}), use_container_width=True)
    else:
        st.warning("No results found for this query.")
