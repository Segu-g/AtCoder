import functools

@functools.lru_cache(maxsize = None)
def solve(x, y):
    if y % 2 == 0:
        return min(abs(x - y), solve(x, y // 2) + 1)
    elif y == 1:
        return abs(x - y)
    else:
        return min(abs(x - y), solve(x, (y + 1) // 2) + 2, solve(x, (y - 1) // 2) + 2)


x, y = map(int, input().split())
print(solve(x, y))
