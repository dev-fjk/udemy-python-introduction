from sys import argv

# sysモジュールの　argvでリスト形式で引数を受け取る
# python chapter2.py japanese english
print(argv[0])  # chapter2.py(ファイル名)
print(argv[1])  # japanese
print(argv[2])  # english
