n, m = map(int, input().split())
a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))
a_array.sort()
b_array.sort()

ret = []
a_i, b_i = 0, 0
while a_i < n and b_i < m:
    a, b = a_array[a_i], b_array[b_i]
    if a < b:
        ret.append(a)
        a_i += 1
    elif b < a:
        ret.append(b)
        b_i += 1
    else:
        a_i += 1
        b_i += 1
if a_i != n:
    for i in range(a_i, n):
        ret.append(a_array[i])
if b_i != m:
    for i in range(b_i, n):
        ret.append(b_array[i])
print(" ".join(list(map(str, ret))))
