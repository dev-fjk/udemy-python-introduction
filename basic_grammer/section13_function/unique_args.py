# デフォルト引数
def hello(name='匿名'):
    print(name)


hello()
hello('fjk')


# 必須引数とデフォルト引数の混在 デフォルト引数は後に定義すること
def hello2(text, name='匿名'):
    print(text, name)


# 位置引数とキーワード引数(引数名=値)
# デフォルト引数を持つ変数に対してのみキーワード引数で指定するのが慣例
hello2('こんにちは')
hello2(text='こんにちは')
hello2('こんにちは', 'fjk')
hello2(text='こんにちは', name='fjk')


# 可変長引数 *引数で位置引数をタプルでまとめられる
def hello3(*args):
    print(args)

    for arg in args:
        print(arg)


hello3('a', 'b', 'c')


# 可変長引数 **引数でキーワード引数を辞書としてまとめられる
def hello4(*args, **kwargs):
    print(args, kwargs)


hello4('a', 'b', 'c', a='1', b=2, c=3)


# デフォルト値を持つ引数のの直前に*を引数で付与することで キーワード引数での起動を強制できる
def hello5(text, *, name='fjk'):
    print(text, name)


hello5('こんにちは')
# hello5('こんにちは','太郎') 　エラーになる
hello5('こんにちは', name='太郎')
