MOD = 998244353
n, k = map(int, input().split())
cumulative_sum = [0 for _ in range(n+1)]
table = [0 for i in range(n)]
pair_list = []
for i in range(k):
    l, r = map(int, input().split())
    pair_list.append((l,r))

table[0] = 1
cumulative_sum[1] = 1
for i in range(1,n):
    root = 0
    for l, r in pair_list:
        l = max(i-l+1, 0)
        r = max(i-r,0)
        root += cumulative_sum[l]- cumulative_sum[r]
        root %= MOD
    table[i]= root % MOD
    cumulative_sum[i+1] = (cumulative_sum[i]+root)%MOD
    #print("step{}\n table:{}\n  cum:{}".format(i,table, cumulative_sum))

print(table[-1])
