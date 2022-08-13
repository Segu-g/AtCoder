n = int(input())
print(2 * n)
print(int("".join(map(str,(n % 4,) + (4, ) * (n // 4)))))
