p_vec = list(map(int, input().split()))
chr_vec = list(map(lambda i: chr(ord('a') + i - 1), p_vec))
print(''.join(chr_vec))