n = int(input())
s = input()
a_array = list(map(int, input().split()))
minimal_array = [0 for _ in range(n+1)]
for i in range(n):
    if s[i] == '<':
        minimal_array[i+1] = minimal_array[i] + 1
for i in range(n-1, -1, -1):
    if s[i] == '>':
        minimal_array[i] = max(minimal_array[i], minimal_array[i+1]+1)


diff_array = [0 for _ in range(n)]
for i in range(n):
    diff_array[i] = a_array[i+1] - a_array[i]

div_array = [float("inf") for _ in range(n)]
for i in range(n):
    if minimal_array[i] != 0:
        div_array[i] = a_array[i] // minimal_array[i]

min_div = min(div_array)

print(min_div)
str_minimal_array = list(map(str, minimal_array))
for _ in range(min_div-1):
    print(" ".join(str_minimal_array))
print(" ".join([str(a_array[i] - (min_div-1) * minimal_array[i]) for i in range(n+1)]))
