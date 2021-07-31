n, ufo_d, ufo_h = map(int, input().split())

min_hight = 0
for i in range(n):
    d, h = map(int, input().split())
    min_hight = max((ufo_d * h - ufo_h * d) / (ufo_d - d), min_hight)
print(min_hight)
