import math
r, x, y = map(int, input().split())
r_s = r**2
d_s = x**2 + y**2
lo = 0
hi = 2 * 10**5
# print(lo, hi)
while lo < hi:
    mid = (lo + hi) // 2
    # print(lo, hi, mid)
    if r_s * mid**2 < d_s:
        lo = mid + 1
    else:
        hi = mid
if lo == 1 and d_s < r_s:
    print(2)
else:
    print(lo)
