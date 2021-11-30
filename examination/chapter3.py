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
