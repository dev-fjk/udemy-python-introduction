# 超基礎文法系
print("Hello World!")

# 割り算を実施してくれるメソッド divmod() 割った結果とあまりを返却してくれる
print(divmod(10, 3))

# 変数 変数名 = 代入値 型推論あり
# javaのデータ型についても pythonだとメモリの番地参照となるようなので注意(基本再代入はしない方がよさげ)
num = 100
print(num)

# 型確認 この場合は<class 'int'>  <class 'str'>
print(type(num))
print(type('str'))

# 型変換 float -> int
float_num = 10.1
change_int = int(float_num)
print(changeInt)
