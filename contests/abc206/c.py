from collections import defaultdict

n = int(input())
a_map = map(int, input().split())
a_dic = defaultdict(int)
for a in a_map:
    a_dic[a] += 1

ret = 0
for a_val, a_num in a_dic.items():
    n -= a_num
    ret += a_num * n

print(ret)
