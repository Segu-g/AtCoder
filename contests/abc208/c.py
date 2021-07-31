n, k = map(int, input().split())
a_map = map(int, input().split())

val_index_vec = []
for i, a in enumerate(a_map):
    val_index_vec.append((a, i))

val_index_vec.sort()

ans_vec = [k // n for _ in range(n)]

for i in range(k % n):
    a, index = val_index_vec[i]
    ans_vec[index] += 1

for ans in ans_vec:
    print(ans)
