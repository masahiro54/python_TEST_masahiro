import numpy
import pandas
import datetime
import matplotlib.pyplot as plt

data = pandas.read_csv('C:\\Users\owner\Desktop\python_lesson\data_port_f\\1990-99.csv',index_col='date', parse_dates=['date'])

#matplotlib inline
start = data.index.searchsorted(datetime.datetime(1991, 1, 1))
end = data.index.searchsorted(datetime.datetime(1992, 1, 1))
data[start:end].plot()
print(start)
print(end)
plt.show()

start = data.index.searchsorted(datetime.datetime(1999, 1, 1))
end = data.index.searchsorted(datetime.datetime(1999, 12, 31))
data[start:end].plot()
#plt.show()
