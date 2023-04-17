import streamlit as st
from copyFiles import copy_files
from renameFiles import rename_files
from deleteFiles import delete_files
from moveFiles import move_files


def main():
    st.sidebar.header('File Manager App')
    st.header('File Manager App')
    op = st.sidebar.selectbox('Select your option', ['copy', 'move', 'rename', 'delete'])

    if op == 'copy':
        copy_files()
    elif op == 'move':
        move_files()
    elif op == 'rename':
        rename_files()
    else:
        delete_files()


if __name__ == '__main__':
    main()
