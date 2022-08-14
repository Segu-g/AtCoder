import itertools
import numpy as np

h1, w1 = map(int, input().split())
mat1 = np.array(list(list(map(int, input().split())) for _ in range(h1)))

h2, w2 = map(int, input().split())
mat2 = np.array(list(list(map(int, input().split())) for _ in range(h2)))

flag = False
for h_tuple in itertools.combinations(range(h1), h2):
    for w_tuple in itertools.combinations(range(w1), w2):
        flag |= np.alltrue(mat1[h_tuple, :][:, w_tuple] == mat2)
        if flag:
            break
    if flag:
        break
print("Yes" if flag else "No")
