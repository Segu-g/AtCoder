n = int(input())
while n >= 10:
    if n % 10 != 0:
        break
    n = n // 10
n_str = str(n)
if n_str == n_str[::-1]:
    print("Yes")
else:
    print("No")
