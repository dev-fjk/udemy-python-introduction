# Pythonは定数不可らしいので注意 定数として扱いたい場合は 大文字スネークケース MY_CONSTANT_VALUE

# list
my_list = ['python', 'java', 'ruby']
print(type(my_list))
print(list('一文字ずつ分割されたリストになります'))

# 要素追加
my_list.append('php')  # 末尾に要素が追加
my_list.append(1)
print(my_list)

#  listもシーケンスの仲間
print(my_list[0])
# 逆順
print(my_list[::-1])
print(my_list[1:])

# 要素変換 listなら出来るが str や intは出来ない(immutableのため)
my_list[0] = 'javaScript'
print(my_list[0])

# tuple 基本はリストと同じように扱える
# 差異 初回の要素設定後に要素の追加不可(javaの配列に近い) 要素の書き換え不可(immutable)
# 利点 listよりパフォーマンスが良い / set(辞書)のキーに使用可
# () 省略可能
my_tuple = (1, True, False, 'Hello')
print(type(my_tuple))
my_tuple = 1, True, False, 'Hello'
print(type(my_tuple))

# 要素が一つの場合は末尾に,をつける
one_tuple = 'python',
print(type(one_tuple))
print(len(my_tuple))

# ======================= list 操作系のメソッド ======================= #
numbers = [1, 2, 3, 4, 5]
print(len(numbers))

# 全要素数字でないと例外出る系
print(sum(numbers))
print(max(numbers))
print(min(numbers))

# 場所指定して要素追加 (index, value)
numbers.insert(3, 10)
print(numbers)

# 要素の追加
numbers2 = [100, 101]
numbers.extend(numbers2)
print(numbers)  # numbersに直接要素追加

# +演算子の場合は新しいリストとして返す
numbers3 = numbers + numbers2
print(numbers3)

# 削除系
# pop 要素番号指定して削除 削除した値を戻り値で返す
del_start = numbers.pop(0)  # 先頭を消す
del_end = numbers.pop()  # 末尾を消す -1でもいい
print(del_start)
print(del_end)

# remove 値指定で削除
str_list = ['a', 'i', 'u']
str_list.remove('i')
print(str_list)

# 要素番号の取得
i = str_list.index('u')
print(i)

# 同じリストを別オブジェクトとして突っ込みたい場合のやり方
a_list = [1, 2, 3]

# NGな例
all_list = [a_list, a_list]
# 二番目に設定したa_listにも値が追加されてしまう
all_list[0].append(4)
print(all_list)  # [[1, 2, 3, 4], [1, 2, 3, 4]]

#  OKな例 copyメソッド
a_list = [1, 2, 3]
all_list = [a_list, a_list.copy()]
all_list[0].append(4)
print(all_list)  # [[1, 2, 3, 4], [1, 2, 3]]

#  OKな例　スライス
a_list = [1, 2, 3]
all_list = [a_list[:], a_list[:]]
all_list[0].append(4)
print(all_list)  # [[1, 2, 3, 4], [1, 2, 3]]

# ======================= list 操作系のメソッド ======================= #
