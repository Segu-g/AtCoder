r, c = map(int, input().split())
r = r if r < 8 else 16 - r
c = c if c < 8 else 16 - c
r, c = sorted([
    r,
    c,
])

print("white" if r % 2 == 0 else "black")