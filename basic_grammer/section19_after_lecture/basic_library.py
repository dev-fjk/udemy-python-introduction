import datetime
import os
import shutil
from collections import Counter, defaultdict, OrderedDict

# datetimeモジュール
from pathlib import Path

now = datetime.datetime.now()
print(now)
date = datetime.datetime(year=2021, month=12, day=30, hour=12, minute=10, second=30)
print(date)

delta = datetime.timedelta(days=3)
print(date + delta)  # 日付の加算減算

# 日付の文字列出力例
message = '{0.year}-{0.month}-{0.day}'.format(date)
print(message)

# collectionsモジュール
my_list = [1, 1, 1, 5, 1, 2, 5, 1]
counter = Counter(my_list)  # 各要素の含まれる数を返す
print(counter)  # Counter({1: 5, 5: 2, 2: 1})
print(counter.most_common())  # 要素数の多い順出力 [(1, 5), (5, 2), (2, 1)]

my_dict = defaultdict(int)
print(my_dict['fjk'])  # デフォルト値を持つ辞書を作成　デフォルト値はdefaultdictの引数に渡した型の初期値

my_dict = OrderedDict()  # 登録順序を保持する辞書 (LinkedHashMapみたいなの)
my_dict['food'] = 'カレー'
my_dict['juice'] = 'コーラ'

for key, val in my_dict.items():
    print(key, val)

# pathlibモジュール javaでいうFiles的立ち位置っぽい
current = Path()  # 初期値を設定しない場合カレントディレクトリの情報を持って生成
for path in current.iterdir():
    print(path)

# ディレクトリだけ出力する例
basic_route = Path("..")
for path in basic_route.iterdir():
    if path.is_dir():
        for p in path.iterdir():
            print(p)

hello = Path('hello.txt')
with hello.open('w', encoding='utf-8') as file:
    file.write('hello')

# shutilモジュール　高水準なファイル操作 UNIXライクな命名で良い感じ
# rmtreeでフォルダ丸ごと削除できる(ファイルが入っている場合でも消せス)
shutil.copy('hello.txt', 'copy.txt')  # copytreeメソッドで ディレクトリコピーも可能
shutil.move('copy.txt', 'rename.txt')  # ファイルの移動 リネーム

# ファイル削除 osモジュールか Path.unlinkで消す　rmdirでディレクトリも消せるが空ディレクトリでないと消せない
shutil.copy('hello.txt', 'delete_target.txt')
os.remove('delete_target.txt')
# path = Path('delete_target.txt')
# path.unlink()
