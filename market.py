
import streamlit as st
import webbrowser


url = 'https://felipeodonnell-model-main-ryfv0j.streamlit.app'

with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Blueblocks.ai")
    if st.button('All MVP Solutuons'):
        webbrowser.open_new_tab(url)

st.image('333368727_567698838713526_2956667945644696937_n.jpg')
