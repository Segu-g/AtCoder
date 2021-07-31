def dot(a, x):
    return (a[0][0]*x[0] + a[0][1]*x[1], a[1][0]*x[0] + a[1][1]*x[1])
def dot_mat(a, b):
    return ((a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]),
            (a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]))
def plus(x, y):
    return (x[0] + y[0], x[1] + y[1])
from sys import stdin
n = int(stdin.readline())
points = [None for i in range(n)]
for i in range(n):
    x, y = map(int, stdin.readline().split())
    points[i] = (x, y)
m = int(stdin.readline())
matrix_seq = [None for _ in range(m+1)]
matrix_seq[0] = ((1, 0), (0, 1))
bias_seq = [None for _ in range(m+1)]
bias_seq[0] = (0, 0)
op1_mat = ((0, 1), (-1, 0))
op2_mat = ((0, -1), (1, 0))
op3_mat = ((-1, 0), (0, 1))
op4_mat = ((1, 0), (0, -1))
for i in range(1, m+1):
    op = list(map(int, stdin.readline().split()))
    if op[0] == 1:
        matrix_seq[i] = dot_mat(op1_mat, matrix_seq[i-1])
        bias_seq[i] = dot(op1_mat, bias_seq[i-1])
    elif op[0] == 2:
        matrix_seq[i] = dot_mat(op2_mat, matrix_seq[i-1])
        bias_seq[i] = dot(op2_mat, bias_seq[i-1])
    elif op[0] == 3:
        matrix_seq[i] = dot_mat(op3_mat, matrix_seq[i-1])
        bias_seq[i] = plus(dot(op3_mat, bias_seq[i-1]), (2*op[1], 0))
    elif op[0] == 4:
        matrix_seq[i] = dot_mat(op4_mat, matrix_seq[i-1])
        bias_seq[i] = plus(dot(op4_mat, bias_seq[i-1]) , (0, 2*op[1]))
# print(matrix_seq)
# print(bias_seq)
q = int(stdin.readline())
for i in range(q):
    a, b = map(int, stdin.readline().split())
    ans = plus(dot(matrix_seq[a], points[b-1]) , bias_seq[a])
    print(ans[0], ans[1], flush = True)
