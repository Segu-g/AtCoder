import numpy as np

n = int(input())
c_arrays = [list(map(int, input().split())) for _ in range(n)]
c_mat = np.array(c_arrays)
row_diff = c_mat[:-1,:] - c_mat[1:,:]
col_diff = c_mat[:,:-1] - c_mat[:,1:]
row_flag = np.all(row_diff.max(axis = 1) == row_diff.min(axis = 1))

col_flag = np.all(col_diff.max(axis = 0) == col_diff.min(axis = 0))

flag = False
a_array = None
b_array = None
if row_flag and col_flag and n != 1:
    a_diff = row_diff.max(axis = 1)
    b_diff = col_diff.max(axis = 0)
    a_diff_cumsum = [0 for _ in range(n)]
    b_diff_cumsum = [0 for _ in range(n)]
    for i in range(1, n):
        a_diff_cumsum[i] = a_diff_cumsum[i-1] + a_diff[i-1]
        b_diff_cumsum[i] = b_diff_cumsum[i-1] + b_diff[i-1]
    a_max_diff = max(a_diff_cumsum)
    b_max_diff = max(b_diff_cumsum)
    if c_mat[0,0] < a_max_diff + b_max_diff:
        flag = False
    else:
        flag = True
        a_array = a_max_diff  - a_diff_cumsum
        b_array = c_mat[0,0] - a_max_diff - b_diff_cumsum
if n ==1:
    flag = True
    a_array = [0]
    b_array = [c_arrays[0][0]]
print("Yes" if flag else "No")
if flag:
    print(" ".join(list(map(str, a_array))))
    print(" ".join(list(map(str, b_array))))
