#!/usr/bin/python
# This script replaces all occurrences of sage, Sage, and SAGE to femhub, Femhub, and FEMhub respectively except the file extensions declared

import re, os
from os.path import join, getsize

# The content of the files with these extension will not be fixed
EXT_NOT_TO_FIX = ['.jpg', '.JPG', '.png', '.PNG', 'gif', 'GIF']

# SEARCH_REPLACE = { 'search_this':'replace_with'}
SEARCH_REPLACE = { 'sage':'femhub', 'Sage':'Femhub', 'SAGE':'FEMHUB' }

# Where to fix
fix_there = '/home/all/sage_notebook/src'

def search_and_replace(str):
    for key, value in SEARCH_REPLACE.items():
        str = re.sub(key, value, str)
    return str

# Fix file content
def fix_file_content(filename):
    f = open(filename)
    str = f.read()
    f.close()

    str = search_and_replace(str)

    f = open(filename, "w")
    f.write(str)
    f.close

# Fix file name (use with caution)
def fix_file_name(dir, filename):
    new_file_name = search_and_replace(filename)
    os.rename(os.path.join(root, filename), os.path.join(root, new_file_name))

if __name__ == "__main__":
    for root, dirs, files in os.walk(fix_there):
        for f in files:
            name, ext = os.path.splitext(f)
            if (ext not in EXT_TO_FIX):
                fix_file_content(os.path.join(root, f))
                fix_file_name(root, f)
                #print os.path.join(root, f)

    for root, dirs, files in os.walk(fix_there, topdown='False'):
        for d in dirs:
            fix_file_name(root, f)
