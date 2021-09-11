import math


def main():
    n = int(input())
    a_vec = list(map(int, input().split()))
    a_vec.sort()
    a_cumsum = [0 for _ in range(n + 1)]
    for i in range(n):
        a_cumsum[i + 1] = a_cumsum[i] + a_vec[i]
    a_sum = a_cumsum[-1]
    min_sum = 2 * a_sum

    for i in range(math.ceil(n / 2)):
        x = a_vec[i]
        sum_val = (2 * i - n) * x + 2 * (a_sum - a_cumsum[i])
        min_sum = min(min_sum, sum_val)

    for i in range(n - 1, math.floor(n / 2), -1):
        x = a_vec[i]
        sum_val = (2 * i - n) * x + 2 * (a_sum - a_cumsum[i])
        min_sum = min(min_sum, sum_val)

    print(min_sum / n / 2)


if __name__ == "__main__":
    main()
