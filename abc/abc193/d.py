k = int(input())
takahashi = map(int, input()[:-1])
aoki = map(int, input()[:-1])

card_n = 9*k - 8
deck = {i:k  for i in range(1,10)}
tkhs_cards = [0 for _ in range(10)]
aoki_cards = [0 for _ in range(10)]


for s in takahashi:
    deck[s] -= 1
    tkhs_cards[s] += 1
for t in aoki:
    deck[t] -= 1
    aoki_cards[t] += 1
tkhs_points = [i * 10**tkhs_cards[i] for i in range(10)]
aoki_points = [i * 10**aoki_cards[i] for i in range(10)]

point_diff = sum(aoki_points) - sum(tkhs_points)
ans = 0
for s in range(1,10):
    for t in range(1,10):
        if s == t:
            p = deck[s]*(deck[s]-1)
        else:
            p = deck[s]*deck[t]
        diff = tkhs_points[s]*9 - aoki_points[t]*9
        if diff > point_diff:
            ans += p
print(ans/(card_n*(card_n-1)))
