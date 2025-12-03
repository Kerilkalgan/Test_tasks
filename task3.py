
def merge(A:list, B:list):
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    if i < len(A):
        C[n:] = A[i:]
    if k < len(B):
        C[n:] = B[k:]
    return C

def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = A[0:middle]
    R = A[middle:]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    A[0:] = C[0:]

A = [7, 2, 5, 3, 7, 13, 1, 6]
merge_sort(A)
print(A)