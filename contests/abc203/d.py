from collections import defaultdict
import bisect
import math
from traceback import print_tb

n, k = map(int, input().split())

a_cells = [list(map(int, input().split())) for _ in range(n)]

a_dicts = defaultdict(int)
for i in range(n):
    for j in range(n):
        a = a_cells[i][j]
        a_dicts[a] += 1
a_keys = sorted(a_dicts.keys())
key_num = len(a_keys)
a_press = dict()
for i, a in enumerate(a_keys):
    a_press[a] = i

a_cumsums = [0 for _ in range(key_num)]
for i in range(k):
    for j in range(k):
        a = a_cells[i][j]
        a_index = a_press[a]
        a_cumsums[a_index] += 1

cumsum = 0
for i in range(key_num):
    val = a_cumsums[i]
    a_cumsums[i] += cumsum
    cumsum += val

start_i = 0
start_j = 0


def update_cumsum(start_pos, row, add):
    s_i, s_j = start_pos
    if row:
        for j in range(s_j, s_j + k):
            a = a_cells[s_i][j]
            a_index = a_press[a]
            a_cumsums[a_index] += 1 if add else -1
    else:
        for i in range(s_i, s_i + k):
            a = a_cells[i][s_j]
            a_index = a_press[a]
            a_cumsums[a_index] += 1 if add else -1


def move(start_pos, direction_j: bool, inc: bool):
    s_i, s_j = start_pos
    if direction_j:
        if inc:
            update_cumsum(start_pos, False, False)
            update_cumsum((s_i, s_j + k), False, True)
        else:
            update_cumsum((s_i, s_j - 1), False, True)
            update_cumsum((s_i, s_j + k - 1), False, False)
    else:
        if inc:
            update_cumsum(start_pos, True, False)
            update_cumsum((s_i + k, s_j), True, True)
        else:
            update_cumsum((s_i - 1, s_j), True, True)
            update_cumsum((s_i + k - 1, s_j), True, False)


def calc_median():
    print(a_keys)
    print(a_cumsums)
    median_index = bisect.bisect_right(a_cumsums, k ** 2 // 2)
    return a_keys[median_index]


toright = True
min_median = calc_median()

for i in range(n - k + 1):
    if toright:
        step = range(n - k)
    else:
        step = range(n - k, 0, -1)
    for j in step:
        print(calc_median())
        min_median = min(min_median, calc_median())
        move((i, j), True, toright)
    print(calc_median())
    min_median = min(min_median, calc_median())
    if i != n - k:
        move((i, n - k if toright else 0), False, True)
    toright = not toright

print(min_median)
