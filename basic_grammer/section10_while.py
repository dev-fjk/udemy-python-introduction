count = 0
while count < 10:
    print(count, end=' ')
    count += 1

# flag = True
# while flag:
#     user_input = input()
#     if user_input == 'exit':ski
#         flag = False

flag = True
while flag:
    user_input = input()
    if user_input == 'exit':
        break
    elif user_input == 'skip':
        print('skip!')
        continue
    print('あなたの入力は{0}でした'.format(user_input))
