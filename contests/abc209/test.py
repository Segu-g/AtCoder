import numpy as np

n = int(input())
lst = [[1 for _ in range(n)]]

for _ in range(n - 1):
    lst.append([sum(lst[-1][: i + 1]) for i in range(n)])

print(np.array(lst))
