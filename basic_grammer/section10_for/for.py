# for 変数 in コレクション:
names = ['佐藤', '鈴木', '田中']
for name in names:
    print(name)

my_tuple = (1, 2, 3)
for i in my_tuple:
    print(i)

# 文字列の1文字ずつの切り出し
for char in 'HelloWorld':
    print(char)

# 入れ子
for name in names:
    for char in name:
        print(char)

# dictionary
# forにそのまま辞書を渡した場合keyが順番に出力される
band_members = {'ボーカル': '佐藤', 'ギター': '鈴木'}
for val in band_members:
    print(val)

for val in band_members:
    # 辞書なのでキーを使用してvalueを取り出す
    name = band_members[val]
    message = '{0}は、{1}さん'.format(val, name)
    print(message)

# 変数は複数取れる
for key, val in band_members.items():
    print(key + 'は' + val + 'さん')
for val in band_members.values():
    print(val)

# アンタック代入(左辺に複数の変数を書いて代入すること)
my_tuple = (1, 2)
a, b = my_tuple
print(a, b)

# 入れ子のリスト
items = [
    ['ボーカル', '佐藤'],
    ['ギター', '鈴木']
]

for part, name in items:
    print(part, name)

# ループ回数の指定 組み込み関数 rangeを使用 rangeはループする回数
for i in range(100):
    print(i)

# 1から100まで
numbers = []
for i in range(1, 101):
    print(i)
    numbers.append(i)

print(numbers)

# 2飛ばし(1,3,5,7~)
for i in range(1, 101, 2):
    print(i)

# rangeはjavaのitemStreamのイメージ ループ毎に値を生成する(out of memory防止)
my_list = list(range(1, 101))
print(my_list)

# 便利なforループ　他言語ライクな書き方
names = ['佐藤', '鈴木', '田中']
index = 0
for name in names:
    message = '{0}は、{1}さん'.format(index, name)
    print(message)
    index += 1

# forの便利な関数
# enumerate 引数に渡したコレクションの indexを一緒に返す
names = ['佐藤', '鈴木', '田中']
for index, name in enumerate(names):
    message = '{0}は、{1}さん'.format(index, name)
    print(message)

# zip 並列で要素を取り出す
# 要素数が異なる場合 少ない方にループ回数が合わせられるので注意
foods = ['納豆', 'ヨーグルト', 'チャーハン']
juices = ['コーラ', 'コーヒー', 'カフェラテ']
for food, juice in zip(foods, juices):
    print(food, juice)

# for else
# elseは直観的でないので使わない方がいいという意見もあり
names = ['佐藤一郎', '鈴木次郎', '田中三郎']
for name in names:
    if name.endswith('三郎'):
        print('居ました')
        break
else:
    # breakしなければ入る
    print('居ませんでした')
