a, b= map(int, input().split())
# breakpoint()
for val in range(b // 2, 0, -1):
    sup , inf = b//val, (a + val -1)//val
    if sup > inf:
        print(val)
        break
