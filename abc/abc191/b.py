n, x = map(int, input().split())
a_array = map(int, input().split())
ans = []
for a in a_array:
    if a!=x:
        ans.append(a)
print(" ".join(map(str, ans)))
