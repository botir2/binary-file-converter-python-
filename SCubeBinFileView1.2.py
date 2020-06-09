# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import struct
import glob
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#print("Matplotlib version", matplotlib.__version__)
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'



binfilename = 'C:/Users/ceo/Desktop/SCubeBinFileView/CM91005013_202005200100.bin'
#path = 'C:/Users/ceo/Desktop/SCubeBinFileView/20200519/04/*.bin'

'''
files = glob.glob(path)
for name in files:
   if name.endswith(".bin"):
           binfilename = name
'''

fname, ext = binfilename.split('.')
print(binfilename)
txtfilename = fname + '.csv'

g_prevTime = 0
g_dataList = []


f = open(binfilename, 'rb')

fw = open(txtfilename, mode='wt', encoding='utf-8')
while True:
        dateT = f.read(8)
        if dateT == b'': break
        #print(dateT)
        dateTD = int.from_bytes(dateT, 'big')
        if g_prevTime == 0:
            g_prevTime = dateTD
        gapTime = dateTD - g_prevTime
        g_prevTime = dateTD

        #print(dateTD)
        dts, ms = divmod(dateTD, 1000)

        valueF = f.read(4)
        #print(valueF)
        valueFD = valueF[::-1]
        #print(valueFD)
        [valueFDD] = struct.unpack('f', valueFD)
        #print(valueFDD)
        g_dataList.append(valueFDD)

        ts = datetime.fromtimestamp(float(int(dts))).strftime('%Y-%m-%d %H:%M:%S')
        print('{}.{:03d},{},{:.8f}'.format(ts, ms, gapTime, valueFDD))

        # print(ms)
        # print('{}'.format(valueFDD))
        fw.write('{}.{:03d},{},{:.8f}\n'.format(ts, ms, gapTime, valueFDD))
f.close()
fw.close()
# print(g_dataList)

npDataArr = np.array(g_dataList)
sR = pd.Series(npDataArr, )
sR.plot()
# ax1 = npDataArr.plot(color="k", marker="", linestyle="--")
