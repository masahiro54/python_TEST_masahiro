import numpy as np

arr = np.arange(10)
print(arr)

# 変数arrの要素の内3, 4, 5だけを出力してください
print(arr[0:6])

# 変数arrの要素の内3, 4, 5を24に変更してください
arr[3:6] = 24
print(arr)



arr2 = np.array([[1, 2, 3], [4, 5, 12], [15, 20, 22]])

# arrの行の合計値を求め、問題文に指定の1次元配列を返してください
print(arr2.sum())
