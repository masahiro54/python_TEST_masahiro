# 必要なライブラリをインポートする
import csv
# 判定対象となる西暦を標準入力の第２引数から取得する
with open('C:\\Users\owner\Desktop\python_lesson\d4c\data\order_report.csv', 'r') as rf:
    # 結果を出力する
    with open('C:\\Users\owner\Desktop\python_lesson\d4c\output\order_report_update_taste.csv', 'w') as wf:
        # 1行目（項目行）だけ読み込む
        line = rf.readline()
        # 項目名を先に書き出しておく
        wf.write( 'Order_ID,Date_YMD,Taste,Amount\n' )
        reader = csv.reader(rf)
        for data in reader: # data[0]に1列目、data[1]に2列目…が格納される
            #変数初期化
            taste = ""
            if data[2] == "T1":
                taste = "Kinako-Milk"
            elif data[2] == "T2":
                taste = "Oolong-Milk"
            elif data[2] == "T3":
                taste = "Green-Milk"
            elif data[2] == "T4":
                taste = "Black-Milk"
            elif data[2] == "T5":
                taste = "Green"
            elif data[2] == "T6":
                taste = "Black"
            elif data[2] == "T7":
                taste = "Special"
            #出力
            wf.write( str(data[0]) + ',' + str(data[1])+ ","+str(taste) + ","+str(data[3])+ "\n" )
