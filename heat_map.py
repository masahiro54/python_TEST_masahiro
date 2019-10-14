import seaborn
import matplotlib.pyplot as plt
import pandas
import datetime
import matplotlib
import numpy as np
#%matplotlib inline

tmp = []
y = []
y_name = []
data = pandas.read_csv('C:\\Users\owner\Desktop\python_lesson\data_port_f\\test_data.csv',index_col='date', parse_dates=['date'])
for i in range(28):
    start = data.index.searchsorted(datetime.datetime(2018-i, 1, 1))
    end = data.index.searchsorted(datetime.datetime(2019-i, 1, 1))
    t = data[start:end].values

    tmp.append([t[i][3] for i in range(365)])#うるう年面倒なので1日データが欠損させます。
    if i%2 == 1:
        y.append(i)
        y_name.append(str(2018-i))
    #if end == data.index.searchsorted(datetime.datetime(2018, 1, 1)):
    #    print("通ってること")
    #    print(tmp)

#ヒートマップの成型
plt.figure(figsize=(200,200))
ax = seaborn.heatmap(tmp,vmin=0, vmax=39,center=20)
plt.xticks(np.arange(0, 364, 10))
plt.yticks(y,y_name)
plt.title('cho-hu heatmap(1990-2018)')
plt.xlabel('day(0-364)')
plt.ylabel('year（2018－1990）')
plt.show()
