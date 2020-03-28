def pares(i):
    if i % 2 == 0:
        return i

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

listaPares = filter(pares, nums)
print(list(listaPares))