a, b, c, d = map(int, input().split())
dc_b = d * c - b
ans = -1
if dc_b == 0:
    if a == 0:
        ans = 0
elif dc_b > 0:
    ans = (a + dc_b - 1) // dc_b
print(ans)
