# 必要なライブラリをインポートする
import csv
# ファイルから１行ずつデータを読み込む
with open('C:\\Users\owner\Desktop\python_lesson\d4c\data\A01-02.1.気象庁データ.csv', 'r') as rf:
    reader = csv.reader(rf)
    for data in reader:
        print(data[1])
