n = int(input())
a_array = list(map(int, input().split()))
stack = [(a_array[0], 0)]
ans = a_array[0]
for i in range(1, n):
    a = a_array[i]
    if stack[-1][0] < a:
        stack.append((a, i))
    else:
        while len(stack) > 0 and stack[-1][0] >= a:
            former_max = stack.pop()
            # print(f"index: ({former_max[1]} ~ {i -1}), value: {former_max[0]}")
            ans = max(ans, former_max[0]*(i - former_max[1]))
        stack.append((a, former_max[1]))
for a, index in stack:
    ans = max(ans, a*(n-index))
    # print(f"index: ({index} ~ {n-1}), value: {a}")
print(ans)
