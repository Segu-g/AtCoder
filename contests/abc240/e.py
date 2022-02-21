import sys

sys.setrecursionlimit(200000)

n = int(input())

edges = tuple([] for _ in range(n))

for _ in range(n - 1):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)

ans = [None for _ in range(n)]


def create_childs(target, parent, left):
    width = 0
    for child in edges[target]:
        if child == parent:
            continue
        width += create_childs(child, target, left + width)
    width = max(1, width)
    ans[target] = (left, left + width - 1)
    return width


create_childs(0, None, 1)

print("\n".join(tuple(map(lambda x: " ".join(map(str, x)), ans))))