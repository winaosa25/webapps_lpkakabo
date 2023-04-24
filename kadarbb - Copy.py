import streamlit as st

st.title('Aplikasi Perhitungan Kadar(%b/b)')

normalitas = st1.number_input('Masukan Nilai Normalitas Titran (N)')
volume = st1.number_input('Masukan Nilai Volume Titran (mL)')
be = st1.number_input('Masukan nilai BE')
gram = st1.number_input('Masukan Nilai Gram Contoh (g)')
fp = st.number_input('Masukkan Nilai FP')

tombol = st.button('Hitung Nilai Kadar(%(b/b))')

if tombol:
    nilai_persentase = volume*normalitas*be*fp*10**-3*100/(gram) 
    st.success(f'Nilai Normalitas adalah {nilai_persentase}')