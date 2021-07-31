n = int(input())
lst = list(input())
def mapping(left, right):
  if left!= right:
    for s in "BRW":
      if s != left and s!= right:
        return s
  else:
    return left
for i in range(n-1, 0, -1):
  for j in range(i):
    lst[j] = mapping(lst[j], lst[j+1])
print(lst[0])
