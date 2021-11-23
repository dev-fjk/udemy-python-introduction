def add(a, b):
    return a + b


# このモジュール(pythonファイル) を直接実行した際にのみ実行される処理
if __name__ == '__main__':
    result = add(1, 3)
    print(result)

# いかのように書いてしまうとimportしただけで処理が実行されてしまう
# result = add(1, 3)
# print(result)
