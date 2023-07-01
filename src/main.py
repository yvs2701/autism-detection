from keras.models import load_model
import streamlit as st
import pandas as pd
import numpy as np

# load the saved model from keras
model = load_model("classifier")

st.title("Autism Detection - DL classification")

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    a1 = st.number_input(label="Ans 1 score", min_value=0, max_value=1, step=1)
with col2:
    a2 = st.number_input(label="Ans 2 score", min_value=0, max_value=1, step=1)
with col3:
    a3 = st.number_input(label="Ans 3 score", min_value=0, max_value=1, step=1)

with col1:
    a4 = st.number_input(label="Ans 4 score", min_value=0, max_value=1, step=1)
with col2:
    a5 = st.number_input(label="Ans 5 score", min_value=0, max_value=1, step=1)
with col3:
    a6 = st.number_input(label="Ans 6 score", min_value=0, max_value=1, step=1)

with col1:
    a7 = st.number_input(label="Ans 7 score", min_value=0, max_value=1, step=1)
with col2:
    a8 = st.number_input(label="Ans 8 score", min_value=0, max_value=1, step=1)
with col3:
    a9 = st.number_input(label="Ans 9 score", min_value=0, max_value=1, step=1)

with col1:
    a10 = st.number_input(label="Ans 10 score", min_value=0, max_value=1, step=1)
with col2:
    age = st.number_input(label="Age", min_value=0, max_value=1, step=1)
with col3:
    gender = st.selectbox(
        'Gender',
        ('Female', 'Male'))

with col1:
    ethnicity = st.selectbox(
        'Ethnicity',
        ('Others', 'Middle Eastern', 'South Asian', 'Asian', 'Black', 'Hispanic',
        'Latino', 'Pasifika', 'Turkish', 'White-European'))
with col2:
    jundice = st.selectbox(
        'Jundice',
        ('no', 'yes'))
with col3:
    austim = st.selectbox(
        'Austim',
        ('no', 'yes'))

with col1:
    used_app_before = st.selectbox(
        'Used app before',
        ('no', 'yes'))
with col2:
    result = st.number_input(label="result", min_value=0, step=1)
with col3:
    relation = st.selectbox(
        'Relation',
        ('Self', 'Health care professional', 'Others',
        'Parent', 'Relative'))

# creating a button for Prediction
if st.button("Autism Screening"):
    columns = [
                "A1_Score", "A2_Score", "A3_Score", "A4_Score", "A5_Score", "A6_Score", "A7_Score", "A8_Score", "A9_Score", "A10_Score",
                "age",
                "result",
                # gender
                "gender_f",
                "gender_m",
                # ethnicity
                "ethnicity_'Middle Eastern '", "ethnicity_'South Asian'", "ethnicity_Asian", "ethnicity_Black", "ethnicity_Hispanic", "ethnicity_Latino", "ethnicity_Others", "ethnicity_Pasifika", "ethnicity_Turkish", "ethnicity_White-European",
                # jundice
                "jundice_no", "jundice_yes",
                # austim
                "austim_no", "austim_yes",
                # used_app_before
                "used_app_before_no", "used_app_before_yes",
                # relation
                "relation_'Health care professional'", "relation_Others", "relation_Parent", "relation_Relative", "relation_Self",
            ]
    with st.spinner("Processing..."):
        print("Processing...")
        # Create a dataframe from user input from the fields above
        df = pd.DataFrame (
                            [[
                                a1, a2, a3,
                                a4, a5, a6,
                                a7, a8, a9,
                                a10, age, result,

                                1 if gender == 'Female' else 0,
                                1 if gender == 'Male' else 0,

                                1 if ethnicity == 'Middle Eastern' else 0,
                                1 if ethnicity == 'South Asian' else 0,
                                1 if ethnicity == 'Asian' else 0,
                                1 if ethnicity == 'Black' else 0,
                                1 if ethnicity == 'Hispanic' else 0,
                                1 if ethnicity == 'Latino' else 0,
                                1 if ethnicity == 'Others' else 0,
                                1 if ethnicity == 'Pasifika' else 0,
                                1 if ethnicity == 'Turkish' else 0,
                                1 if ethnicity == 'White-European' else 0,

                                1 if jundice == 'no' else 0,
                                1 if jundice == 'yes' else 0,

                                1 if austim == 'no' else 0,
                                1 if austim == 'yes' else 0,

                                1 if used_app_before == 'no' else 0,
                                1 if used_app_before == 'yes' else 0,

                                1 if relation == 'Health care professional' else 0,
                                1 if relation == 'Others' else 0,
                                1 if relation == 'Parent' else 0,
                                1 if relation == 'Relative' else 0,
                                1 if relation == 'Self' else 0,
                            ]],
                            columns=columns
                        )

        prediction = (model.predict(np.asarray(df).astype(np.float32)))[0]
        print(prediction)

        if np.argmax(prediction) == 1:
            diagnosis = "The person is autistic"
            st.write('### The person is autistic', round((prediction[1] * 100), 2), '%')
            st.warning(diagnosis, icon="⚠️")
        else:
            diagnosis = "The person is not autistic"
            st.write('### The person is *not* autistic', round((prediction[0] * 100), 2), '%')
            st.success(diagnosis, icon="✅")
