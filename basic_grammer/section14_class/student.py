# クラスだけキャメルケースで命名する(javaと一緒)
class Student:
    # __init__ コンストラクタ / self == javaのthisと同じようなイメージ
    def __init__(self, name):
        self.name = name
        self.score = {}

    #  受け取った教科名と点数を辞書に保存する
    def add_score(self, subject_name, point):
        self.score[subject_name] = point

    # 指定された教科の点数を返す
    def get_score(self, subject_name):
        return self.score.get(subject_name, 'その教科の点数はまだ登録されていません')


# インスタンス作成

members = {'fjk': Student('fjk'), 'tanaka': Student('tanaka')}

print(members['fjk'].add_score('math', 50))
print(members['fjk'].get_score('math'))
print(members['fjk'].get_score('english'))

print(members['tanaka'].add_score('english', 100))
print(members['tanaka'].get_score('math'))
print(members['tanaka'].get_score('english'))
