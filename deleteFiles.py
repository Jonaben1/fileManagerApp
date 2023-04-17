import streamlit as st
import os
from files import see_files
from send2trash import send2trash


def delete_files():
    st.header('Delete Files')
    st.warning('Becareful using this feature! Any action done cannot be reversed')
    st.info('For files inside a folder, separate the folder from the files using slash (/)')
    st.text('Your current directory contains')
    st.text(os.listdir())
    ch = st.selectbox('Do you want to see the files in a given folder?', ['No', 'Yes'])
    if ch == 'Yes':
        file = st.text_input('Enter the name of the folder')
        if file:
            st.text(see_files(file))
    file = st.text_input('Enter the file or folder you want to delete')
    op = st.selectbox('Select an option', ['temporary', 'permanent'])
    if op == 'temporary':
        if st.button('Delete'):
            send2trash(file)
            st.success('File sent to recycle bin!')
    else:
         if st.button('Delete'):
             os.unlink(file)
             st.success('File deleted!')

