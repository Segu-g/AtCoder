n, m = map(int, input().split())
edges = [tuple(map(lambda s: int(s) - 1, input().split())) for _ in range(m)]
par = [i for i in range(n)]

def root(i: int):
    while par[i] != i:
        i = par[i]
    return i

def unite(x, y):
    root_x, root_y = map(root, (x, y))
    root_x, root_y = sorted((root_x, root_y))
    par[root_y] = root_x

for edge in filter(lambda edge: edge[2] <= 0, edges):
    a, b, _ = edge
    unite(a, b)

