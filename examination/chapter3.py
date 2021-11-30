s = 'kojima\naitou\nozaki'  # \nは改行コード扱い
print(s)
print(len(s))

s = r'kojima\naitou\nozaki'  # 文頭にrをつけることで raw文字列になるためバックスラッシュも文字列として認識される
print(s)
print(len(s))

s = 'doesn\'t'  # doesn't ('がエスケープされる)
print(s)
print(len(s))

print(19 / 3)  # 6.33333333　割った結果
print(19 // 3)  # 6.. // で商
print(19 % 3)  # 1　余り
print(3 ** 3)  # 27

print(7.0 / 2)  # 型混同時はfloat型になる　また割り算時は常にfloatになる

# 末尾のindexは-1となる
word = 'abcdefghijk'
print(word[0])  # a
print(word[5])  # f
print(word[2:8])  # cdefgh
print(word[-2])  # j
print(word[-2:])  # jk
print(word[: -2])  # abcdefghi

# >>> zei = 8 / 100　96.0
# >>> kakaku = 1200
# >>> 96.0
# >>> print(kakaku + _) #対話モード限定　_ は最後に表示した結果が代入 1296.0

price = 8.35551111
print(round(price, 3))  # 四捨五入

# tigerとhorseだけを表示
list_a = ['dog', 'cat', 'tiger', 'horse', 'monkey']
print(list_a[2:3])

list_a = ['dog', 'cat', 'tiger', 'horse', 'monkey']
list_a[1:3] = []  # catとtigerが削除される
print(list_a)

# tigerを出力
list_a = [[2, 4, 6], ['dog', 'cat', 'tiger']]
print(list_a[1][2])

# 300を出力する
list_a = [[2, 4, 6], ['dog', 'cat', 'tiger', [100, 200, 300]]]
print(list_a[1][3][2])

a, b = 0, 2
while b < 20:
    print(b, end=',')
    a, b = b, a + b

print(list(range(3, 6)))  # [3,4,5]
args = [3, 6]
print(list(range(*args)))  # *argsでrange()の始まりと終わりを指定 * でリストであることを宣言
