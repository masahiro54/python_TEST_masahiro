import MeCab
from mlask import MLAsk
string="近年では、親愛の情を込めて友人、知人や親族にも贈るお歳暮へと少しずつ変化してきているようです。"
m = MeCab.Tagger("-Ochasen")
print(m.parse(string))
emotion_analyzer = MLAsk()
#emotion_analyzer.analyze(string)
print(emotion_analyzer.analyze(string))
