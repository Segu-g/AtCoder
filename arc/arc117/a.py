a, b = map(int, input().split())
god_array = [0 for _ in range(a+b)]
sign = 1 if a >= b else -1
big_n = max(a, b)
small_n = min(a, b)
for i in range(big_n):
    god_array[i] = sign * (i+1)
for i in range(small_n):
    god_array[big_n+i] = -sign * (i+1)
god_array[-1] += -sign * (big_n*(big_n+1) - small_n*(small_n+1))//2
# breakpoint()
print(" ".join(list(map(str, god_array))))
