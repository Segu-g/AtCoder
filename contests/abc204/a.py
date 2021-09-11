s = set(map(int, input().split()))
if len(s) == 1:
    print(s.pop())
else:
    for i in range(3):
        if i not in s:
            print(i)
            break
