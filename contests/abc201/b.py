n = int(input())
mount_lst = []
for _ in range(n):
    s, t = input().split()
    mount_lst.append((int(t), s))
mount_lst.sort(key=lambda x: x[0], reverse=True)
print(mount_lst[1][1])
