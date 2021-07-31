n, m = map(int, input().split())
gold_vals = list(map(int, input().split()))
path = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    path[x-1].append(y-1)

min_gold = [float("inf") for _ in range(n)]
ans = - float("inf")
for i in range(n):
    # print(f"{i}:{max_gold[i]}, {gold_vals[i]}")
    ans = max(ans, gold_vals[i] - min_gold[i])
    gold = min(min_gold[i], gold_vals[i])
    for town in path[i]:
        min_gold[town] = min(gold, min_gold[town])
print(ans)
