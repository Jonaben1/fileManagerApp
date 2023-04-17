import streamlit as st
import os
import shutil
from files import see_files



def move_files():
    '''Move files to a folder'''
    st.header('Move Files')
    st.warning('Becareful to avoid overwriting files')
    st.info('For files inside a folder, separate the folder from the files using slash (/)')
    st.text('Your current directory contains')
    st.text(os.listdir())
    if st.selectbox('Do you want to create a folder?', ['No', 'Yes']) == 'Yes':
        folder = st.text_input('Enter name of the folder')
        if folder:
            os.mkdir(folder)
            st.text(f'{folder} folder created!')
    ch = st.selectbox('Do you want to see files in a folder?', ['No', 'Yes'])
    if ch == 'Yes':
        file = st.text_input('Enter the name of the folder')
        if file:
            st.text(see_files(file))
    file = st.text_input('Enter the file or folder or both')
    dest = st.text_input('Enter a new name or destination folder followed by the new name')
    if st.button('Move'):
        shutil.move(file, dest)
        st.success('File Moved!')

