h, w, x, y = map(int, input().split())
x, y = x-1, y-1
mat = [input() for _ in range(h)]
ans = [0, 0]

count = 0
flag = False
for col in range(w):
    if col == y:
        flag = True
    if mat[x][col] == "#":
        if flag:
            break
        else:
            count = 0
    else:
        count += 1
ans[0] = count

count = 0
flag = False
for row in range(h):
    if row == x:
        flag = True
    if mat[row][y] == "#":
        if flag:
            break
        else:
            count = 0
    else:
        count += 1
ans[1] = count
print(ans[0] + ans[1] - 1)
