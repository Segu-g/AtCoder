import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


n = int(input())
s_tuple = tuple(input() for _ in range(n))
suffix_dict = defaultdict(list)

for i, s in enumerate(s_tuple):
    suffix_dict[s[:3]].append(i)

paths = [[] for _ in range(n)]


for i, s in enumerate(s_tuple):
    if s[-3:] in suffix_dict:
        paths[i] = suffix_dict[s[-3:]]


reversed_paths = [[] for _ in range(n)]

for i in range(n):
    for j in paths[i]:
        reversed_paths[j].append(i)


d_lst = [len(p) for p in paths]
end_nodes = tuple(filter(lambda i: d_lst[i] == 0, range(n)))
# breakpoint()

UNREACH = 0
LOSE = 1
WIN = 2
DRAW = 3

state_lst = [UNREACH for _ in range(n)]


def search(node, state, reached):
    if reached[node]:
        return False
    state_lst[node] = max(state, state_lst[node])
    # if d_lst[node] != 0:
    #     return False
    next_state = LOSE if state == WIN else WIN
    for j in reversed_paths[node]:
        d_lst[j] -= 1
        search(j, next_state)


for end in end_nodes:
    search(end, WIN)


for i in filter(lambda i: d_lst[i] != 0, range(n)):
    state_lst[i] = DRAW


for state in state_lst:
    if state == WIN:
        print("Takahashi")
    elif state == LOSE:
        print("Aoki")
    else:
        print("Draw")
