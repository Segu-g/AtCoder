n = int(input())

lo = 0
hi = 10**6
while lo < hi:
    mid = (lo + hi) // 2
    string = str(mid)
    val = int(string + string)
    if  n < val:
        hi = mid
    else:
        lo = mid + 1
print(lo - 1)
