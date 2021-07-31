def solve(n: int):
    if n % 2 != 0:
        return "Odd"
    else:
        if (n//2) % 2 != 0:
            return "Same"
        else:
            return "Even"

t = int(input())
inputs = [int(input()) for _ in range(t)]
ans = list(map(solve, inputs))
print("\n".join(ans))
