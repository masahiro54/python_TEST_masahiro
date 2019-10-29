import MeCab
m = MeCab.Tagger("-Ochasen")
print(m.parse("すもももももももものうち"))
print(m.parse("頑張れ！ベアーズ"))
