s = input()
MOD = 10 ** 9 + 7
target_chars = "chokudai"
pattern_lst = [0 for _ in range(len(target_chars))]
for c in s:
    try:
        index = target_chars.index(c)
        if index == 0:
            pattern_lst[index] += 1
        else:
            pattern_lst[index] += pattern_lst[index - 1]
        pattern_lst[index] %= MOD
    except ValueError:
        pass
print(pattern_lst[-1])