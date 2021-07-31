MOD = 998244353
n, m, k = map(int, input().split())


bad_ways = tuple(tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m))


sum_case = 1

case_lst = [0 for _ in range(n)]
new_case_lst = [0 for _ in range(n)]
case_lst[0] = 1

for _ in range(k):
    for i in range(n):
        new_case_lst[i] = (sum_case - case_lst[i]) % MOD
    new_sum_case = (sum_case * (n - 1)) % MOD

    for u, v in bad_ways:
        new_case_lst[u] -= case_lst[v]
        new_case_lst[u] %= MOD
        new_case_lst[v] -= case_lst[u]
        new_case_lst[v] %= MOD
        new_sum_case -= (case_lst[u] + case_lst[v]) % MOD
        new_sum_case %= MOD
    # swap
    sum_case = new_sum_case
    new_case_lst, case_lst = case_lst, new_case_lst

print(case_lst[0])
