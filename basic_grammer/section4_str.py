# pythonの変数はスネークケース クォートはシングル、ダブルどちらでも可
first_name = 'Fuji'
print(first_name)
print('シングルクォート内部に"ダブルクォート"混ぜ込めます。')
print("ダブルクォート内部に'シングルクォート'混ぜ込めます。")

# int -> str
number_to_str = str(1)
print(number_to_str)
print(type(number_to_str))

# 複数行の文字列は クォート3つで囲む
# バックスラッシュを入れることで1行目に改行が入ることを防げる
text = """\
おはよう　
こんにちは
"""
print(text)

# str append
address = ''
address += '北海道'
address += '札幌市'
print(address)

# *で文字列の繰り返しも可能
# ========== レポート ============
print('=' * 10 + 'レポート' + '=' * 10)

# エスケープシーエンス \\n のようにすれば文字列として表示も可能
print('こんにちは\tタブ区切りさん')
print('こんにちは\\nタブ区切りさん')

# 文字数 length
print(len("10文字とカウント。"))

# 属性、メソッド 一覧の参照 dir(参照したい型の値)
print(dir('str_sample'))
print(dir(1))

print('================ 文字列の便利メソッド ================ ')

#  1.format  {} に指定した引数の文字列を代入する
fmt = '私の名前は{}です。'
print(fmt.format('太郎'))

fmt2 = '私の名前は{}{}です。'
print(fmt2.format('テスト', '太郎'))

fmt3 = '私の名前は{0}{1}{0}です。'
print(fmt3.format('テスト', '太郎'))

# f -string 佐藤 太郎と出力される
last_name = '佐藤'
first_name = '太郎'
print(f'{last_name} {first_name}')

# formatが出る前の古い書き方  ~ python3.5
print('私の名前は%sです' % last_name)

# 2.split 文字列の分割
languages = 'java,python,php,ruby'
lang_list = languages.split(',')
print(lang_list)

# 3.join 文字列の連結 一つの文字列にする　'java,python,php,ruby'
joined_str = ','.join(lang_list)
print(joined_str)

# 4.replace 文字列の置換
poem = '今日はとてもいい天気でした'
print(poem.replace('今日', '昨日'))

# 5.count 一致文字列のカウント
text = 'ハロー、ハロー、ハロー'
print(text.count('ハロー'))

# 6.startswith 開始文字チェック bool
# 7.endswith 終了文字チェック bool
print(text.startswith('ハロー'))  # True
print(text.startswith('dummy'))  # False
print(text.endswith('ハロー'))  # True
print(text.endswith('dummy'))  # False

# 8 文字列の場所検索
hello = 'hello world'
hello_index = hello.find(hello)
print(hello_index)  # 0

# 文字見つからない場合エラーとしたい場合はindex
print(hello.index('world'))  # 含まれてない場合例外

# 9 文字列切り取り rstrip 左側だけ lstrip 右側だけ
text = '           HelloWorld         '
print(text.strip())
print(text.rstrip())
print(text.lstrip())

print('================ 文字列の便利メソッド ================ ')

print('================ シーケンス型としての文字列操作 ================ ')

text = 'あいうえお'
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
# print(text[5]) index out

# ~文字目まで
print(text[0:3])
print(text[1:])
print(text[:4])

# ラスト三文字を取得
print(text[-3:])

# step 何文字ずつとるか start:end:step
print(text[1:4:2])
# 分かりづらくなるので以下のように書いたほうが可読性良い
text2 = text[1:4]
print(text2[::2])

# step に-1を入れると逆順で取得可能
print(text[::-1])  # おえういあ

print('================ シーケンス型としての文字列操作 ================ ')
