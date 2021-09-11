MOD = 10 ** 9 + 7

n = int(input())
a_vec = list(map(int, input().split()))

a_vec.sort()

case_n = 1
for i, a in enumerate(a_vec):
    case_n *= max(a - i, 0) % MOD
    case_n %= MOD
print(case_n)
