import streamlit as st
import pandas as pd
from database.db_connection import DatabaseConnection
from src.queries import Queries

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Placement Dashboard", layout="wide")
st.title("🎓 Placement Eligibility Dashboard")

# ---------------- DB ----------------
db = DatabaseConnection()
db.connect()

queries = Queries()

# ---------------- SIDEBAR FORM ----------------
st.sidebar.header("🔍 Filters")

with st.sidebar.form("filter_form"):
    min_problems = st.slider("Min Problems Solved", 0, 300, 50)
    min_communication = st.slider("Min Communication", 0, 100, 60)
    min_interview = st.slider("Min Interview Score", 0, 100, 60)
    min_internships = st.slider("Min Internships", 0, 3, 0)

    batch = st.selectbox("Batch", ["All", "Batch A", "Batch B", "Batch C", "Batch D"])
    status = st.selectbox("Placement Status", ["All", "Ready", "Not Ready", "Placed"])

    submit = st.form_submit_button("Apply Filters")

# ---------------- FILTER FUNCTION ----------------
def get_filtered_students():
    query = f"""
    SELECT s.name, s.course_batch, p.problems_solved, 
           ss.communication, pl.mock_interview_score,
           pl.internships_completed, pl.placement_status
    FROM students s
    JOIN programming p ON s.student_id = p.student_id
    JOIN soft_skills ss ON s.student_id = ss.student_id
    JOIN placements pl ON s.student_id = pl.student_id
    WHERE p.problems_solved >= {min_problems}
    AND ss.communication >= {min_communication}
    AND pl.mock_interview_score >= {min_interview}
    AND pl.internships_completed >= {min_internships}
    """

    if batch != "All":
        query += f" AND s.course_batch = '{batch}'"

    if status != "All":
        query += f" AND pl.placement_status = '{status}'"

    return db.fetchall(query)

# ---------------- SHOW FILTERED DATA ----------------
st.subheader("🎯 Eligible Students")

if submit:
    results = get_filtered_students()
    df = pd.DataFrame(results, columns=[
        "Name", "Batch", "Problems", "Communication",
        "Interview", "Internships", "Status"
    ])
    st.dataframe(df)

    st.download_button(
        "📥 Download Data",
        df.to_csv(index=False),
        file_name="filtered_students.csv"
    )

# ---------------- INSIGHTS ----------------
st.markdown("---")
st.header("📊 SQL Insights")

# ---------- QUERY BUTTONS ----------
col1, col2 = st.columns(2)

with col1:
    if st.button("1️⃣ Top 5 Students"):
        st.dataframe(pd.DataFrame(
            queries.top_5_students(),
            columns=["Name", "Problems", "Interview"]
        ))

    if st.button("2️⃣ Avg Programming by Batch"):
        st.dataframe(pd.DataFrame(
            queries.avg_programming_by_batch(),
            columns=["Batch", "Avg Problems"]
        ))

    if st.button("3️⃣ Soft Skills Distribution"):
        st.dataframe(pd.DataFrame(
            queries.soft_skills_distribution(),
            columns=[
                "Communication", "Teamwork", "Presentation",
                "Leadership", "Critical Thinking", "Interpersonal"
            ]
        ))

    if st.button("4️⃣ Placement Status Count"):
        st.dataframe(pd.DataFrame(
            queries.placement_status_count(),
            columns=["Status", "Count"]
        ))

    if st.button("5️⃣ Students with Internships > 1"):
        st.dataframe(pd.DataFrame(
            queries.students_with_internships(),
            columns=["Name", "Internships"]
        ))

with col2:
    if st.button("6️⃣ High Soft Skills"):
        st.dataframe(pd.DataFrame(
            queries.high_soft_skills(),
            columns=["Name", "Communication", "Teamwork"]
        ))

    if st.button("7️⃣ Low Coding + High Soft Skills"):
        st.dataframe(pd.DataFrame(
            queries.low_coding_high_soft(),
            columns=["Name", "Problems", "Communication"]
        ))

    if st.button("8️⃣ Avg Interview Score"):
        st.dataframe(pd.DataFrame(
            queries.avg_mock_interview_score(),
            columns=["Avg Interview Score"]
        ))

    if st.button("9️⃣ High Package Students"):
        st.dataframe(pd.DataFrame(
            queries.high_package_students(),
            columns=["Name", "Package"]
        ))

    if st.button("🔟 Top Performers"):
        st.dataframe(pd.DataFrame(
            queries.top_performers(),
            columns=["Name", "Problems", "Interview"]
        ))

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Built with Streamlit + SQL + Python")