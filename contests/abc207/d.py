from functools import cmp_to_key
import sys
from typing import List, Tuple, Callable

VEC = Tuple[int, int]
LABEL = Tuple[int, int, int]


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def square(p):
    return p[0] ** 2 + p[1] ** 2


def theta_lab(p0: VEC, p1: VEC) -> LABEL:
    dot = p0[0] * p1[0] + p0[1] * p1[1]
    cross = p0[0] * p1[1] - p0[1] * p1[0]
    return (square(p0) * square(p1), dot ** 2, to_level(sign(cross), sign(dot)))


def to_level(cross_sign: int, dot_sign: int):
    signs = (cross_sign, dot_sign)
    if signs == (0, 0):
        return 0
    elif signs == (1, 1):
        return 1
    elif signs == (1, 0):
        return 2
    elif signs == (1, -1):
        return 3
    elif signs == (0, -1):
        return 4
    elif signs == (-1, -1):
        return 5
    elif signs == (-1, 0):
        return 6
    else:
        return 7


def compare(lab0: LABEL, lab1: LABEL) -> int:
    ab0, dot20, level0 = lab0
    ab1, dot21, level1 = lab1
    if level0 < level1:
        return -1
    elif level0 == level1:
        level = level0
        if level in (0, 2, 4, 6):
            return -1 if ab0 < ab1 else (0 if ab0 == ab1 else 1)
        elif level in (1, 5):
            if ab1 * dot20 > ab0 * dot21:
                return -1
            elif ab1 * dot20 == ab0 * dot21:
                return -1 if ab0 < ab1 else (0 if ab0 == ab1 else 1)
            else:
                return 1
        elif level in (3, 7):
            if ab1 * dot20 < ab0 * dot21:
                return -1
            elif ab1 * dot20 == ab0 * dot21:
                return -1 if ab0 < ab1 else (0 if ab0 == ab1 else 1)
            else:
                return 1
    return 1


n = int(input())
s = tuple(tuple(map(int, input().split())) for _ in range(n))
t = tuple(tuple(map(int, input().split())) for _ in range(n))

if n == 1:
    print("Yes")
    sys.exit()
mid_s: VEC = (sum(a for a, _ in s), sum(b for _, b in s))
mid_t: VEC = (sum(a for a, _ in t), sum(b for _, b in t))
scaled_s: Tuple[VEC, ...] = tuple(map(lambda p: (p[0] * n - mid_s[0], p[1] * n - mid_s[1]), s))
scaled_t: Tuple[VEC, ...] = tuple(map(lambda p: (p[0] * n - mid_t[0], p[1] * n - mid_t[1]), t))


base_lab: VEC = (1, 0)
zero_filter: Callable[[VEC], bool] = lambda p: p != (0, 0)
s_labs: Tuple[LABEL, ...] = tuple(map(lambda p: theta_lab(base_lab, p), filter(zero_filter, scaled_s)))
t_labs: Tuple[LABEL, ...] = tuple(map(lambda p: theta_lab(base_lab, p), filter(zero_filter, scaled_t)))
if len(s_labs) != len(t_labs):
    print("No")
    sys.exit()


cmp: Callable[[Tuple[LABEL, VEC], Tuple[LABEL, VEC]], int] = lambda p0, p1: compare(p0[0], p1[0])
sorted_s_zip: List[Tuple[LABEL, VEC]] = sorted(zip(s_labs, scaled_s), key=cmp_to_key(cmp))
sorted_t_zip: List[Tuple[LABEL, VEC]] = sorted(zip(t_labs, scaled_t), key=cmp_to_key(cmp))

# print(s)
# print(t)

# print(scaled_s)
# print(scaled_t)

# print(sorted_s_zip)
# print(sorted_t_zip)

flag = False
s_base = sorted_s_zip[0][1]
for i in range(len(sorted_t_zip)):
    t_base = sorted_t_zip[i][1]
    for j in range(len(sorted_t_zip)):
        s_vec = sorted_s_zip[j][1]
        t_vec = sorted_t_zip[(i + j) % n][1]
        s_lab = theta_lab(s_base, s_vec)
        t_lab = theta_lab(t_base, t_vec)
        if compare(s_lab, t_lab) != 0:
            # print("break", s_base, t_base, s_vec, t_vec, s_lab, t_lab)
            break
    else:
        flag = True

    if flag:
        break

print("Yes" if flag else "No")
