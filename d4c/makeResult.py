# 必要なライブラリをインポートする
import csv
from module import myYear
# 判定対象となる西暦を標準入力の第２引数から取得する(第2引数？第1じゃなくて？)
with open('C:\\Users\owner\Desktop\python_lesson\d4c\data\A01-02.1.気象庁データ.csv', 'r') as rf:
    # 結果を出力する
    with open('C:\\Users\owner\Desktop\python_lesson\d4c\output\makeresult_2.txt', 'w') as wf:
        # 1行目（項目行）だけ読み込む
        line = rf.readline()
        # 項目名を先に書き出しておく
        wf.write( '"Year","Daily Sunshine Hours"\n' )
        reader = csv.reader(rf)
        for data in reader: # data[0]に1列目、data[1]に2列目…が格納される
            year=myYear.myYear(data[0])
            if year.isTaisho() == True:
                # うるう年フラグと年間総日数を取得し、１日あたりの日照時間を計算します
                flg=year.getLeapFlg()
                days=year.getCountDays()
                dailySun=float(data[1])/days
                # 元々のデータにダミー列（値は全て1）を加えカンマ区切りで出力
                # 1列目（西暦）はダブルクォーテーションで囲む
                wf.write( '"' + str(data[0]) + '",' + str(dailySun) + "\n" )
