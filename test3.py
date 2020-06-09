# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import struct
from datetime import datetime
import pandas as pd
import numpy as np
import glob


import os

def getfilenames(path):
    ftype = path.split(".")[-1]
    folder = path.split("*")[0]
    return [i for i in os.listdir(folder) if ftype in i.split(".")[-1]]

print(getfilenames(sys.argv[1]))