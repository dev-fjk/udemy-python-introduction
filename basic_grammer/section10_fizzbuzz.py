"""Fizz Buzz
1から、n回まで繰り返し
・3の倍数はFizz
・5の倍数でBuzz
・15の倍数でFizz Buzz
・それ以外は数字
を出力する
"""

# 普通の
for i in range(1, 101):
    if i % 15 == 0:
        print('Fizz Buzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)

# pass = continue
for i in range(1, 101):
    message = ''
    if i % 3 == 0:
        message += 'Fizz'
    if i % 5 == 0:
        message += 'Buzz'

    # end=文字列で改行しないことができる
    # messageが空文字でない場合は messageを 空文字の場合は数字を出力する
    print(message or i, end='　')

# 内包表記を使った例
# trueは 1 , falseは0にできる 文字列に0を掛けると空文字扱いになることを利用したテク
fizz_buzz_list = ['Fizz' * (num % 3 == 0) + 'Buzz' * (num % 5 == 0)
                  or str(num) for num in range(1, 101)]
result = ''.join(fizz_buzz_list)
print(fizz_buzz_list)
