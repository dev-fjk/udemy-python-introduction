# 辞書 Mapに近い
# キーは immutableでないといけない　(str,int, tuple)
# Mapと同じく辞書の重複は不可(上書きされる)
score = {'math': 80, 'science': 50}
print(type(score))
print(score.get('math'))

# 空辞書
empty = {}
empty2 = dict()

# dict型への変換
names = [['佐藤', '太郎'], ['田中', '次郎']]
name_dict = dict(names)
print(name_dict)

# 存在しないキーへアクセスした際は例外が発生する getメソッドを使用すれば回避可能
print(score['math'])
print(score.get('japanese', 'データなし'))
print(score.get('japanese'))  # デフォルト値 Noneが出力される
print(score.get('math', 'データなし'))

band_members = {'ギター': '佐藤', 'ベース': '吉田'}
new_members = {'ドラム': '斎藤', 'ボーカル': '田中'}

# update
band_members.update(new_members)
print(band_members)

# 削除 pop
band_members.pop('ギター')
print(band_members)

# 存在確認 in
print('ベース' in band_members)

# キーが存在しない場合は値を設定する
print(band_members.setdefault('ベース', '瀧澤'))
print(band_members.setdefault('ギター', '瀧澤'))
print(band_members)

print(band_members.keys())
print(band_members.values())
print(band_members.items())
