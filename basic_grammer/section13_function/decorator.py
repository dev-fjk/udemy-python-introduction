def decorator(function):
    print('decorator')
    return function


@decorator
def say_hello():
    print('hello')


# pythonでは関数もオブジェクト　関数の引数に関数を渡す
# say_hello = decorator(say_hello)
say_hello()
