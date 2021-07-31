
n, x = map(int, input().split())
ans = -1
sum_al = 0
for i in range(n):
    v, p = map(int, input().split())
    sum_al += v * p
    if sum_al > x * 100:
        ans = i + 1
        break
print(ans)
