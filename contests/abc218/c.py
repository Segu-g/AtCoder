import sys

n = int(input())
s_img = [list(map(lambda c: c=='#', input())) for _ in range(n)]
t_img = [list(map(lambda c: c=='#', input())) for _ in range(n)]

s_min_i = n
s_max_i = 0

s_min_j = n
s_max_j = 0

t_min_i = n
t_max_i = 0

t_min_j = n
t_max_j = 0


for i in range(n):
    for j in range(n):
        if s_img[i][j]:
            s_min_i = min(s_min_i, i)
            s_max_i = max(s_max_i, i)
            s_min_j = min(s_min_j, j)
            s_max_j = max(s_max_j, j)
        if t_img[i][j]:
            t_min_i = min(t_min_i, i)
            t_max_i = max(t_max_i, i)
            t_min_j = min(t_min_j, j)
            t_max_j = max(t_max_j, j)

s_i_len = s_max_i - s_min_i + 1
s_j_len = s_max_j - s_min_j + 1
t_i_len = t_max_i - t_min_i + 1
t_j_len = t_max_j - t_min_j + 1


if (s_i_len, s_j_len) == (t_i_len, t_j_len):
    flag = True
    for di in range(s_i_len):
        for dj in range(s_j_len):
            s = s_img[s_min_i + di][s_min_j + dj]
            t = t_img[t_min_i + di][t_min_j + dj]
            flag &= s == t
    if flag:
        print("Yes")
        sys.exit()
    
    flag = True
    for di in range(s_i_len):
        for dj in range(s_j_len):
            s = s_img[s_min_i + di][s_min_j + dj]
            t = t_img[t_max_i - di][t_max_j - dj]
            flag &= s == t
    if flag:
        print("Yes")
        sys.exit()

if (s_i_len, s_j_len) == (t_j_len, t_i_len):
    flag = True
    for di in range(s_i_len):
        for dj in range(s_j_len):
            s = s_img[s_min_i + di][s_min_j + dj]
            t = t_img[t_min_i + dj][t_max_j - di]
            flag &= s == t
    if flag:
        print("Yes")
        sys.exit()
    
    flag = True
    for di in range(s_i_len):
        for dj in range(s_j_len):
            s = s_img[s_min_i + di][s_min_j + dj]
            t = t_img[t_max_i - dj][t_min_j + di]
            flag &= s == t
    if flag:
        print("Yes")
        sys.exit()

print("No")