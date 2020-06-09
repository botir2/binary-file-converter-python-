import numpy as np
import pandas as pd
import glob, os
import csv


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def remove2rows(csv_file):
    data = pd.read_csv(csv_file)
    len_of_file = file_len('C:/Users/ceo/Desktop/SCubeBinFileView/CM31000001.csv')
    data = data.iloc[np.arange(0,len_of_file,500)]
    data.to_csv(csv_file, header=None, index=False)

if __name__ == '__main__':
    df = pd.read_csv('C:/Users/ceo/Desktop/SCubeBinFileView/CM31000001.csv')

    remove2rows('C:/Users/ceo/Desktop/SCubeBinFileView/CM31000001.csv')
    print(df.head())