n = int(input())
t_vec = list(map(int, input().split()))
sum_t = sum(t_vec)
half_t = sum_t / 2

time_bag = [False for _ in range(sum_t + 1)]
time_bag[0] = True

best_t = 0
best_diff = half_t
for t in t_vec:
    for from_t, to_t in zip(range(sum_t + -t, -1, -1), range(sum_t, t - 1, -1)):
        if time_bag[from_t]:
            # print(f"from_t:{from_t}, to_t:{to_t}")
            time_bag[to_t] = True
            if abs(half_t - to_t) < best_diff:
                best_t = to_t
                best_diff = abs(half_t - to_t)

print(max(best_t, sum_t - best_t))
