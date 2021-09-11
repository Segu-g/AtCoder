n, k = map(int, input().split())
friend_lst = [tuple(map(int, input().split())) for _ in range(n)]
friend_lst.sort()

last_town = 0
coin = k
for a, b in friend_lst:
    coin -= a - last_town
    last_town = a
    if coin < 0:
        last_town += coin
        break
    coin += b
else:
    last_town += coin
print(min(last_town, 10 ** 100))
