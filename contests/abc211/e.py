import itertools

n = int(input())
k = int(input())

field = tuple(tuple(map(lambda c: c == ".", input())) for _ in range(n))
white_pallet = tuple(filter(lambda arg: field[arg[0]][arg[1]], ((i, j) for i in range(n) for j in range(n))))


def around(pos):
    return (
        (pos[0] + i, pos[1] + j)
        for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1))
        if 0 <= pos[0] + i < n and 0 <= pos[1] + j < n
    )


count = 0

for pattern in itertools.combinations(white_pallet, k):
    flags = [[False for _ in range(n)] for _ in range(n)]
    start = pattern[0]
    flags[start[0]][start[1]] = True
    num = 1
    active = [start]
    while active:
        target = active.pop()
        for next in around(target):
            if field[next[0]][next[1]] and next in pattern:
                if flags[next[0]][next[1]]:
                    continue
                else:
                    flags[next[0]][next[1]] = True
                    num += 1
                    active.append(next)
    print(pattern)
    # print(num)
    # print(flags)
    if num == k:
        count += 1

print(count)
