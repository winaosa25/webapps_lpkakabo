import streamlit as st

st.title('Aplikasi Perhitungan Normalitas(N) dan Kadar(%)')

st.title('Aplikasi Perhitungan Normalitas(N)')
bobot = st.number_input('Masukan Nilai Bobot Standar Primer (mg)')
volume = st.number_input('Masukan Nilai Volume Standar Sekunder (mL)')
be = st.number_input('Masukan nilai BE Standar Primer')
fp = st.number_input('Masukkan Nilai FP')

tombol = st.button('Hitung Nilai Normalitas')

if tombol:
    nilai_normalitas = bobot/(fp*be*volume) 
    st.success(f'Nilai Normalitas adalah {nilai_normalitas}')

import streamlit as st

st.title('Aplikasi Perhitungan Kadar(%)')
normalitas = st.number_input('Masukan Nilai Normalitas Titran (N)')
volume = st.number_input('Masukan Nilai Volume Titran (mL)')
be = st.number_input('Masukan nilai BE')
efpe = st.number_input('Masukkan Nilai FP')
volumee = st.number_input('Masukan Nilai Volume Titrat (mL) atau Gram Contoh (g)')

hitung = st.button('Hitung Nilai Kadar(%)')

if hitung:
    nilai_persentase = volume*normalitas*be*efpe*10**-3*100/(volumee) 
    st.success(f'Nilai Kadar (%) adalah {nilai_persentase}')