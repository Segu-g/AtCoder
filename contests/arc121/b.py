n = int(input())

dogs = []
colored_dogs_count = [0, 0, 0]

colors = ["R", "G", "B"]
for i in range(2 * n):
    a, c = input().split()
    a = int(a)
    color_index = colors.index(c)
    colored_dogs_count[color_index] += 1
    dogs.append((a, i, c))


dogs.sort()


a_bufs = [None, None, None]
a_mins = [float("inf") for _ in range(3)]
for a, i, c in dogs:
    color_i = colors.index(c)
    a_bufs[color_i] = a

    for lack in range(3):
        if lack == color_i:
            continue
        p = 0
        for p in range(3):
            if p != lack and p != color_i:
                break
        if a_bufs[p] is not None:
            a_mins[lack] = min(a_mins[lack], abs(a - a_bufs[p]))


odd_indexs = []
for i in range(3):
    if colored_dogs_count[i] % 2 != 0:
        odd_indexs.append(i)


if len(odd_indexs) == 0:
    print(0)
else:
    odd2odd = 0
    odd2even = 0
    for p in range(3):
        if p not in odd_indexs:
            odd2odd += a_mins[p]
        else:
            odd2even += a_mins[p]
    print(min(odd2odd, odd2even))
