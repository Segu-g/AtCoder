import math
class SegmentTree:
    __slots__ = ["operator", "depth", "len", "memlen", "initial_val", "invalid_val", "__len__", "memory"]

    def __init__(self, operator, length, initial_val, invalid_val):
        self.operator = operator
        self.depth = math.ceil(math.log2(length))
        self.len = length
        self.memlen = 2 ** self.depth
        self.initial_val = initial_val
        self.invalid_val = invalid_val
        self.__len__ = lambda: self.len
        self.memory = [initial_val for _ in range(2*self.memlen -1)]


    def _sub_query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.invalid_val
        elif a <= l and r <= b:
            return self.memory[k]
        else:
            vl = self._sub_query(a, b, k*2+1, l, (l+r)//2)
            vr = self._sub_query(a, b, k*2+2, (l+r)//2, r)
            return self.operator(vl,vr)


    def query(self, a, b):
        a, b = max(a, 0), max(b, 0)
        a, b = min(a, self.memlen), min(b, self.memlen)
        return self._sub_query(a, b, 0, 0, self.memlen)

    def update(self, index, x):
        index += self.memlen-1
        self.memory[index] = x
        while(index):
            index = (index-1) // 2
            self.memory[index] = self.operator(self.memory[index*2+1], self.memory[index*2+2])

def main():
    n, k = map(int, input().split())
    segu = SegmentTree(max, 300000, 0, 0)
    a = int(input())
    segu.update(a-1, 1)
    for _ in range(n-1):
        a = int(input())
        query_max = segu.query(a-k, a + k +1)
        segu.update(a, query_max+1)
    print(segu.memory[0])


if __name__ == "__main__":
    main()
