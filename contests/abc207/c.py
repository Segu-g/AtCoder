n = int(input())


def have_common(p0, p1):
    if p0[1] > p1[1]:
        p0, p1 = p1, p0
    t0, l0, r0 = p0
    t1, l1, r1 = p1
    if l1 < r0:
        return True
    elif l1 == r0:
        if t0 in (1, 3) and t1 in (1, 2):
            return True
    return False


input_lst = [tuple(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if have_common(input_lst[i], input_lst[j]):
            count += 1
print(count)
