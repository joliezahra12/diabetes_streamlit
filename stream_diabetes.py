import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Prediksi Diabetes')

# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Input Pregnancies')
    Glucose = st.text_input('Input Glucose')
    BloodPressure = st.text_input('Input BloodPressure')
    SkinThickness = st.text_input('Input SkinThickness')
    Insulin = st.text_input('Input Insulin')
    
with col2:
    BMI = st.text_input('Input BMI')
    DiabetesPedigreeFunction = st.text_input('Input DiabetesPedigreeFunction')
    Age = st.text_input('Input Age')

# Code untuk prediksi
if st.button('Test Prediksi Diabetes'):
    try:
        # Konversi input menjadi float
        Pregnancies = float(Pregnancies)
        Glucose = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin = float(Insulin)
        BMI = float(BMI)
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
        Age = float(Age)

        # Prediksi menggunakan model
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        # Menampilkan hasil prediksi
        if diabetes_prediction[0] == 0:
            st.success("Tidak Diabetes")
        elif diabetes_prediction[0] == 1:
            st.success("Diabetes")
        else:
            st.warning("Status Prediksi Tidak Diketahui")
    
    except ValueError:
        st.error('Semua input harus berupa angka.')
    except Exception as e:
        st.error(f'Error: {e}')
