n = int(input())
a_array = list(map(int, input().split()))
a_top = max(enumerate(a_array[:2**(n-1)]), key= lambda x:x[1])
a_back = max(enumerate(a_array[2**(n-1):]), key= lambda x:x[1])
index = 0
if a_top[1] < a_back[1]:
    index = a_top[0]
else:
    index = a_back[0] + 2**(n-1)
print(index+1)
