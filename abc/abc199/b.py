n = int(input())
a_array = map(int, input().split())
b_array = map(int, input().split())
print(max(0, min(b_array) - max(a_array) + 1))
