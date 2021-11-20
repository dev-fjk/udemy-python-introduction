# pythonはオーバーロードできないみたい
def hello():
    print('こんにちは')


def hello2(name):
    message = '{0}さん、こんにちは'.format(name)
    print(message)


hello()
hello2('太郎')


# 6文字以上ならtrueを返却
def check_name(name):
    return len(name) > 6


check_result = check_name('あいうえおいう')
print('登録完了' if check_result else '名前が短いです')


# デフォルト値にmutableな値を持たせると同じインスタンスを参照し続けるため複数回起動されると結果が変わる
def create_int_list(numbers=[]):
    for i in range(10):
        numbers.append(i)
    return numbers


# 起動される度に格納される数が増えていってしまう例
result_numbers = create_int_list()
print(result_numbers)
result_numbers2 = create_int_list()
print(result_numbers2)
result_numbers3 = create_int_list()
print(result_numbers3)


# 対策
def create_int_list2(numbers=None):
    # is は同一インスタンスかチェック
    # Noneはアプリケーションで常に同じインスタンスを使うためNone だけ isでチェックする
    if numbers is None:
        numbers = []
    for i in range(10):
        numbers.append(i)
    return numbers


result_numbers = create_int_list2()
print(result_numbers)
result_numbers2 = create_int_list2()
print(result_numbers2)
result_numbers3 = create_int_list2()
print(result_numbers3)
