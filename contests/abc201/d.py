h, w = map(int, input().split())
a_array = [list(map(lambda c: 1 if c == "+" else -1, input())) for _ in range(h)]
# print(a_array)
dp = [[0 for _ in range(w)] for _ in range(h)]

dp[h - 1][w - 1] = -a_array[h - 1][w - 1]
for sum_ij in range(h + w - 2 - 1, -1, -1):
    for i in range(max(0, sum_ij - w + 1), min(sum_ij + 1, h)):
        j = sum_ij - i
        if i == h - 1:
            val = dp[i][j + 1]
        elif j == w - 1:
            val = dp[i + 1][j]
        else:
            val = min(dp[i + 1][j], dp[i][j + 1])
        dp[i][j] = -val - a_array[i][j]


x = dp[0][0] + a_array[0][0]
if x > 0:
    print("Takahashi")
elif x < 0:
    print("Aoki")
else:
    print("Draw")
