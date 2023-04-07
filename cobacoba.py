import streamlit as st

st.title('Aplikasi Perhitungan Normalitas')

bobot = st.number_input('Masukan Nilai Bobot (g)')
volume = st.number_input('Masukan Nilai Volume (L)')
mr = st.number_input('Masukan nilai BE')

tombol = st.button('Hitung Nilai Normalitas')

if tombol:
    nilai_normalitas = Bobot/(BE*Volume) 
    st.success(f'Nilai Normalitas adalah {nilai_normalitas}')