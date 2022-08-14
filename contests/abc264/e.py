n, m, e = map(int, input().split())

wires = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(e)]
q = int(input())
error_wires_index = [int(input()) - 1 for _ in range(q)]

sorted_error_wires_index = sorted(error_wires_index, reverse=True)

rest_wires_index = []
for i in range(e):
    if sorted_error_wires_index and sorted_error_wires_index[-1] == i:
        sorted_error_wires_index.pop()
        continue
    rest_wires_index.append(i)

union_find = [-1 for p in range(n + m)]

up_target_threshold = n
up_target_num = m


def find(target):
    return target if union_find[target] < 0 else find(union_find[target])


def is_up(target):
    return find(target) >= up_target_threshold


def get_count(parent):
    return -union_find[parent]


def union(target1, target2):
    global up_target_num
    # print(f"connect: {target1} {target2}")
    # print(f"    {target1}: {find(target1)}")
    # print(f"    {target2}: {find(target2)}")
    par1, par2 = find(target1), find(target2)
    if par1 > par2:
        par1, par2 = par2, par1
    if par1 == par2:
        return
    if not is_up(par1) and is_up(par2):
        up_target_num += get_count(par1)
    union_find[par2] += union_find[par1]
    union_find[par1] = par2
    # print(union_find, up_target_num)


for i in rest_wires_index:
    wire = wires[i]
    wire = sorted(wire)
    union(wire[0], wire[1])

reversed_error_wires_index = reversed(error_wires_index)
reversed_up_target_nums = []
for error_wire_index in reversed_error_wires_index:
    reversed_up_target_nums.append(up_target_num - m)
    error_wire = wires[error_wire_index]
    union(error_wire[0], error_wire[1])

print("\n".join(map(str, reversed(reversed_up_target_nums))))
