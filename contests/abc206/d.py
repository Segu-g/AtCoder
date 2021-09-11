import sys

sys.setrecursionlimit(200000)

n = int(input())
a_vec = list(map(int, input().split()))
a_set = set()

for i in range(n // 2):
    a_f = a_vec[i]
    a_b = a_vec[n - 1 - i]
    if a_f != a_b:
        a_set.add(a_b)
        a_set.add(a_f)

a_keys = list(a_set)
a_dic = dict()
for i, a in enumerate(a_set):
    a_dic[a] = i

paths = [set() for _ in range(len(a_keys))]
for i in range(n // 2):
    a_f = a_vec[i]
    a_b = a_vec[n - 1 - i]
    if a_f != a_b:
        f = a_dic[a_f]
        b = a_dic[a_b]
        paths[f].add(b)
        paths[b].add(f)


a_flags = [False for _ in range(len(a_keys))]


def count(index):
    if a_flags[index]:
        return False
    a_flags[index] = True
    for path in paths[index]:
        count(path)
    return True


cnt = len(a_keys)
for i in range(len(a_keys)):
    if count(i):
        cnt -= 1

print(cnt)
