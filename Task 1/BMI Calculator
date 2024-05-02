import streamlit as st 
import pandas as pd

st.title("BMI Calculator")

weight = st.slider("Enter the weight (in kgs)",1,100)

height = st.radio("Select your height format:", ("cms", "meters", "feet"))

bmi = None

if height == 'cms':
    height = st.number_input("Centimeter")
    if height:
        bmi = weight / ((height / 100) ** 2)
elif height == 'meters':
    height = st.number_input("Meters")
    if height:
        bmi = weight / (height ** 2)
else:
    height = st.number_input('Feet')
    if height:
        bmi = weight / (((height / 3.28)) ** 2)

if st.button("Calculate BMI"):
    if bmi:
        st.text("Your BMI Index is {:.2f}.".format(bmi))
        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Healthy")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
        else:
            st.error("Extremely Overweight")
    else:
        st.text("Please enter valid weight and height.")
