import calc as cal  # asで別名指定にできる　基本的にはつけなくてよい(慣習に従う)
from printer.execute_print import execute  # パッケージのimport


# from calc import add のように書くことで import先のクラスの要素を直でimportすることも可能
# ただし名前の重複に注意
# # from calc import * 非推奨 どの要素がどのクラスの要素か分かりづらくなるため

def add(a, b, c):
    return a + b + c


result = cal.add(1, 1)
print(result)

result2 = add(1, 1, 1)
print(result2)

execute('パッケージ')
