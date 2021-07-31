n = int(input())
color_pos = dict()
for i in range(n):
    x, c = map(int, input().split())
    if c in color_pos:
        left, right = color_pos[c]
        color_pos[c] = (min(left, x), max(right, x))
    else:
        color_pos[c] = (x, x)
items = color_pos.items()
colors = sorted(items)
dp = [((0, 0) , (0, 0))]

def reach(dp_element, to):
    from_left = dp_element[0]
    from_right = dp_element[1]
    left_time = from_left[0] + abs(to - from_left[1])
    right_time = from_right[0] + abs(to - from_right[1])
    return min(left_time, right_time)

for c, rang in colors:
    left_pos, right_pos = rang
    dp_ele = dp[-1]
    length = right_pos - left_pos
    # print(f"{right_pos}:{reach(dp_ele, right_pos)}, {left_pos}:{reach(dp_ele, left_pos)}")
    dp.append(((reach(dp_ele, right_pos) + length, left_pos), (reach(dp_ele, left_pos) + length, right_pos)))

# print(dp)
last_ele = dp.pop()
print(min(last_ele[0][0] + last_ele[0][1], last_ele[1][0] + last_ele[1][1]) )
