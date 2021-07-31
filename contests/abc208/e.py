import math

n_str, k_str = input().split()
n, k = int(n_str), int(k_str)

max_dig = min(len(n_str), math.ceil(math.log2(k)))
