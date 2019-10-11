# 必要なライブラリをインポートする
import csv
# 判定対象となる西暦を標準入力の第２引数から取得する
with open('C:\\Users\owner\Desktop\python_lesson\d4c\data\order_report.csv', 'r') as rf:
    line = rf.readline()
    reader = csv.reader(rf)
    #値の初期化
    t1_sum = 0
    t2_sum = 0
    t3_sum = 0
    t4_sum = 0
    t5_sum = 0
    t6_sum = 0
    t7_sum = 0
    #味コードごとに集計
    for data in reader:
            if data[2] == "T1":
                t1_sum += int(data[3])
            elif data[2] == "T2":
                t2_sum += int(data[3])
            elif data[2] == "T3":
                t3_sum += int(data[3])
            elif data[2] == "T4":
                t4_sum += int(data[3])
            elif data[2] == "T5":
                t5_sum += int(data[3])
            elif data[2] == "T6":
                t6_sum += int(data[3])
            elif data[2] == "T7":
                t7_sum += int(data[3])
#出力
print("T1:"+str(t1_sum))
print("T2:"+str(t2_sum))
print("T3:"+str(t3_sum))
print("T4:"+str(t4_sum))
print("T5:"+str(t5_sum))
print("T6:"+str(t6_sum))
print("T7:"+str(t7_sum))
