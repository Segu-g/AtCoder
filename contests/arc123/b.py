n = int(input())
a_vec = list(map(int, input().split()))
b_vec = list(map(int, input().split()))
c_vec = list(map(int, input().split()))

a_vec.sort()
b_vec.sort()
c_vec.sort()

count = 0
a_index = 0
b_index = 0
c_index = 0

while a_index < n and b_index < n and c_index < n:
    a, b, c = a_vec[a_index], b_vec[b_index], c_vec[c_index]
    if a >= b:
        b_index += 1
        continue
    if b >= c:
        c_index += 1
        continue
    count += 1
    a_index += 1
    b_index += 1
    c_index += 1
print(count)
