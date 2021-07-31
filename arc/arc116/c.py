MOD = 998244353
n, m = map(int, input().split())
MAX_DEPTH = 18
dp = [[0 for _ in range(m + 1)] for _ in range(MAX_DEPTH)]

for i in range(1, m+1):
    dp[0][i] = 1
