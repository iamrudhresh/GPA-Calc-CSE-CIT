import streamlit as st
department_subjects = {
    "CSE": [
        {"code": "MA2401", "name": "Discrete Mathematics", "credits": 3},
        {"code": "CS2401", "name": "Operating System", "credits": 4},
        {"code": "CS2402", "name": "Artificial Intelligence and Machine Learning", "credits": 4},
        {"code": "CS2403", "name": "Computer Networks", "credits": 4},
        {"code": "CS2404", "name": "Web Frameworks", "credits": 4},
        {"code": "CS2405", "name": "Software Engineering", "credits": 4},
        {"code": "ES2401", "name": "Employability Enhancement Skills", "credits": 0},
        {"code": "HS2401", "name": "Tamils and Technology", "credits": 1},
    ],
    "IT": [
        {"code": "MA2401", "name": "Discrete Mathematics", "credits": 3},
        {"code": "CS2401", "name": "Operating System", "credits": 4},
        {"code": "CS2402", "name": "Artificial Intelligence and Machine Learning", "credits": 4},
        {"code": "CS2403", "name": "Computer Networks", "credits": 4},
        {"code": "CS2404", "name": "Web Frameworks", "credits": 4},
        {"code": "CS2405", "name": "Software Engineering", "credits": 4},
        {"code": "ES2401", "name": "Employability Enhancement Skills", "credits": 0},
        {"code": "HS2401", "name": "Tamils and Technology", "credits": 1},
    ],
    "AI&DS": [
        {"code": "MA2401", "name": "Discrete Mathematics", "credits": 3},
        {"code": "AD2401", "name": "Operating System", "credits": 4},
        {"code": "AD2402", "name": "Machine Learning", "credits": 4},
        {"code": "AD2403", "name": "Computer Networks", "credits": 4},
        {"code": "AD2404", "name": "Web Frameworks", "credits": 4},
        {"code": "AD2405", "name": "Artificial Intelligence", "credits": 3},
        {"code": "ES2401", "name": "Employability Enhancement Skills", "credits": 1},
        {"code": "HS2401", "name": "Tamils and Technology", "credits": 1},
    ],
    "AI&ML": [
        {"code": "MA2401", "name": "Discrete Mathematics", "credits": 3},
        {"code": "AM2401", "name": "Operating System", "credits": 4},
        {"code": "AM2402", "name": "Machine Learning", "credits": 4},
        {"code": "AM2403", "name": "Computer Networks", "credits": 4},
        {"code": "AM2404", "name": "Web Frameworks", "credits": 4},
        {"code": "AM2405", "name": "Artificial Intelligence", "credits": 3},
        {"code": "ES2401", "name": "Employability Enhancement Skills", "credits": 1},
        {"code": "HS2401", "name": "Tamils and Technology", "credits": 1},
    ],
    "ECE": [
        {"code": "EC2401", "name": "Control Systems", "credits": 3},
        {"code": "EC2402", "name": "Transmission lines and RF Design", "credits": 3},
        {"code": "EC2403", "name": "Microprocessors and Microcontrollers", "credits": 4},
        {"code": "EC2404", "name": "Digital Signal Processing", "credits": 4},
        {"code": "EC2405", "name": "Communication Systems", "credits": 4},
        {"code": "EC2406", "name": "VLSI design", "credits": 4},
        {"code": "EC2407", "name": "Course Project", "credits": 1},
        {"code": "ES2401", "name": "Employability Enhancement Skills", "credits": 0},
        {"code": "HS2401", "name": "Tamils and Technology", "credits": 1},
    ]
}

grade_to_point = {
    "O": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "RA": 0
}

# Streamlit app
st.set_page_config(page_title="GPA Calculator - 4th Sem", page_icon="📊")

st.markdown("<h1 style='text-align: center;'>GPA Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>By <strong>Rudhresh S</strong></p>", unsafe_allow_html=True)

department = st.selectbox("Select your department", options=["Select"] + list(department_subjects.keys()))

if department != "Select":
    st.write(f"Enter your grades for the following subjects in {department} department:")

    subjects = department_subjects[department]
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
