import streamlit as st

st.title("Aplikasi Perhitungan Kadar(%b/v)")

normalitas = st.number_input("Masukan Nilai Normalitas Titran (N)")
volume = st.number_input("Masukan Nilai Volume Titran (mL)")
be = st.number_input("Masukan nilai BE")
volumee = st.number_input("Masukan Nilai Volume Titrat (mL)")
fp = st.number_input("Masukkan Nilai FP")

tombol = st.button("Hitung Nilai Kadar(%(b/v))")

if tombol:
    nilai_persentase = volume*normalitas*be*fp*10**-3*100/(volumee) 
    st.success(f"Nilai Kadar (%(b/v)) adalah {nilai_persentase}")
