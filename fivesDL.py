import streamlit as st

st.set_page_config(layout='wide')

if "kumpulan" not in st.session_state:
    st.session_state.kumpulan={'kondisi1':True, 'kondisi2':False, 'kondisi3':False,
                               'kondisi4':False, 'kondisi5':False, 'kondisi6':False, 'kondisi7':False}


def tampilkan1():
    st.markdown("""
    <iframe src='https://martin123-oke.github.io/fives/kover_depan.html' style='width:100%; height:600px;'></iframe>
    """,unsafe_allow_html=True)
def tampilkan2():
    tab = st.tabs(["Visual","Fitur Interaktif","Aktivitas"])
    with tab[0]:
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/cerita_fakta.html' style='width:100%; height:2500px;'></iframe>
        """,unsafe_allow_html=True)
    with tab[1]:
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/Fitur_interaktif.html' style='width:100%; height:2500px;'></iframe>
        """,unsafe_allow_html=True)
    with tab[2]:
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/Aktivitas.html' style='width:100%; height:2500px;'></iframe>
        """,unsafe_allow_html=True)

def tampilkan3():
    tab = st.tabs(["Visual","Fitur Interaktif","Aktivitas"])
    with tab[0]:
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/visual2.html' style='width:100%; height:2500px;'></iframe>
        """,unsafe_allow_html=True)
    with tab[1]:
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/Fitur2.html' style='width:100%; height:3700px;'></iframe>
        """,unsafe_allow_html=True)
    with tab[2]:
        st.write("Akan dilanjutkan")

if st.session_state.kumpulan['kondisi1']:
    tampilkan1()
if st.session_state.kumpulan['kondisi2']:
    tampilkan2()
if st.session_state.kumpulan['kondisi3']:
    tampilkan3()
    
if st.sidebar.button('Tampilan Awal'):
    st.session_state.kumpulan={'kondisi1':True, 'kondisi2':False, 'kondisi3':False,
                               'kondisi4':False, 'kondisi5':False, 'kondisi6':False, 'kondisi7':False}
    st.rerun()
if st.sidebar.button('Fakta (F)'):
    st.session_state.kumpulan={'kondisi1':False, 'kondisi2':True, 'kondisi3':False,
                               'kondisi4':False, 'kondisi5':False, 'kondisi6':False, 'kondisi7':False}
    st.rerun()
if st.sidebar.button('Inferensi (I)'):
    st.session_state.kumpulan={'kondisi1':False, 'kondisi2':False, 'kondisi3':True,
                               'kondisi4':False, 'kondisi5':False, 'kondisi6':False, 'kondisi7':False}
    st.rerun()
if st.sidebar.button('Kosakata (V)'):
    pass
if st.sidebar.button('Pengalaman (E)'):
    pass
if st.sidebar.button('Ringkasan (S)'):
    pass
if st.sidebar.button('Latihan'):
    pass
if st.sidebar.button('Dashboard Guru'):
    pass
