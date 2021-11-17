names = ['田中', '佐藤']

if '田中' in names:
    print('in tanaka')
else:
    print('else')
print('処理終了')

color = 'red'
if color == 'red':
    print('赤です')
elif color == 'blue':
    print('青です')
else:
    print('else')

# javaとの対照表
# && = and
# || = or
# != = not
# in = contains

# 空文字などを除きオブジェクト単体を渡してもtrueとなるので注意(逆に言うとnull/空チェック頑張らなくていい)
numbers = [1, 2]
if numbers:
    print(numbers)
else:
    print('空要素です')
