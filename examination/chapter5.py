from collections import deque

list_a = 'nagasakiwakyoumoamedatta'
print(list_a[2:15:3])  # gawym 2~14文字目まで3文字沖に切り出す

list_a = [5, 4, 2, 3, 1, 4, 3, 1]
list_a.remove(4)
print(list_a)  # [5, 2, 3, 1, 4, 3, 1] 最初の4だけ削除

list_a = [1, 2, 3]
list_b = [10, 20, 30]

list_a.extend(list_b)  # list_a + list_b
print(list_a)

list_a.sort(reverse=True)
print(list_a)

list_a = deque(list_a)
list_a.popleft()  # 左端の要素を削除
print(list_a)

list_b = [[x * y for x in 'abc'] for y in range(1, 3)]
print(list_b)  # [['a', 'b', 'c'], ['aa', 'bb', 'cc']]

list_a = []
for i in range(1, 5):
    for j in range(10, 15):
        if j % i > 1:
            list_a.append((i, j))

print(list_a)

list_a = [(i, j) for i in range(1, 5) for j in range(10, 15) if j % i > 1]
print(list_a)
