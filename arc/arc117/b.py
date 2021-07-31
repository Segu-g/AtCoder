n = int(input())
a_array = list(map(int, input().split()))
MOD = 10**9 + 7
a_array.sort()
num = 1
base = 0
for a in a_array:
    diff = a - base
    num = (num * (diff+1)) % MOD
    base = a
print(num)
