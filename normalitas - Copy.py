import streamlit as st

st.title('Aplikasi Perhitungan Normalitas(N)')

bobot = st.number_input('Masukan Nilai Bobot Standar Primer (mg)')
volume = st.number_input('Masukan Nilai Volume Standar Sekunder (mL)')
be = st.number_input('Masukan nilai BE Standar Primer')
fp = st.number_input('Masukkan Nilai FP')

tombol = st.button('Hitung Nilai Normalitas')

if tombol:
    nilai_normalitas = bobot/(fp*be*volume) 
    st.success(f'Nilai Normalitas adalah {nilai_normalitas}')
