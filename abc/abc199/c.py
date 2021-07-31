n = int(input())
s = input()
q = int(input())
swap = False
s_lst = [list(s[:n]), list(s[n:])]
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        a, b = a-1, b-1
        a_index, a_pos = (0, a) if a < n else (1, a-n)
        b_index, b_pos = (0, b) if b < n else (1, b-n)
        # print(a_index, a_pos)
        # print(b_index, b_pos)
        s_lst[a_index][a_pos], s_lst[b_index][b_pos] = s_lst[b_index][b_pos], s_lst[a_index][a_pos] 
    else:
        s_lst[0], s_lst[1] = s_lst[1], s_lst[0]

print("".join(s_lst[0]) + "".join(s_lst[1]))