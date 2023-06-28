from keras.models import load_model
import streamlit as st
import time

# load the saved model from keras
model = load_model("classifier")

# Diabetes Prediction Page
# page title
st.title("Autism Detection - DL classification")

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    a1 = st.text_input("A1")
with col2:
    a2 = st.text_input("A2")
with col3:
    a3 = st.text_input("A3")

with col1:
    a4 = st.text_input("A4")
with col2:
    a5 = st.text_input("A5")
with col3:
    a6 = st.text_input("A6")

with col1:
    a7 = st.text_input("A7")
with col2:
    a8 = st.text_input("A8")
with col3:
    a9 = st.text_input("A9")

with col1:
    a10 = st.text_input("A10")
with col2:
    age = st.text_input("Age")
with col3:
    gender = st.text_input("Gender")

with col1:
    ethnicity = st.text_input("ethnicity")
with col2:
    jundice = st.text_input("jundice")
with col3:
    austim = st.text_input("austim")

with col1:
    contry_of_res = st.text_input("contry_of_res")
with col2:
    used_app_before = st.text_input("used_app_before")
with col3:
    result = st.text_input("result")

with col1:
    age_desc = st.text_input("age_desc")
with col2:
    relation = st.text_input("relation")
with col3:
    class_asd = st.text_input("class")

# creating a button for Prediction
if st.button("Autism Screening"):
    with st.spinner('Processing...'):
        print("Processing...")
        time.sleep(5)
        # # create a dataframe use one hot encoding to get the user input
        # # match the columns of the training data

        # THIS IS WRONG:
        # prediction = model.predict(
        #     [
        #         [
        #             a1, a2, a3,
        #             a4, a5, a6,
        #             a7, a8, a9,
        #             a10, age, gender,
        #             ethnicity, jundice, austim,
        #             contry_of_res, used_app_before, result,
        #             age_desc, relation, class_asd
        #         ]
        #     ]
        # )

        # if prediction[0] == 1:
        #     diagnosis = "The person is autistic"
        #     st.warn(diagnosis, icon="⚠️")
        # else:
        #     diagnosis = "The person is not autistic"
        #     st.success(diagnosis, icon="✅")
