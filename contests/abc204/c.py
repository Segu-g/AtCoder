import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
from_town_to = [set() for _ in range(n)]
to_town_from = [set() for _ in range(n)]
for i in range(n):
    from_town_to[i].add(i)
    to_town_from[i].add(i)

for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    to_a = from_town_to[a].copy()
    from_b = to_town_from[b].copy()
    for from_town in to_a:
        to_town_from[from_town].update(from_b)
    for to_town in from_b:
        from_town_to[to_town].update(to_a)

    # update_froma = to_town_from[b].copy()
    # update_tob = from_town_to[a].copy()
    # to_town_from[a].update(update_froma)
    # from_town_to[b].update(update_tob)
    # to_town_from[a].add(b)
    # from_town_to[b].add(a)
    # print(from_town_to)
    # print(to_town_from)

print(sum(map(len, to_town_from)))
