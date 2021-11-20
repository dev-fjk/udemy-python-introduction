# write
text = """おはよう
こんにちは
こんばんは"""

text2 = '追記'

# ファイルを開き、扱うためのオブジェクト
file = open('resources/hello.txt', 'w', encoding='utf-8')
file.write(text)
file.close()

# aで追記モードになる
# wbでバイナリ形式の書き込み可能(pngなど)
file = open('resources/hello.txt', 'a', encoding='utf-8')
file.write(text2)
file.close()

# 処理が終了したら自動で閉じるようにしたい with文
# with文終了時にファイルが自動で閉じられる
with open('resources/hello2.txt', 'w', encoding='utf-8') as file2:
    file2.write(text)
