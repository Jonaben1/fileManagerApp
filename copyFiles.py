import streamlit as st
import os
import shutil
from files import see_files


def copy_files():
    st.header('Copy Files')
    st.text('Your current directory contains')
    st.text(os.listdir())
    if st.selectbox('Do you want to create a folder?', ['No', 'Yes']) == 'Yes':
        folder = st.text_input('Enter name of the folder')
        if folder:
            os.mkdir(folder)
            st.text(f'{folder} folder created!')
    ch = st.selectbox('Do you want to see the files in a given folder?', ['No', 'Yes'])
    if ch == 'Yes':
        file = st.text_input('Enter the name of the folder')
        if file:
            st.text(see_files(file))
    if st.selectbox('How many files?', ['single', 'all']) == 'single':
        file = st.text_input('Enter the name of the file or folder as seen above')
        dest = st.text_input('Enter existing or new destination file/folder')
        if st.button('Copy'):
            shutil.copy(file, dest)
            st.success('File copied!')
    else:
        st.info('This will copy all files in a folder to another folder')
        file = st.text_input('Enter the name of the folder')
        dest = st.text_input('Enter the name of the new or existing folder')
        if st.button('Copy'):
            shutil.copytree(file, dest)
            st.success('File copied!')


