def make_squares(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i ** 2)
    return numbers


print(make_squares(10))
