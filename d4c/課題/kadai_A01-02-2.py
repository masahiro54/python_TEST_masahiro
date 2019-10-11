# 必要なライブラリをインポートする
import sys
# 判定対象となる西暦を標準入力の第２引数から取得する
year_char=sys.argv[1]
#パラメータが整数であるかを確認
if str.isdecimal(year_char) == True:
    int_year = int(year_char)
    #2000以上の値が入力されているかを確認
    if int_year >= 2000:
        #夏のオリンピックの周期であれば出力（2000,2004,2008・・・・）
        if (int_year-2000)%4 == 0:
            print(year_char+"は夏のオリンピック開催年です。")
        #冬のオリンピックの周期であれば出力（2002,2006,2010・・・・）
        elif (int_year-2002)%4 == 0:
            print(year_char+"は冬のオリンピック開催年です。")
        else:
            print(year_char+"オリンピックの開催年ではありません。")
    else:
        print ("2000以上の値を入力してください" )
else:
    print( "値が整数ではありません。")
