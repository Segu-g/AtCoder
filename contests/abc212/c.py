n, m = map(int, input().split())

a_vec = list(map(int, input().split()))
b_vec = list(map(int, input().split()))

comp_vec = tuple((a, 0) for a in a_vec) + tuple((b, 1) for b in b_vec)
sorted_comp_vec = sorted(comp_vec)
a_vec.sort()
b_vec.sort()

buf_a, buf_b = min(a_vec), min(b_vec)
ans = abs(buf_a - buf_b)

for val, label in sorted_comp_vec:
    if label == 0:
        buf_a = val
    elif label == 1:
        buf_b = val
    ans = min(ans, abs(buf_a - buf_b))


print(ans)
