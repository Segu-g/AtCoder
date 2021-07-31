a,b,c,d = map(int, input().split())
if a>c:
    a,b,c,d = c,d,a,b
if c<=b:
    print("Yes")
else:
    print("No")
