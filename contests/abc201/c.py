s = input()

length = 4

dp = [[0 for _ in range(2 ** 10)] for _ in range(length)]

for i in range(10):
    dp[0][1 << i] = 1
for l in range(1, length):
    for b in range(2 ** 10):
        n = dp[l - 1][b]
        for i in range(10):
            dp[l][b | (1 << i)] += n


o_mask = 0
x_mask = 0
for i in range(10):
    if s[i] == "o":
        o_mask |= 1 << i
    elif s[i] == "x":
        x_mask |= 1 << i
# print(bin(o_mask))
# print(bin(x_mask))


def check(b):
    if o_mask & b != o_mask:
        return False
    if x_mask & (~b) != x_mask:
        return False
    return True


# breakpoint()
ans = 0
for b in range(2 ** 10):
    if check(b):
        n = dp[length - 1][b]
        # print(bin(b), n)
        ans += n
print(ans)
