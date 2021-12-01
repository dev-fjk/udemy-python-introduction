list_a = ['dog', 'cat', 'tiger', 'horse', 'monkey']
for s in list_a[:]:
    if (len(s)) == 5:
        list_a.append(s)

print(list_a)

for i in range(0, 16, 4):
    print(i, end=',')


def hawold(age, list_w=[25]):
    list_w.append(age)
    return list_w


print(hawold(30))
print(hawold(38))
print(hawold(42))


def name(*args):
    print("参加者名：", args)


name('a', 'b')
name('a', 'b', 'c')

toshi_code = [(42, 'naga'), (41, 'saga'), (40, 'fuku'), (43, 'kuma')]
pref = toshi_code
pref.sort(key=lambda pref: pref[0])  # キーでソート
print(pref)  # [(40, 'fuku'), (41, 'saga'), (42, 'naga'), (43, 'kuma')]
pref.sort(key=lambda pref: pref[1])  # 値ソート
print(pref)  # [(40, 'fuku'), (41, 'saga'), (42, 'naga'), (43, 'kuma')]


def asai_kaisan(weight, height, sex, work):
    '体重、身長、性、職業を表示します'

    asai = weight, height, sex, work
    print(asai_kaisan.__doc__)  # docｓｔりんｇ
    print(asai)


aa = {'weight': 58.5, 'height': 170, 'sex': '女性', 'work': 'OL'}
asai_kaisan(**aa)  # 引数に辞書を設定する場合 **辞書名とする
