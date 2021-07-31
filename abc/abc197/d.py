import math
n = int(input())
x0, y0 = map(int, input().split())
xh, yh = map(int, input().split())
xoh, yoh = xh - x0, yh - y0
xd = math.sin(math.pi / n) * (xoh * math.cos(math.pi * (n//2 - 1) / n) + yoh * math.sin(math.pi * (n//2 - 1) / n))
yd = math.sin(math.pi / n) * (yoh * math.cos(math.pi * (n//2 - 1) / n) - xoh * math.sin(math.pi * (n//2 - 1) / n))
print(x0 + xd, y0 + yd)
