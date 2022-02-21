n, x = map(int, input().split())
jumps = tuple(tuple(map(int, input().split())) for _ in range(n))

flags = [False for _ in range(x + 1)]
next_flags = [False for _ in range(x + 1)]

flags[0] = True

for (a, b) in jumps:
    a, b = map(lambda v: min(v, x + 1), sorted((a, b)))
    for i in range(0, a):
        next_flags[i] = False
    for i in range(a, b):
        next_flags[i] = flags[i - a]
    for i in range(b, x + 1):
        next_flags[i] = flags[i - a] or flags[i - b]
    flags, next_flags = next_flags, flags

print("Yes" if flags[x] else "No")