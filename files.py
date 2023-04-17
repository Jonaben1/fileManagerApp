import os


def see_files(file):
    '''List all files in a folder'''
    for item in os.scandir(file):
        if item.is_dir():
            return item
