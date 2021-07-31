from collections import defaultdict


def main():
    n = int(input())
    a_array = map(int, input().split())

    cumdiff_map = defaultdict(int)
    cumdiff = 0
    cumdiff_map[cumdiff] = 1

    ans = 0
    for i, a in enumerate(a_array):
        if i % 2 == 0:
            cumdiff -= a
        else:
            cumdiff += a
        ans += cumdiff_map[cumdiff]
        cumdiff_map[cumdiff] += 1
    print(ans)


if __name__ == "__main__":
    main()
