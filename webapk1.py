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

st.title('Aplikasi Perhitungan Kadar(%b/v)')

normalitas = st.number_input('Masukan Nilai Normalitas Titran (N)')
volume = st.number_input('Masukan Nilai Volume Titran (mL)')
be = st.number_input('Masukan nilai BE')
volumee = st.number_input('Masukan Nilai Volume Titrat (mL)')

tombol = st.button('Hitung Nilai Kadar(%(b/v))')

if tombol:
    nilai_persentase = volume*normalitas*be*10**-3*100/(volumee) 
    st.success(f'Nilai Normalitas adalah {nilai_persentase}')
	
import streamlit as st1
	
st.title('Aplikasi Perhitungan Kadar(%b/b)')

normalitas = st1.number_input('Masukan Nilai Normalitas Titran (N)')
volume = st1.number_input('Masukan Nilai Volume Titran (mL)')
be = st1.number_input('Masukan nilai BE')
gram = st1.number_input('Masukan Nilai Gram Contoh (g)')

tombol = st.button('Hitung Nilai Kadar(%(b/b))')

if tombol:
    nilai_persentase = volume*normalitas*be*10**-3*100/(gram) 
    st.success(f'Nilai Normalitas adalah {nilai_persentase}')
