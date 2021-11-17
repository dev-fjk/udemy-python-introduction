# set
# 辞書をキーだけにしたようなもの javaと一緒 順序持たない 重複不可(listなどから変換する際は重複している値は1つを残して削除)
my_set = {1, 2, 3}
print(type(my_set))

# 空セットはset関数で使う
empty_set = set()

my_list = [1, 2, 3]
my_set = set(my_list)
print(my_set)

my_set.add(4)
print(my_set)

my_set.remove(4)
print(my_set)

mutable = {'list', 'dict', 'set'}
immutable = {'str', 'number', 'tuple'}
sequence = {'list', 'tuple', 'str'}

# set同士で共通する要素の取り出し
print(mutable & sequence)
print(mutable.intersection(sequence))

# setそれぞれで存在する要素を全て統合 重複は1件除き削除
print(mutable | sequence)
print(mutable.union(sequence))

# 要素の差分
print(immutable - sequence)
print(immutable.difference(sequence))

# 排他的論理和 重複しない要素の抽出
print(mutable ^ sequence)
print(mutable.symmetric_difference(sequence))
