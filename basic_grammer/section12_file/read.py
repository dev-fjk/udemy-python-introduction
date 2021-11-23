# ファイルを開き、扱うためのオブジェクト
file = open('resources/hello.txt', 'r', encoding='utf-8')
source = file.read()
print(source)
file.close()

# 1行ずつ読み取る例
# 文字コードが違う場合 Unicode Decode Errorが発生する
with open('resources/hello.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
