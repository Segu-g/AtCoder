n = int(input())
t, f = 1, 1
for i in range(n):
    s = input()
    t_b, f_b = t, f
    if s == "AND":
        t = t_b
        f = t_b + f_b * 2
    elif s == "OR":
        t = t_b * 2 + f_b
        f = f_b
print(t)
