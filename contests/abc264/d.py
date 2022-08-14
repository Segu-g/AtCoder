s = input()
orig = "atcoder"

swap = 0
for c in orig:
    swap += s.index(c)
    s = s.replace(c, "")
print(swap)
