import math
from decimal import *

# 少数第4桁までの精度なので10000倍すれば整数になる
base = 10000

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

# base倍された値を戻してceilを取る
def ceil(arg):
    ans = arg // base
    if arg % base != 0:
        ans += 1
    return int(ans)

# base倍された値を戻してfloorを取る
def floor(arg):
    ans = arg // base
    return int(ans)


# x, y, r を10進数として保持
x, y, r = map(Decimal, input().split())
# 10000倍してintにする
x, y, r = map(lambda arg: int(arg * base), (x, y, r))

# breakpoint()

# 格子点のカウンタ
count = 0

# 円の範疇に入っているxの整数値x_nに対してループ
for x_n in range(ceil(x - r) , floor(x + r) + 1):

    # 根号の値の10000倍を計算
    root = isqrt(r**2 - (x - x_n*base)**2)

    # 範囲は[(y - root)/base, (y + root)/base]であるため含まれる整数値は
    # ceil((y - root)/base) - floor((y + root)/base) + 1
    count += floor(y + root) - ceil(y - root) + 1

# 値の表示
print(count)
