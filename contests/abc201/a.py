a_array = list(map(int, input().split()))
a_array.sort()
if a_array[1] - a_array[0] == a_array[2] - a_array[1]:
    print("Yes")
else:
    print("No")
