from collections import defaultdict

r, l = map(int, input().split())
l = l + 1
mind = [0 for i in range(l)]

primes = []


def gen(i):
    j = 0
    while j < len(primes) and primes[j] <= mind[i] and i * primes[j] < l:
        yield j
        j += 1


mind[0], mind[1] = 1, 1
for i in range(2, l):
    if mind[i] == 0:
        primes.append(i)
        mind[i] = i
    count = 0
    for j in gen(i):
        mind[i * primes[j]] = primes[j]
