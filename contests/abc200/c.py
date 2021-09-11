n = int(input())
a_array = map(int, input().split())
mod_array = [0 for _ in range(200)]
for a in a_array:
    mod_array[a % 200] += 1
ans = 0
for num in mod_array:
    ans += (num * (num - 1)) // 2

print(ans)
