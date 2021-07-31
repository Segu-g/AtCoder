n = int(input())
a_gen = map(int, input().split())
sum_a = 0
for a in a_gen:
    if a > 10:
        sum_a += a - 10
print(sum_a)
