d = 0
pos = [0, 0]
n = int(input())
t_arr = input()
for t in t_arr:
    if t == "S":
        if d == 0:
            pos[0] += 1
        elif d == 1:
            pos[1] -= 1
        elif d == 2:
            pos[0] -= 1
        elif d == 3:
            pos[1] += 1
    elif t == "R":
        d = (d + 1) % 4
print(pos[0], pos[1])
