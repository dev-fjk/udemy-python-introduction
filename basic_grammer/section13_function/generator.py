"""
ジェネレータ関数 for文などで回されるたびに値を1つ生成して返却する yield(イールド) 返却したい値
1つずつ値を生成して返す関係で listにappendするより見やすく、out of memory対策になる
シンプルな処理はジェネレータ式 ジェネレータ式だと読みずらくなってきたら関数にするのが良い
"""


def make_squares2(n):
    for j in range(1, n + 1):
        yield j ** 2


squares = make_squares2(10)
for i in squares:
    print(i)


def my_range(start, end, step):
    current_number = start
    while current_number < end:
        yield current_number
        current_number += step


for i in my_range(1, 10000, 0.1):
    print(i)
