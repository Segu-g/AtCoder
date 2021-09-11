p = int(input())
f_vec = [1]
for i in range(1, 11):
    f_vec.append(f_vec[-1] * i)

num = 0
for f in reversed(f_vec):
    num += p // f
    p %= f
print(num)
