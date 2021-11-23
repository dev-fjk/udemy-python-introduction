"""
特殊メソッド init,lenなど ある状況下で暗黙的に起動されるメソッド
"""


class A:
    def __init__(self):
        self.name = '属性'
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.count
        if current > 10:
            raise StopIteration
        self.count += 1
        return current

    # toString枠
    def __str__(self):
        result = str(self.name) + '\n' + str(self.count)
        return result


# for文実行時は暗黙的に__iter__と__nextメソッドが起動されている
a = A()
for count in a:
    print(count)  # 10を超えた段階でループストップ

print(a)
