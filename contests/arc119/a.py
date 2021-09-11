import math


def main():
    n = int(input())
    lg = math.floor(math.log2(n))
    min_val = float("inf")
    for b in range(lg + 1):
        bb = 2 ** b
        a = n // bb
        c = n - a * bb
        min_val = min(a + b + c, min_val)
    print(min_val)


if __name__ == "__main__":
    main()
