# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import struct
from datetime import datetime
import glob
import errno
import numpy as np
import pandas as pd
#path = 'C:/Users/ceo/Desktop/SCubeBinFileView/20200519/04/CM91005013_202005190500.bin'
g_prevTime = 0
g_dataList = []
global dts, ms, gapTime, valueFDD
txtfilename = 'C:/Users/ceo/Desktop/SCubeBinFileView/ACC/allinone.csv'
fw = open(txtfilename, mode='wt', encoding='utf-8')
try:
    #data = open("C:/Users/ceo/Desktop/SCubeBinFileView/20200519/03/CM91005013_202005190305.bin", "rb+").read(8)
    #path = 'C:/Users/ceo/Desktop/SCubeBinFileView/20200519/04/*.bin'
    path = 'C:/Users/ceo/Desktop/SCubeBinFileView/ACC/**/**/*.bin'
    files = glob.glob(path)
    #files = glob.glob(all_bin, recursive = True) # take all bin file in the files
    bin_files = []
    for name in files:
        if name.endswith(".bin"):
            bin_files.append(name)
            with open(name, 'rb') as f:
                while True:
                    dateT = f.read(8)
                    if dateT == b'': break
                    dateTD = int.from_bytes(dateT, 'big')
                    if g_prevTime == 0:
                        g_prevTime = dateTD
                    gapTime = dateTD - g_prevTime
                    g_prevTime = dateTD
                    #print(dateTD)

                    dts, ms = divmod(dateTD, 1000)
                    valueF = f.read(4)
                    valueFD = valueF[::-1]
                    [valueFDD] = struct.unpack('f', valueFD)
                    g_dataList.append(valueFDD)
                    ts = datetime.fromtimestamp(float(int(dts))).strftime('%Y-%m-%d %H:%M:%S')
                    print('{}.{:03d},{},{:.8f}'.format(ts, ms, gapTime, valueFDD))

                    #with open(txtfilename, 'a', newline='\n') as f:

                    data = '{}.{:03d},{},{:.8f}'.format(ts, ms, gapTime, valueFDD)

                    datas = pd.DataFrame([[ts, ms, gapTime, valueFDD]], columns=['ts', 'ms', 'gapTime', 'valueFDD'])

                    #print(datas)
                    with open(txtfilename, 'a', newline='\n') as fil:
                        datas.to_csv(fil, index=False, header=False)
                    #datas.to_csv(txtfilename, header=False)

                    #print(ts)

                f.close()
                fw.close()


except Exception as e:
    print(e)

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)







