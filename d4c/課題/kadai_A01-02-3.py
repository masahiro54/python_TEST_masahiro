# 必要なライブラリをインポートする
import sys
import datetime
# 判定対象となる西暦を標準入力の第２引数から取得する
year_char=sys.argv[1]
#12回ループを作成
x=0
for i in range(1,13):
    #月ごとの13日を変数に格納する。
    date_13 =  datetime.datetime(int(year_char), i, 13)
    #金曜日（4）の値のみ出力また、変数にカウント
    if date_13.weekday() == 4:
        print("{}年{}月13日は金曜日です。".format(year_char,str(i)))
        #カウントアップ
        x += 1

print("{}年には合計{}個の13日の金曜日があります。".format(year_char,str(x)))
