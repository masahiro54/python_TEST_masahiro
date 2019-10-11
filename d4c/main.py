# 必要なライブラリをインポートする
import sys
from module import myYear
# 判定対象となる西暦を標準入力の第２引数から取得する(第2引数？第1じゃなくて？)
year_char=sys.argv[1]
year=myYear.myYear(year_char)
#year.setYear(year_char)
# うるう年か否か（True or False)
#result=year.isLeap()
#print("うるう年かどうか？："+str(result))
# うるう年か否か（1 or 0）
#result=year.getLeapFlg()
#print("うるう年かどうか？："+str(result))
# １年の総日数
#result=year.getCountDays()
#print("日数："+str(result))
# 大正か否か（True or False）
#result=year.isTaisho()
#print("大正？："+str(result))
#課題①解答
print(year.getWareki())
