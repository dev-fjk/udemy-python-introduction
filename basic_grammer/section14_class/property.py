class Person:
    def __init__(self, name):
        self.name = name  # name.setterのnameメソッドが起動され 代入値が_nameに代入される

    # .name で要素に単純にアクセスした場合このメソッドが起動される
    @property
    def name(self):
        return self._name

    # 関数名の属性に代入が行われた際に実行される
    @name.setter
    def name(self, value):
        if not value:
            value = '名無しの権兵衛'
        # _をつけることで無限ループを回避(nameに代入すると無限にセッターが起動されるため)
        self._name = value


person = Person('')
print(person.name)  # 名無しの権兵衛
