#!/usr/bin/env python3

# python script to get the absolute path of the parent of the given directory

import os

def parent_dir():
    current_dir = os.getcwd()
    print(f'Current directory:{current_dir}')
    # changes the directory
    os.chdir('..')
    new_current_dir = os.getcwd()
    print(f'New Current Directory:{new_current_dir}')
    return new_current_dir

print(parent_dir())
