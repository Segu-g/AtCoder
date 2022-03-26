s1, s2, s3 = input().split()
t1, t2, t3 = input().split()
ans = (s1, s2, s3) in {(t1, t2, t3), (t2, t3, t1), (t3, t1, t2)}
print("Yes" if ans else "No")
