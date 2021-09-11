MOD = 10 ** 9 + 7


def main():
    n = int(input())
    a_gen = map(int, input().split())
    pm = (1, 0)
    a = a_gen.__next__()
    pm_sum = (a, 0)
    pm = (1, 0)
    for a in a_gen:
        # print(pm, pm_sum)
        p, m = pm
        ps, ms = pm_sum
        ps_next = ((ps + ms) % MOD + ((p + m) % MOD) * a) % MOD
        ms_next = (ps - (p * a) % MOD) % MOD
        pm_sum = (ps_next, ms_next)
        pm = ((p + m) % MOD, p % MOD)

    # print(pm, pm_sum)
    print((pm_sum[0] + pm_sum[1]) % MOD)


if __name__ == "__main__":
    main()
