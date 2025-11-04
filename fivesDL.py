import streamlit as st

st.set_page_config(layout='wide')

if "kumpulan" not in st.session_state:
    st.session_state.kumpulan={'kondisi1':True, 'kondisi2':False, 'kondisi3':False,
                               'kondisi4':False, 'kondisi5':False, 'kondisi6':False, 'kondisi7':False,
                               'kondisi8':False}


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
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/Aktivitas2.html' style='width:100%; height:3700px;'></iframe>
        """,unsafe_allow_html=True)

def tampilkan4():
    tab = st.tabs(["Visual","Aktivitas"])
    with tab[0]:
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/visual3.html' style='width:100%; height:2500px;'></iframe>
        """,unsafe_allow_html=True)
    with tab[1]:
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/aktiitas3.html' style='width:100%; height:2500px;'></iframe>
        """,unsafe_allow_html=True)

def tampilkan5():
    tab = st.tabs(["Visual","Fitur Interaktif"])
    with tab[0]:
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/visual4.html' style='width:100%; height:2500px;'></iframe>
        """,unsafe_allow_html=True)
    with tab[1]:
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/Fitur3.html' style='width:100%; height:2500px;'></iframe>
        """,unsafe_allow_html=True)
        
def tampilkan6():
    tab = st.tabs(["Visual","Aktivitas"])
    with tab[0]:
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/visual5.html' style='width:100%; height:2500px;'></iframe>
        """,unsafe_allow_html=True)
    with tab[1]:
        st.markdown("""
        <iframe src='https://martin123-oke.github.io/fives/Aktivitas4.html' style='width:100%; height:2500px;'></iframe>
        """,unsafe_allow_html=True)
def tampilkan7():
    tab = st.tabs(["Visual","Aktivitas"])
    with tab[0]:
        pass
    with tab[1]:
        pass
def tampilkan8():
    tab = st.tabs(["Visual","Aktivitas"])
    with tab[0]:
        pass
    with tab[1]:
        pass


if st.session_state.kumpulan['kondisi1']:
    tampilkan1()
if st.session_state.kumpulan['kondisi2']:
    tampilkan2()
if st.session_state.kumpulan['kondisi3']:
    tampilkan3()
if st.session_state.kumpulan['kondisi4']:
    tampilkan4()
if st.session_state.kumpulan['kondisi5']:
    tampilkan5()
if st.session_state.kumpulan['kondisi6']:
    tampilkan6()
if st.session_state.kumpulan['kondisi7']:
    tampilkan7()
if st.session_state.kumpulan['kondisi8']:
    tampilkan8()
    
if st.sidebar.button('Tampilan Awal'):
    st.session_state.kumpulan={'kondisi1':True, 'kondisi2':False, 'kondisi3':False,
                               'kondisi4':False, 'kondisi5':False, 'kondisi6':False, 'kondisi7':False,
                               'kondisi8':False}
    st.rerun()
if st.sidebar.button('Fakta (F)'):
    st.session_state.kumpulan={'kondisi1':False, 'kondisi2':True, 'kondisi3':False,
                               'kondisi4':False, 'kondisi5':False, 'kondisi6':False, 'kondisi7':False,
                               'kondisi8':False}
    st.rerun()
if st.sidebar.button('Inferensi (I)'):
    st.session_state.kumpulan={'kondisi1':False, 'kondisi2':False, 'kondisi3':True,
                               'kondisi4':False, 'kondisi5':False, 'kondisi6':False, 'kondisi7':False,
                               'kondisi8':False}
    st.rerun()
if st.sidebar.button('Kosakata (V)'):
    st.session_state.kumpulan={'kondisi1':False, 'kondisi2':False, 'kondisi3':False,
                               'kondisi4':True, 'kondisi5':False, 'kondisi6':False, 'kondisi7':False,
                               'kondisi8':False}
    st.rerun()
if st.sidebar.button('Pengalaman (E)'):
    st.session_state.kumpulan={'kondisi1':False, 'kondisi2':False, 'kondisi3':False,
                               'kondisi4':False, 'kondisi5':True, 'kondisi6':False, 'kondisi7':False,
                               'kondisi8':False}
    st.rerun()
if st.sidebar.button('Ringkasan (S)'):
    st.session_state.kumpulan={'kondisi1':False, 'kondisi2':False, 'kondisi3':False,
                               'kondisi4':False, 'kondisi5':False, 'kondisi6':True, 'kondisi7':False,
                               'kondisi8':False}
    st.rerun()


