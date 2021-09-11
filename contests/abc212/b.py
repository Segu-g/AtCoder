x_vec = list(map(int, input()))

res = "Strong"

if len(set(x_vec)) == 1:
    res = "Weak"


for i in range(1, len(x_vec)):
    if (x_vec[i - 1] + 1) % 10 != x_vec[i]:
        break
else:
    res = "Weak"


print(res)
