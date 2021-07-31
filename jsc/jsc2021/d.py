n, p = map(int, input().split())
MOD = 10**9 + 7
pm1 = p-1
bad_n = 0
good_n = pm1
sum_n = pm1
# breakpoint()
for i in range(1, n):
    sum_n = (sum_n * pm1) % MOD
    bad_n = ((bad_n * pm1) % MOD + good_n % MOD) % MOD
    good_n = (sum_n - bad_n) % MOD
print(good_n)
