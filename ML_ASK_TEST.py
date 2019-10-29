#必要ライブラリをインポート
from mlask import MLAsk
#ファイルのオープン
file_data = open("C:\\Users\\owner\\Desktop\\サラリーマン川柳.txt","r",encoding="utf-8")
#※上記のデータは上述のＨＰより対象の川柳部分のみ張り付けただけのテキストファイルです。
emotion_analyzer = MLAsk()
#初期化
senryu =[]
positive_count = 0
negative_count = 0
neutral_count = 0
exception_count = 0
for line in file_data:
    #改行コードを削除して、感情分析を行います。
    emotion_senryu = emotion_analyzer.analyze(line.replace("\n",""))
    #orientationが設定されない場合があるので、try exceptで囲っています。
    try:
        if  "POSITIVE" in emotion_senryu['orientation']:
            positive_count += 1
            #print("POSITIVE") ←デバッグ用です。
            #print(line)
        elif "NEGATIVE" in emotion_senryu['orientation'] :
            negative_count += 1
            #print("NEGATIVE")
            #print(line)
        else:
            neutral_count += 1
    #判定不能の場合はexception_countに割り振ります。
    except:
        exception_count += 1
        if exception_count < 9:
            print(emotion_senryu)
#トータルの件数
print("ネガティブ：" + str(negative_count))
print("ポジティブ：" + str(positive_count))
print("ニュートラル：" + str(neutral_count))
print("例外："+str(exception_count))
