a1, a2, a3 = map(int, input().split())
d = a1 - 2 * a2 + a3

if d >= 0:
    print((d + 1) // 2 + d % 2)
else:
    print(abs(d))
