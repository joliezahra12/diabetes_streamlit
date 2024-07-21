import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.title('Prediksi Diabetes')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('input Pregnancies')

with col2 :
    Glucose = st.text_input ('input Glucose')

with col1 :
    BloodPressure = st.text_input ('input BloodPressure')

with col2 :
    SkinThickness = st.text_input ('input SkinThickness')

with col1 :
    Insulin = st.text_input ('input Insulin')

with col2 :
    BMI = st.text_input ('input BMI')

with col1 :
    DiabetesPedigreeFunction = st.text_input ('input DiabetesPedigreeFunction')

with col2 :
    Age = st.text_input ('input Age')


# code untuk prediksi
diabetes_pred = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

   if upitrans_pred == '0':
    return "Tidak Diabetes"
elif upitrans_pred == '1':
    return "Diabetes"
else:
    return None
st.success(diabetes_pred)