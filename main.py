import streamlit as st

# Subject details
subjects = [
    {"code": "MA2401", "name": "Discrete Mathematics", "credits": 3},
    {"code": "CS2401", "name": "Operating System", "credits": 4},
    {"code": "CS2402", "name": "Artificial Intelligence and Machine Learning / Machine Learning", "credits": 4},
    {"code": "CS2403", "name": "Computer Networks", "credits": 4},
    {"code": "CS2404", "name": "Web Frameworks", "credits": 4},
    {"code": "CS2405", "name": "Software Engineering / Artificial Intelligence", "credits": 4},
    {"code": "ES2401", "name": "Employability Enhancement Skills", "credits": 0},
    {"code": "HS2401", "name": "Tamils and Technology", "credits": 1},
]

# Grade to point mapping
grade_to_point = {
    "O": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "RA": 0
}

# Streamlit app
st.set_page_config(page_title="GPA Calculator", page_icon="📊")

st.markdown("<h1 style='text-align: center; '>GPA Calculator for 4th Sem Result</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>By <strong>Rudhresh S</strong></p>", unsafe_allow_html=True)

st.write("Enter your grades for the following subjects:")

grades = {}
for subject in subjects:
    grade = st.selectbox(
        f"{subject['name']} ({subject['code']})",
        options=["Select"] + list(grade_to_point.keys()),
        key=subject['code']
    )
    grades[subject['code']] = grade

if st.button("Calculate GPA"):
    total_credits = 0
    total_points = 0
    missing_grades = False

    for subject in subjects:
        grade = grades[subject['code']]
        if grade == "Select":
            missing_grades = True
            break
        credits = subject["credits"]
        points = grade_to_point[grade]
        total_credits += credits
        total_points += points * credits

    if missing_grades:
        st.error("Please enter grades for all subjects.")
    elif total_credits > 0:
        gpa = total_points / total_credits
        st.success(f"Your GPA is: {gpa:.2f}")
    else:
        st.error("Please enter valid grades.")
