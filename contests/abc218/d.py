import bisect

n = int(input())

dots = list(tuple(map(int, input().split())) for _ in range(n))
dots.sort()


count = 0
for a in range(n):
    for b in range(a+1, n):
        dot_a = dots[a]
        dot_b = dots[b]
        if dot_a[0] != dot_b[0] and dot_a[1] != dot_b[1]:
            for required_dot in ((dot_a[0], dot_b[1]), (dot_b[0], dot_a[1])):
                index = bisect.bisect_left(dots, required_dot)
                if index == n or dots[index] != required_dot:
                    break
            else:
                count += 1
print(count // 2)
                




