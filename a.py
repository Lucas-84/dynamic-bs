# Algorithme de recherche dichotomique dynamique

from random import randint

def binary_search(M, c):
    low = 0
    up = len(M)
    while low < up - 1:
        mid = low + (up - low) // 2
        if M[mid] <= c:
            low = mid
        else:
            up = mid
    return M[low] == c

def merge(M, N):
    size = len(N)
    i, j, k = 0, 0, 0
    R = [0] * (2 * size)
    while i < size or j < size:
        if j == size or (i < size and M[i] < N[j]):
            R[k] = M[i]
            i += 1
        else:
            R[k] = N[j]
            j += 1
        k += 1
    return R

def swap_sorted(M, c, d):
    i = 0
    while M[i] != c:
        i += 1
    while i < len(M) - 1:
        M[i] = M[i + 1]
        i += 1
    while i > 0 and M[i - 1] > d:
        M[i] = M[i - 1]
        i -= 1
    M[i] = d

class DynamicBinarySearch:
    def __init__(self):
        self.n = 0
        self.maxn = 0
        self.A = []

    def search(self, c):
        i = 0
        j = self.n
        while j > 0:
            if j % 2 == 1 and binary_search(self.A[i], c):
                return True
            j //= 2
            i += 1
        return False

    def insert(self, c):
        i = 0
        j = self.n
        while j % 2 == 1:
            i += 1
            j //= 2
        if j == 0 and self.n == self.maxn:
            self.A.append([])
        self.A[i] = [c]
        for k in range(i):
            self.A[i] = merge(self.A[i], self.A[k])
        self.n += 1
        self.maxn = max(self.n, self.maxn)

    def delete(self, c):
        j =  self.n
        left_col = 0
        while j > 0 and j % 2 == 0:
            left_col += 1
            j //= 2
        found_col = left_col
        while j > 0:
            if j % 2 == 1 and binary_search(self.A[found_col], c):
                swap_sorted(self.A[found_col], c, self.A[left_col][0])
                s = 1
                size = 1
                for k in range(left_col):
                    for l in range(size):
                        self.A[k][l] = self.A[left_col][s]
                        s += 1
                    size *= 2
                self.n -= 1
                return True
            j //= 2
            found_col += 1
        return False

class EasySearch:
    def __init__(self):
        self.A = []

    def insert(self, c):
        self.A.append(c)

    def search(self, c):
        return c in self.A

    def delete(self, c):
        if not self.search(c):
            return
        del self.A[self.A.index(c)]

X = DynamicBinarySearch()
Y = EasySearch()
N = 10 ** 5
V = 1000
inserted = [False] * V
for i in range(N):
    value = randint(0, V - 1)
    request = randint(0, 2)
    if request == 0:
        ans1 = X.search(value)
        ans2 = Y.search(value)
        if ans1 != ans2:
            print("Error: ", inserted)
    elif request == 1:
        if inserted[value]:
            continue
        inserted[value] = True
        X.insert(value)
        Y.insert(value)
    else:
        inserted[value] = False
        X.delete(value)
        Y.delete(value)
