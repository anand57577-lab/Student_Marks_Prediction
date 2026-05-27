import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(
    page_title="Student Final Exam Marks Predictor",
    page_icon="🎓",
    layout="wide"
)

# Load trained model
model = joblib.load("student_marks_model.pkl")

# Custom CSS Styling
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #1e3a8a, #06b6d4);
}
.stApp {
    background: linear-gradient(135deg, #0b1020, #132a4a, #0ea5e9);
    color: white;
}
.title-container {
    text-align: center;
    padding: 25px;
    border-radius: 24px;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(14px);
    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
    margin-bottom: 30px;
}
.main-title {
    font-size: 3rem;
    font-weight: 800;
    color: white;
}
.sub-text {
    font-size: 1.15rem;
    color: #dbeafe;
}
.prediction-box {
    padding: 28px;
    border-radius: 22px;
    text-align: center;
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    font-size: 2.2rem;
    font-weight: bold;
    box-shadow: 0 10px 30px rgba(34,197,94,0.35);
    margin-top: 25px;
}
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb, #06b6d4);
    color: white;
    font-size: 20px;
    font-weight: bold;
    border-radius: 16px;
    padding: 14px;
    border: none;
    transition: 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg, #1d4ed8, #0891b2);
}
[data-testid="stNumberInput"] {
    background-color: rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 8px;
}
.insight-container {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 22px;
    backdrop-filter: blur(16px);
    box-shadow: 0 10px 35px rgba(0,0,0,0.25);
    border: 1px solid rgba(255,255,255,0.08);
    min-height: 100%;
}
.insight-title {
    text-align: center;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 20px;
    color: white;
}
.metric-card {
    background: linear-gradient(135deg, rgba(37,99,235,0.35), rgba(6,182,212,0.25));
    padding: 18px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 14px;
    box-shadow: 0 8px 18px rgba(0,0,0,0.2);
    border: 1px solid rgba(255,255,255,0.08);
}
.metric-label {
    font-size: 1rem;
    color: #dbeafe;
}
.metric-value {
    font-size: 1.8rem;
    font-weight: bold;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="title-container">
    <div class="main-title">🎓 Student Final Exam Marks Predictor</div>
    <div class="sub-text">
        Predict final exam performance using attendance, sessional scores, assignment score, and daily study hours.
    </div>
</div>
""", unsafe_allow_html=True)

# Layout columns
col1, col2 = st.columns([1, 1])

# Left Section
with col1:
    st.subheader("📘 Enter Student Performance Details")

    attendance = st.number_input(
        "Attendance (%)",
        min_value=0,
        max_value=100,
        value=80
    )

    sessional_1 = st.number_input(
        "Sessional 1 (out of 40)",
        min_value=0,
        max_value=40,
        value=30
    )

    sessional_2 = st.number_input(
        "Sessional 2 (out of 40)",
        min_value=0,
        max_value=40,
        value=30
    )

    assignment_score = st.number_input(
        "Assignment Score (out of 10)",
        min_value=0,
        max_value=10,
        value=7
    )

    daily_study_hours = st.number_input(
        "Daily Study Hours",
        min_value=0,
        max_value=24,
        value=3
    )

# Right Section
with col2:
    st.markdown('<div class="insight-container">', unsafe_allow_html=True)

    st.markdown('<div class="insight-title">📊 Performance Insights</div>', unsafe_allow_html=True)

    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)

    with row1_col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📅 Attendance</div>
            <div class="metric-value">{attendance}%</div>
        </div>
        """, unsafe_allow_html=True)

    with row1_col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📝 Sessional 1</div>
            <div class="metric-value">{sessional_1}/40</div>
        </div>
        """, unsafe_allow_html=True)

    with row2_col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📚 Sessional 2</div>
            <div class="metric-value">{sessional_2}/40</div>
        </div>
        """, unsafe_allow_html=True)

    with row2_col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📄 Assignment</div>
            <div class="metric-value">{assignment_score}/10</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">⏳ Daily Study Hours</div>
        <div class="metric-value">{daily_study_hours} hrs/day</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📈 Academic Progress")
    st.write("Attendance")
    st.progress(attendance / 100)

    st.write("Sessional 1")
    st.progress(sessional_1 / 40)

    st.write("Sessional 2")
    st.progress(sessional_2 / 40)

    st.write("Assignment")
    st.progress(assignment_score / 10)

    st.markdown('</div>', unsafe_allow_html=True)

# Predict button
if st.button("🚀 Predict Final Marks"):

    user_data = pd.DataFrame(
        [[attendance, sessional_1, sessional_2, assignment_score, daily_study_hours]],
        columns=[
            'Attendance (%)',
            'Sessional_1',
            'Sessional_2',
            'Assignment Score (out of 10)',
            'Daily Study Hours'
        ]
    )

    prediction = model.predict(user_data)
    predicted_marks = round(prediction[0], 2)

    st.markdown(
        f"""
        <div class="prediction-box">
            🎯 Predicted Final Exam Marks: {predicted_marks}/100
        </div>
        """,
        unsafe_allow_html=True
    )

    if predicted_marks >= 85:
        st.balloons()
        st.success("🌟 Excellent Performance Expected!")
    elif predicted_marks >= 70:
        st.success("👍 Good Performance Expected!")
    elif predicted_marks >= 50:
        st.warning("📘 Average Performance — More focus can improve marks.")
    else:
        st.error("⚠️ High Risk — Consider improving attendance and study consistency.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Machine Learning + Streamlit")