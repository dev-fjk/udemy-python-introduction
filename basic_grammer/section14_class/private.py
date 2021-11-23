"""
名前の前に_をつけることでprivate変数扱いとする慣習(_value)
ただし javaと異なり外部から書き換え自体は可能

__value とアンダースコアを2つ繋げると外部からアクセスできなくなる(名前の衝突防止)
ただし インスタンス変数_クラス名__属性名とすればアクセス自体は出来てしまう
"""


class A:
    def __init__(self):
        # __ 変数とすることで子クラスなどでの意図しない要素書き換えを防げる
        self.__value = 1


class B(A):
    def __init__(self, name):
        super().__init__()
        self.name = name


class C(B):
    def __init__(self, name):
        super().__init__(name)
        self.value = 10


c = C('fjk')
print(c.value)
