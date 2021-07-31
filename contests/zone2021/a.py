s = input()

pattern = "ZONe"
count = 0
for i in range(len(s) - len(pattern) + 1):
    if s[i : i + len(pattern)] == pattern:
        count += 1
print(count)
