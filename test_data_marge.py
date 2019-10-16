# -*- coding: utf-8 -*-
import os
import glob
import csv
import pandas as pd

# フォルダ中のパスを取得
DATA_PATH ="C:\\Users\owner\Desktop\python_lesson\data_port_f\\weather\\"
All_Files = glob.glob('{}*.csv'.format(DATA_PATH))
#print(All_Files)

list = []
for file in All_Files:
    list.append(pd.read_csv(file))
df = pd.concat(list, sort=False)
df.to_csv('{}1990-2018.csv'.format(DATA_PATH), encoding='utf_8',index=False)
