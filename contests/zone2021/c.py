n = int(input())
STATUS_NUM = 5
status_array = [[None for _ in range(n)] for _ in range(STATUS_NUM)]
val_set = set()
for i in range(n):
    for status_i, val in enumerate(map(int, input().split())):
        status_array[status_i][i] = (val, i)
        val_set.add(val)

val_array = list(val_set)
val_array.sort(reverse=True)
for status_i in range(STATUS_NUM):
    status_array[status_i].sort(reverse=True)

status_flags = [0 for _ in range(n)]
next_indexs = [0 for _ in range(STATUS_NUM)]
satisfied_set = set()
flag = False

for val in val_array:
    for status_i in range(5):
        while True:
            if next_indexs[status_i] >= n:
                break
            element = status_array[status_i][next_indexs[status_i]]
            if element[0] < val:
                break
            status_flags[element[1]] += 1 << status_i
            satisfied_set.add(status_flags[element[1]])
            next_indexs[status_i] += 1
    for a in satisfied_set:
        for b in satisfied_set:
            for c in satisfied_set:
                if a | b | c == 31:
                    flag = True
    if flag:
        break

print(val)
