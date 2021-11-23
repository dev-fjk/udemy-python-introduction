your_input = input('数字を入れてください>')

try:
    number = int(your_input)
    print(10 / number)
except ValueError:  # except:だけにすると全エラーをcatch可能(非推奨)
    print('数字以外が入力されました')
except ZeroDivisionError:
    print('0は入力しないでください')
except:
    print('その他エラー')
