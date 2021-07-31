n = int(input())
char_size = 26

s = tuple(map(lambda c: ord(c) - 97, input()))

if s[0] != s[-1]:
    print(1)
else:
    for i in range(1, n - 1):
        if s[0] != s[i] and s[i + 1] != s[-1]:
            print(2)
            break
    else:
        print(-1)
