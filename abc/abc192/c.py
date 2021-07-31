n, k = map(int, input().split())


def count(num):
    lst = [0 for _ in range(10)]
    while num != 0:
        lst[num % 10] += 1
        num //= 10
    return lst

def f(lst):
    g1 = 0
    g1_dig = 1
    g2 = 0
    g2_dig = 1
    for i in range(10):
        for _ in range(lst[i]):
            g1 += g1_dig * i
            g1_dig *= 10
        for _ in range(lst[9 - i]):
            g2 += g2_dig * (9 - i)
            g2_dig *= 10
    return g1 - g2


for _ in range(k):
    n = f(count(n))

print(n)
