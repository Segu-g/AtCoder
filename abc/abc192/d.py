x = input()
x_lst = list(map(int, x[::-1]))
d = int(max(x))
m = int(input())

def custom_int(lst, base):
    ans = 0
    dig = 1
    for num in lst:
        ans += num * dig
        dig *= base
    return ans


if len(x) == 1:
    if m < d:
        print(0)
    else:
        print(1)
else:
    lo = d + 1
    hi = m + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if m < custom_int(x_lst, mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo - d -1)
