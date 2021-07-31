n = int(input())
town_lst = []
x_lst = []
y_lst = []

for i in range(n):
    x, y = map(int, input().split())
    town_lst.append((x, y))
    x_lst.append((x, i))
    y_lst.append((y, i))


x_lst.sort()
y_lst.sort()


def dist(lst, i0, i1):
    return abs(lst[i1][0] - lst[i0][0])


def compare_town(towns0, towns1):
    if towns0[0] == towns1[0] and towns0[1] == towns1[1]:
        return True
    elif towns0[0] == towns1[1] and towns0[1] == towns1[0]:
        return True
    return False


x_d = dist(x_lst, 0, -1)
x_town = (x_lst[-1][1], x_lst[0][1])
y_d = dist(y_lst, 0, -1)
y_town = (y_lst[-1][1], y_lst[0][1])

if x_d > y_d:
    max_town = x_town
    lst = [
        (dist(y_lst, 0, -1), (y_lst[0][1], y_lst[-1][1])),
        (dist(y_lst, 1, -1), (y_lst[1][1], y_lst[-1][1])),
        (dist(y_lst, 0, -2), (y_lst[0][1], y_lst[-2][1])),
        (dist(x_lst, 0, -2), (x_lst[0][1], x_lst[-2][1])),
        (dist(x_lst, 1, -1), (x_lst[1][1], x_lst[-1][1])),
    ]
else:
    max_town = y_town
    lst = [
        (dist(x_lst, 0, -1), (x_lst[0][1], x_lst[-1][1])),
        (dist(y_lst, 1, -1), (y_lst[1][1], y_lst[-1][1])),
        (dist(y_lst, 0, -2), (y_lst[0][1], y_lst[-2][1])),
        (dist(x_lst, 0, -2), (x_lst[0][1], x_lst[-2][1])),
        (dist(x_lst, 1, -1), (x_lst[1][1], x_lst[-1][1])),
    ]

lst.sort()

for i in range(-1, -3, -1):
    d, town = lst[i]
    if not compare_town(max_town, town):
        print(d)
        break
