class A:
    def __init__(self):
        # インスタンス変数(属性)
        self.number = 10


class B:
    # static(クラス)属性
    number = 10


print(B.number)
a = A()
a2 = A()
print(a.number)

a.number = 100
print(a.number)  # 100
print(a2.number)  # 10

b1 = B()
b2 = B()
B.number = 100

b1.number = 2
# クラス属性とインスタンス属性で同名の物がある場合 インスタンス属性が優先される
print(B.number, b1.number, b2.number)  # 100 2 100
