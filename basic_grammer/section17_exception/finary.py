"""
    with open('resources/hello.txt', 'x', encoding='utf-8') as file:
        file.write('hello')
"""

try:
    file = open('resources/hello.txt', 'x', encoding='utf-8')
except FileExistsError:
    print('ファイルが既に存在しています')
else:
    # エラーがない場合実行される処理
    file.write('hello')
finally:
    file.close()
