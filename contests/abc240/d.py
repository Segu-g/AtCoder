n = int(input())
a_arr = tuple(map(int, input().split()))

fifo = []
sum_n = 0
ans = []

for a in a_arr:
    sum_n += 1
    if not len(fifo):
        fifo.append([a, 1])
    else:
        if fifo[-1][0] == a:
            fifo[-1][1] += 1
        else:
            fifo.append([a, 1])
    if len(fifo) and fifo[-1][0] == fifo[-1][1]:
        a, n = fifo.pop()
        sum_n -= n
    ans.append(sum_n)

print("\n".join(map(str, ans)))
