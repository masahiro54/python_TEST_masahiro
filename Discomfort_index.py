#インポート処理
import matplotlib.pyplot as plt
import pandas
import datetime
#変数の初期化
l_warm = []
l_hot = []
l_too_hot = []
year = []
l_warm_high=[]
l_hot_high =[]
l_too_hot_high =[]
l_h_t_h = []
#csvデータを変数に格納
data = pandas.read_csv('C:\\Users\owner\Desktop\python_lesson\data_port_f\\weather\\1990-2018.csv',index_col='date', parse_dates=['date'])
#ループ（年）
for i in range(30):
    #ループ（日）用の開始位置と終了位置を設定、
    start = data.index.searchsorted(datetime.datetime(2018-i, 1, 1))
    end = data.index.searchsorted(datetime.datetime(2019-i, 1, 1))
    t = data[start:end].values
    #ループ（日）用の初期化
    warm_count = 0
    hot_count = 0
    too_hot_count = 0
    leap = 0
    #リストyearに処理する「年」を格納していく。
    year.append(2018-i)
    #うるう年の判断
    if (2018-i)%400 == 0:
        leap = 366
    elif (2018-i)%100 == 0:
        leap = 365
    elif (2018-i)%4 == 0:
        leap = 366
    else:
        leap = 365
    #ループ（日）
    for d in range(leap):
        tmp = 0
        hum = 0
        disc = 0
        #温度と湿度をそれぞれ変数に格納
        tmp = t[d][0]
        hum = t[d][3]
        #不快指数の計算
        disc = round((0.81*tmp)+(0.01*hum)*((0.99*tmp)-14.3)+46.3,2)
        #if disc >= 65 and disc <= 70:#不快指数が心地いいレベル
        if disc >= 75 and disc < 80:
            warm_count += 1
        elif disc >= 80 and disc < 85:
            hot_count += 1
        elif disc >= 85:
            too_hot_count += 1
    #それぞれの変数に格納（リスト）
    l_h_t_h.append(hot_count + too_hot_count) #不快指数上位の日数
    l_warm.append(warm_count) #75~79の日数
    l_hot.append(hot_count) #80~84の日数
    l_too_hot.append(too_hot_count) #85~の日数
    #テキストを表示する高さを決めるための変数
    l_warm_high.append(warm_count)  #75~79の高さ
    l_hot_high.append(warm_count + hot_count) #80~84の高さ
    l_too_hot_high.append(warm_count + hot_count + too_hot_count) #85~の高さ

#テキストの表示
for x, y, z in zip(year, l_warm_high,l_too_hot_high):
    plt.text(x, round(y/2,0), str(y), ha='center', va='bottom')
    plt.text(x,90,str(x)+"\ntotal\n"+str(z))
for x, y, z in zip(year,l_hot_high,l_hot ):
    if z != 0:
        plt.text(x, y-round(z/2,0), z , ha='center', va='bottom')
if too_hot_count == 0:
    for x, y ,z in zip(year, l_too_hot_high,l_too_hot):
        if z != 0:
            plt.text(x, y-round(z/2,0), z, ha='center', va='bottom')
plt.title("hotday 1989 - 2018")
#不快指数75以上の日を色分けして積み上げ棒グラフにする。
p1 = plt.bar(year,l_warm,color="orange")
p2 = plt.bar(year,l_hot,color="#FF5B70",bottom=l_warm)
p3 = plt.bar(year,l_too_hot,color="red",bottom=l_hot_high,align="center")
#表示する範囲を指定
plt.plot(1989, 100)
#グラフの表示
plt.show()
#不快指数80以上の日をまとめて棒グラフで表示する。
for x, y in zip(year,l_h_t_h):
    plt.text(x,39,str(x)+"\n"+str(y),ha='center', va='bottom')
p4 = plt.bar(year,l_h_t_h)
#グラフの表示
plt.show()
