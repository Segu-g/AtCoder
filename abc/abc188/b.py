import numpy

n = int(input())
a_vec = numpy.array(list(map(int, input().split())), dtype = "int")
b_vec = numpy.array(list(map(int, input().split())), dtype = "int")
if numpy.dot(a_vec, b_vec) == 0:
    print("Yes")
else:
    print("No")
