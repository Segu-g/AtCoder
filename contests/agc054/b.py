MOD = 998244353

n = int(input())
w_vec = list(map(int, input().split()))

sum_w = sum(w_vec)
half_sum_w = sum_w // 2

factorial_pre = [1 for _ in range(n + 1)]
f_bef = 1
for i in range(1, n + 1):
    f_bef = (f_bef * i) % MOD
    factorial_pre[i] = f_bef


if sum_w % 2 == 0:
    dp = [[0 for _ in range(half_sum_w + 1)] for _ in range(n)]
    dp[0][0] = 1
    for w in w_vec:
        for item_num in range(n - 1, 0, -1):
            for weight in range(w, half_sum_w + 1):
                dp[item_num][weight] += dp[item_num - 1][weight - w]
                dp[item_num][weight] %= MOD
    # print(dp)
    ans = 0
    for item_num in range(n):
        pattern_num = (factorial_pre[item_num] * factorial_pre[n - item_num]) % MOD
        ans += (dp[item_num][half_sum_w] * pattern_num) % MOD
        ans %= MOD
    print(ans)
else:
    print(0)
