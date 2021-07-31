n = int(input())
seq_n = 0
max_seq = 0
for _ in range(n):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        seq_n +=1
        max_seq = max(max_seq, seq_n)
    else:
        seq_n = 0
if max_seq < 3:
    print("No")
else:
    print("Yes")
