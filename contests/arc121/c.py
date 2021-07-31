from collections import deque

def solve():
    n = int(input())
    p_array = deque(map(lambda x: int(x) - 1, input().split()))
    p_pos = [0 for _ in range(n)]
    for i in range(n):
        p = p_array[i]
        p_pos[p] = i

    for i in range(n):
        for pos in range(i, n):
            p = p_array[pos]
            if p < i:
                continue
            elif p > i:
                p_pos[p] += 1
            else:
                
        
        p_pos

        



t = int(input())
for _ in range(t):
    solve()
