def main():
    n = int(input())
    s = input()
    t = input()
    ans = 0
    if s.count("1") != t.count("1"):
        ans = -1
    else:
        ans = count(s, t)
    print(ans)


def count(s, t):
    s_zero_index = (i for i, c in enumerate(s) if c == "0")
    t_zero_index = (i for i, c in enumerate(t) if c == "0")
    ret = 0
    for s_i, t_i in zip(s_zero_index, t_zero_index):
        if s_i != t_i:
            ret += 1
    return ret


if __name__ == "__main__":
    main()
