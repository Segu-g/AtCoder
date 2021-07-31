n, prime_cost = map(int, input().split())
event_list = []
for _ in range(n):
    a, b, c = map(int, input().split())
    event_list.append((a, c))
    event_list.append((b + 1, -c))
event_list.sort(key = lambda x: x[0])
# print(event_list)
cost = 0
total_cost = 0
last_date = 0
index = 0
for index in range(2*n):
    date = event_list[index][0]
    # print(f"{last_date} {date}: {cost}")
    total_cost += cost * (date - last_date) if cost < prime_cost else prime_cost * (date - last_date)
    cost += event_list[index][1]
    last_date = date
print(total_cost)
