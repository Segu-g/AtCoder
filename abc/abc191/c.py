h, w = map(int, input().split())
s_img = [None for _ in range(h)]
for i in range(h):
    s_img[i] = list(map(lambda s: 1 if s == '#' else 0, input()))

count = 0

# count vertical line
for ver in range(1, h):
    for hol in range(1, w):
        if s_img[ver][hol] != s_img[ver - 1][hol]:
            if s_img[ver][hol] != s_img[ver][hol-1] or s_img[ver - 1][hol] != s_img[ver - 1][hol - 1]:
                count += 1
        if s_img[ver][hol] != s_img[ver][hol-1]:
            if s_img[ver][hol] != s_img[ver-1][hol] or s_img[ver][hol-1] != s_img[ver - 1][hol - 1]:
                count += 1
print(count)
