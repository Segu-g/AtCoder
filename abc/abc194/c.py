n = int(input())
a_array = list(map(int, input().split()))
a_cumsum = [0 for _ in range(n)]
for i in range(1, n):
    a_cumsum[i] = a_cumsum[i-1] + a_array[i-1]

ans = 0
for i in range(n):
    a = a_array[i]
    ans += (n - 1) * a ** 2
    ans -= 2 * a_array[i] * a_cumsum[i]
print(ans)
