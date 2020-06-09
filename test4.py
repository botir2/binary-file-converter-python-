# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import glob, os

path = 'C:/Users/ceo/Desktop/SCubeBinFileView/ACC/**/**/*.bin'
files = glob.glob(path)
for name in files:
    if name.endswith(".bin"):
        with open(name, 'rb') as f:
            print(f)