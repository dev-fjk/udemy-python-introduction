"""
ラムダ式
Javaと同じくコレクション操作などに適した無名関数を使用して処理する
シンプルな処理ならlambda / 複雑な処理ならdef関数が良い
lambda 引数 : 返す値
"""


# 通常の関数とリストの場合
# 文字列の最後の文字を基準に渡す
def my_sort(string):
    return string[-1]


# リストの復習
my_list = ['python', 'django', 'tkinter', 'kivy', 'requests']
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.sort(key=my_sort)
print(my_list)

# my_sort関数を呼び出した際と同じ結果が得られる
my_list.sort(key=lambda info: info[-1])
print(my_list)

# map / filter  javaと同じ感じ
# pythonの場合は内包表記で代替できるのであまり使わないらしい
numbers = [1, 2, 3, 4, 5]

# 各要素を2乗して出力(無名関数内で各要素を加工した結果を返す)
for i in map(lambda num: num ** 2, numbers):
    print(i)
# 偶数のみ出力(関数の結果がtrueの場合だけ返す)
for i in filter(lambda num: num % 2 == 0, numbers):
    print(i)
