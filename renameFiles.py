import streamlit as st
import os
from files import see_files



def rename_files():
    st.header('Rename Files')
    st.warning('Becareful to avoid overwriting files')
    st.info('For files inside a folder, separate the folder from the files using slash (/)')
    st.text('Your current directory contains')
    st.text(os.listdir())
    ch = st.selectbox('Do you want to see the files in a given folder?', ['No', 'Yes'])
    if ch == 'Yes':
        file = st.text_input('Enter the name of the folder')
        if file:
            st.text(see_files(file))
    file = st.text_input('Enter the file or folder you want to rename')
    dest = st.text_input('Enter the new name or destination folder followed by the new name')
    if st.button('Rename'):
        os.rename(file, dest)
        st.success('File Renamed!')

