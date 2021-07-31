n = int(input())
cost = [float("inf") for _ in range(3)]
for i in range(n):
    a, b = map(int, input().split())
    cost = [min(cost[0], a),
        min(cost[1], b),
        min(cost[2], max(cost[0], b), max(cost[1], a), a + b)]
print(cost[2])
