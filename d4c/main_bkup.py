# 必要なライブラリをインポートする
import sys
# 判定対象となる西暦を標準入力の第２引数から取得する(第2引数？第1じゃなくて？)
year_char=sys.argv[1]
#クラスの定義
class myYear:
    #---------------------------------------------------------------------------------
    #メソッド定義(init)
    #---------------------------------------------------------------------------------
    def __init__(self,init_year_char):
        #print("デバッグ 引数__init__⇒"+init_year_char)
        self.year = ''
        self.year = self.setYear(init_year_char)
        #print(self.year)
    #---------------------------------------------------------------------------------
    #メソッド①
    #---------------------------------------------------------------------------------
    def setYear(self,char):
        #print("デバッグ 引数(setYear)⇒"+char)
        year_char_return='' #変数の初期化
        for counter in range(min(4,len(char))):  #ループの回数は4回もしくは文字列の長さ分のいずれか。短いほうを優先。
            year_char_one = year_char[counter] #変数【カウンタ】文字目の1文字を取得。
            #取得文字列が数字か否かで条件分岐。
            if str.isdecimal(year_char_one) == True:
                year_char_return=year_char_return+year_char_one
            else:
                break
            #counter += 1
        #print("デバッグ 編集後年⇒"+year_char_return)
        return year_char_return
        #print("デバッグ 編集処理終了")

    #--------------------------------------------------------------------------------
    #メソッド②
    #---------------------------------------------------------------------------------
    def isLeap(self):
       print("デバッグ isLeapスタート")
       try:
                 print("tey分後"+str(self.year))
                 chyear=int(self.year)
                 #print("デバッグ isLeap chyear⇒"+chyear)
                 # 西暦の値を見てうるう年か否かを判定する
                 if chyear % 400 == 0:
                     leap = True
                 elif chyear % 100 == 0:
                     leap = False
                 elif chyear % 4 == 0:
                     leap = True
                 else:
                     leap = False
                 return leap
       except:
                 #print(sys.exc_info())
                 return'Error: Input Christian.'
    #---------------------------------------------------------------------------------
    # extractYear を利用して year_char から西暦部分を抽出し、year_char_selectedにセット
    #year_char_selected=extractYear(year_char)
    ## checkLeap を利用して year_char_selected のうるう年判定を行い、結果をresultにセット
    #result = checkLeap(year_char_selected)
    ## result の中身を標準出力に
    #print(result)
    # うるう年判定処理をして結果を1（うるう年）/0（非うるう年）で返すメソッドを定義
    def getLeapFlg(self):
        leap = self.isLeap()
        dict = {True:1,False:0}
        return dict[leap]
    # 1年の総日数を返すメソッドを定義
    def getCountDays(self):
        leap = self.isLeap()
        dict = {True:366,False:365}
        return dict[leap]
    # 元号が大正かを判定をするメソッドを定義
    def isTaisho(self):
        try:
            # 整数化して self.year にセット。
            chYear=int(self.year)
            # 1912年～1926年ならば True を返し、そうでなければ False を返す
            if chYear >= 1912 and chYear <= 1926:
                taisho = True
            else:
                taisho = False
            return taisho
        except:
            return 'Error: Input Christian.'
#year=myYear()
year=myYear(year_char)
#year.setYear(year_char)
# うるう年か否か（True or False)
result=year.isLeap()
print("うるう年かどうか？："+str(result))
# うるう年か否か（1 or 0）
result=year.getLeapFlg()
print("うるう年かどうか？："+str(result))
# １年の総日数
result=year.getCountDays()
print("日数："+str(result))
# 大正か否か（True or False）
result=year.isTaisho()
print("大正？："+str(result))
