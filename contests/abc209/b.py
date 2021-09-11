n, x = map(int, input().split())
a_vec = list(map(int, input().split()))

if sum(a_vec) - n // 2 <= x:
    print("Yes")
else:
    print("No")
