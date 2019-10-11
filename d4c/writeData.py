# 必要なライブラリをインポートする
import sys
from module import myYear
# 判定対象となる西暦を標準入力の第２引数から取得する(第2引数？第1じゃなくて？)
year_char=sys.argv[1]
year=myYear.myYear(year_char)
with open('C:\\Users\owner\Desktop\python_lesson\d4c\output/outputSample.txt', 'w') as wf:
#year.setYear(year_char)
# うるう年か否か（True or False)
  result=year.isLeap()
  wf.write("うるう年かどうか？："+str(result)+"\n")
  # うるう年か否か（1 or 0）
  result=year.getLeapFlg()
  wf.write("うるう年かどうか？："+str(result)+"\n")
  # １年の総日数
  result=year.getCountDays()
  wf.write("日数："+str(result)+"\n")
  # 大正か否か（True or False）
  result=year.isTaisho()
  wf.write("大正？："+str(result)+"\n")
