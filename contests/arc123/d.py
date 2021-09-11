import bisect

n = int(input())
a_lst = tuple(map(int, input().split()))
a_diff_lst = tuple(a_lst[i + 1] - a_lst[i] for i in range(n - 1))
b_diff_lst = tuple(max(a_d, 0) for a_d in a_diff_lst)
c_diff_lst = tuple(min(a_d, 0) for a_d in a_diff_lst)


b_adjust_lst = [0 for _ in range(n)]
c_adjust_lst = [0 for _ in range(n)]
for i in range(n - 1):
    b_adjust_lst[i + 1] = b_adjust_lst[i] + b_diff_lst[i]
    c_adjust_lst[i + 1] = c_adjust_lst[i] + c_diff_lst[i]

b_adjust_cumsum = [0 for _ in range(n + 1)]
c_adjust_cumsum = [0 for _ in range(n + 1)]
for i in range(n):
    b_adjust_cumsum[i + 1] = b_adjust_lst[i] + b_adjust_cumsum[i]
    c_adjust_cumsum[i + 1] = c_adjust_lst[i] + c_adjust_cumsum[i]

b_adjust_reverse_cumsum = [0 for _ in range(n + 1)]
c_adjust_reverse_cumsum = [0 for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    b_adjust_reverse_cumsum[i] = b_adjust_reverse_cumsum[i + 1] + b_adjust_lst[i]
    c_adjust_reverse_cumsum[i] = c_adjust_reverse_cumsum[i + 1] + c_adjust_lst[i]

positive_c_adjust_lst = tuple(map(lambda x: -x, c_adjust_lst))


def calc_f(b0):
    c0 = a_lst[0] - b0
    bi = bisect.bisect_left(b_adjust_lst, -b0)
    ci = bisect.bisect_left(positive_c_adjust_lst, c0)
    ret = 0
    ret += -b0 * bi - b_adjust_cumsum[bi]
    ret += b_adjust_reverse_cumsum[bi] + (n - bi) * b0
    ret += c0 * ci + c_adjust_cumsum[ci]
    ret += -c_adjust_reverse_cumsum[ci] - c0 * (n - ci)
    return ret


press_b0_set = {-b for b in b_adjust_lst} | {a_lst[0] + c for c in c_adjust_lst}
press_b0_lst = list(press_b0_set)

min_val = calc_f(press_b0_lst[0])
for b0 in press_b0_lst:
    min_val = min(min_val, calc_f(b0))

print(min_val)
