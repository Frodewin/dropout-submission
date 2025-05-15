import streamlit as st
import pandas as pd
from joblib import load

st.header("Dashboard Predicting Student Dropout", divider=True)

tab1, tab2 = st.tabs(["Simulation", "Using Table"])

with tab1:
    st.header("Manual Entering Data")
    col1, col2, col3 = st.columns(3)

    import streamlit as st

    def select_box(label, options):
        if isinstance(options, dict):
            options_dict = {k: v for k, v in options.items()}
        elif isinstance(options, list):
            options_dict = {k: k for k in options}
        else:
            raise ValueError("Options harus berupa dict atau list")

        options_with_blank = [""] + list(options_dict.keys())
        selected = st.selectbox(label, options_with_blank)
        return options_dict.get(selected, None)

    with col1:
        Daytime = select_box("Daytime", {"Daytime": 1, "Evening": 0})
        Displaced = select_box("Displaced", {"Yes": 1, "No": 0})
        Edu_spec_needs = select_box("Edu Special Needs", {"Yes": 1, "No": 0})
        Debtor = select_box("Debtor", {"Yes": 1, "No": 0})
        Tuition_utd = select_box("Tuition Up To Date", {"Yes": 1, "No": 0})
        Gender = select_box("Gender", {"Male": 1, "Female": 0})
        Scholarship = select_box("Scholarship", {"Yes": 1, "No":0})
        International = select_box("International", {"Yes": 1, "No": 0})
        Prev_qualification = select_box("Previous Qualification",[
            "school_edu",
            "higher_edu",
            "vocational_professional",
        ])
        Nationality = select_box("Nationality",[
            "portuguese",
            "others",
        ])
        Mother_qualification = select_box("Mother Qualification",[
            "higher_edu_degree",
            "school_edu_degree",
            "others"
        ])
        Father_qualification = select_box("Father Qualification",[
            "higher_edu_degree",
            "school_edu_degree",
            "others"
        ])
        

    with col2:
        Mother_occupation = select_box("Mother Occupation",[
            'professional_or_expert',
            'inter_tech_or_prof_personnel',
            'administration_or_office',
            'services_or_seller',
            'skilled_worker',
            'unskilled_worker',
            'others'
        ])

        Father_occupation = select_box("Father Occupation", [
            'professional_or_expert',
            'inter_tech_or_prof_personnel',
            'administration_or_office',
            'services_or_seller',
            'skilled_worker',
            'machine_opt_and_installer',
            'armed_forces',
            'unskilled_worker',
            'others'
        ])
        Credited_1st = select_box("First Semester Credited", ["0","1+"])
        Enrolled_1st = select_box("First Semester Enrolled", ["0-4", "5-8", "9+"])
        Evaluation_1st = select_box("First Semester Evaluations", ["0-5", "6-10", "11+"])
        Approved_1st = select_box("First Semester Approved", ["0-4", "5-8", "9+"])
        Wo_evaluation_1st = select_box("First Semester Without Evaluations", ["0","1+"])
        Credited_2nd = select_box("Second Semester Credited", ["0","1+"])
        Enrolled_2nd = select_box("Second Semester Enrolled", ["0-4", "5-8", "9+"])
        Evaluation_2nd = select_box("Second Semester Evaluations", ["0-5", "6-10", "11+"])
        Approved_2nd = select_box("Second Semester Approved", ["0-4", "5-8", "9+"])
        Wo_evaluation_2nd = select_box("Second Semester Without Evaluations", ["0","1+"])

    with col3:
        Application_order = select_box("Application Order", ["0-1","2-3","3+"])
        Marital_status = select_box("Marital Status", [
            "single", "married", "others"])
        Application_mode = select_box("Application Mode", [
            "general", "others"])
        Course = select_box("Course",[
            'health_course',
            'business_and_management_course',
            'social_services_course',
            'design_and_communication_course',
            'nature_and_engineering_course',
            'others'                          
        ])
        Age = select_box("Age", [
            "17-24",
            "25-30",
            "31+"
        ])
        Prev_qualification_grade = st.text_input("Previous Qualification Grade (0-200)")
        Admission_grade = st.text_input("Admission Grade (0-200)")
        Grade_1st = st.text_input("First Semester Grade (1-20)")
        Grade_2nd = st.text_input("Second Semester Grade (1-20)")
        Unemployment_rate = st.text_input("Unemployment Rate")
        Inflation_rate = st.text_input("Inflation Rate")
        GDP = st.text_input("GDP")

    if st.button("Predict", key="Predict Manual"):
        required_fields = {
            "Daytime_evening_attendance": Daytime,
            "Displaced": Displaced,
            "Educational_special_needs": Edu_spec_needs,
            "Debtor": Debtor,
            "Tuition_fees_up_to_date": Tuition_utd,
            "Gender": Gender,
            "Scholarship_holder": Scholarship,
            "International": International,
            "Marital_status_grouped": Marital_status,
            "Application_mode_grouped": Application_mode,
            "Course_grouped": Course,
            "Previous_qualification_grouped": Prev_qualification,
            "Nationality_grouped": Nationality,
            "Mothers_qualification_grouped": Mother_qualification,
            "Fathers_qualification_grouped": Father_qualification,
            "Mother_occupation_grouped": Mother_occupation,
            "Father_occupation_grouped": Father_occupation,
            "Application_order_grouped": Application_order,
            "Age_at_enrollment_grouped": Age,
            "Curricular_units_1st_sem_credited_grouped": Credited_1st,
            "Curricular_units_1st_sem_enrolled_grouped": Enrolled_1st,
            "Curricular_units_1st_sem_evaluations_grouped": Evaluation_1st,
            "Curricular_units_1st_sem_approved_grouped": Approved_1st,
            "Curricular_units_1st_sem_without_evaluations_grouped": Wo_evaluation_1st,
            "Curricular_units_2nd_sem_credited_grouped": Credited_2nd,
            "Curricular_units_2nd_sem_enrolled_grouped": Enrolled_2nd,
            "Curricular_units_2nd_sem_evaluations_grouped": Evaluation_2nd,
            "Curricular_units_2nd_sem_approved_grouped": Approved_2nd,
            "Curricular_units_2nd_sem_without_evaluations_grouped": Wo_evaluation_2nd,
            "Previous_qualification_grade": Prev_qualification_grade,
            "Admission_grade": Admission_grade,
            "Curricular_units_1st_sem_grade": Grade_1st,
            "Curricular_units_2nd_sem_grade": Grade_2nd,
            "Unemployment_rate": Unemployment_rate,
            "Inflation_rate": Inflation_rate,
            "GDP": GDP

        }

        numeric_fields = {
            "Previous_qualification_grade": Prev_qualification_grade,
            "Admission_grade": Admission_grade,
            "Curricular_units_1st_sem_grade": Grade_1st,
            "Curricular_units_2nd_sem_grade": Grade_2nd,
            "Unemployment_rate": Unemployment_rate,
            "Inflation_rate": Inflation_rate,
            "GDP": GDP
        }

        numeric_values = {}
        invalid_fields = []

        for field, value in numeric_fields.items():
            try:
                numeric_values[field] = float(value)
            except ValueError:
                invalid_fields.append(field)


        missing_fields = [field for field, value in required_fields.items() if value is None]

        if missing_fields or invalid_fields:
            if missing_fields:
                st.error(f"Please select values for: {', '.join(missing_fields)}")
            if invalid_fields:
                st.error(f"The following fields must be numeric: {', '.join(invalid_fields)}")
        else:
            input_data = {
                "Daytime_evening_attendance": Daytime,
                "Previous_qualification_grade": Prev_qualification_grade,
                "Admission_grade": Admission_grade,
                "Displaced": Displaced,
                "Educational_special_needs": Edu_spec_needs,
                "Debtor": Debtor,
                "Tuition_fees_up_to_date": Tuition_utd,
                "Gender": Gender,
                "Scholarship_holder": Scholarship,
                "International": International,
                "Curricular_units_1st_sem_grade": Grade_1st,
                "Curricular_units_2nd_sem_grade": Grade_2nd,
                "Unemployment_rate": Unemployment_rate,
                "Inflation_rate": Inflation_rate,
                "GDP": GDP,
                "Marital_status_grouped": Marital_status,
                "Application_mode_grouped": Application_mode,
                "Course_grouped": Course,
                "Previous_qualification_grouped": Prev_qualification,
                "Nationality_grouped": Nationality,
                "Mothers_qualification_grouped": Mother_qualification,
                "Fathers_qualification_grouped": Father_qualification,
                "Mothers_occupation_grouped": Mother_occupation,
                "Fathers_occupation_grouped": Father_occupation,
                "Application_order_grouped": Application_order,
                "Age_at_enrollment_grouped": Age,
                "Curricular_units_1st_sem_credited_grouped": Credited_1st,
                "Curricular_units_1st_sem_enrolled_grouped": Enrolled_1st,
                "Curricular_units_1st_sem_evaluations_grouped": Evaluation_1st,
                "Curricular_units_1st_sem_approved_grouped": Approved_1st,
                "Curricular_units_1st_sem_without_evaluations_grouped": Wo_evaluation_1st,
                "Curricular_units_2nd_sem_credited_grouped": Credited_2nd,
                "Curricular_units_2nd_sem_enrolled_grouped": Enrolled_2nd,
                "Curricular_units_2nd_sem_evaluations_grouped": Evaluation_2nd,
                "Curricular_units_2nd_sem_approved_grouped": Approved_2nd,
                "Curricular_units_2nd_sem_without_evaluations_grouped": Wo_evaluation_2nd
            }

            # Buat DataFrame dari 1 row input user
            new_data = pd.DataFrame([input_data])
            
            model = load('RF_model.joblib')
            lab_encoder = load('preprocessed/label_encoders.pkl')
            stndr_scaler = load('preprocessed/standard_scaler.pkl')

            for column, le in lab_encoder.items():
                if column in new_data.columns:
                    new_data[column] = le.transform(new_data[column])  # Hati-hati jika ada label baru

            for column, scaler in stndr_scaler.items():
                if column in new_data.columns:
                    new_data[column] = scaler.transform(new_data[[column]])  # Hati-hati jika ada label baru
            # Prediksi
            X = new_data.copy()
            preds = model.predict(X)
            probas = model.predict_proba(X)[:, 1]

            # Tambahkan hasil prediksi
            X['Dropout_Probability'] = probas
            X['Predicted_Status'] = ['Dropout' if p == 1 else 'Graduate' for p in preds]

            # Tampilkan hasil
            st.success("Prediction Completed")
            st.dataframe(X[['Dropout_Probability', 'Predicted_Status']])

