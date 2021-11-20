# 内包表記
numbers = [1, 5, 6, 11, 3, 5, 7, 3]

# numberの各要素を2乗してsquaresに格納
squares = [num ** 2 for num in numbers]
print(squares)

words = ['python', 'django', 'tkinter']
upper_words = [word.upper() for word in words]
print(upper_words)

# forは左側から評価される
one_words = [char for word in words for char in word]
print(one_words)

# 偶数のリスト
# 1~10までのfor文の結果 xが 2で割り切れる場合にリストの要素として追加
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# Noneが5つ設定されたリストを5件保持したリストを作成
table = [[None for x in range(5)] for y in range(5)]
print(table)

# key,valueの逆転
score = {'math': 80, 'eng': 20}
new_score = {value: key for key, value in score.items()}
print(new_score)

# ジェネレータ forループを使えば値を取り出せる
numbers = [1, 5, 6, 11, 3, 5, 7, 3]
square_gen = (num ** 2 for num in numbers)
for num in square_gen:
    print(num)