with tab2:
    st.header("Using Template Table to input multiple rows")
    st.download_button(
        label = "Download Table Template",
        data = "data/template.csv",
        file_name= "template.csv",
        mime='text/csv',
        icon="👉"
    )
    uploaded_file = st.file_uploader("Choose CSV File", type=["csv"])
    if uploaded_file is not None:
    # Baca sebagai DataFrame
        df = pd.read_csv(uploaded_file, sep=";")
        if "Status" in df.columns:
            df = df.drop(columns=["Status"])
        
        st.success("File berhasil diunggah!")
        st.write("Preview Data:")
        st.dataframe(df.head(5))
    else:
        st.info("Silakan unggah file CSV untuk mulai.")

    if st.button("Predict", key="Predict Table"):
        # Buat DataFrame dari 1 row input user
        
        model = load('RF_model.joblib')
        lab_encoder = load('preprocessed/label_encoders.pkl')
        stndr_scaler = load('preprocessed/standard_scaler.pkl')

        for column, le in lab_encoder.items():
            if column in df.columns:
                df[column] = le.transform(df[column])  # Hati-hati jika ada label baru

        for column, scaler in stndr_scaler.items():
            if column in df.columns:
                df[column] = scaler.transform(df[[column]])  # Hati-hati jika ada label baru
        # Prediksi
        X = df.copy()
        preds = model.predict(X)
        probas = model.predict_proba(X)[:, 1]

        # Tambahkan hasil prediksi
        X['Dropout_Probability'] = probas
        X['Predicted_Status'] = ['Dropout' if p == 1 else 'Graduate' for p in preds]

        # Tampilkan hasil
        st.success("Prediction Completed")
        st.dataframe(X[['Dropout_Probability', 'Predicted_Status']].head(5))

        # Konversi DataFrame ke CSV
        csv = X.to_csv(index=False)

        # Tampilkan tombol download
        st.download_button(
            label="📥 Download Hasil Prediksi sebagai CSV",
            data=csv,
            file_name='hasil_prediksi.csv',
            mime='text/csv'
        )