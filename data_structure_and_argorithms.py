#Đê quy chia để trị , thuật toán khá hay nhé baby

def Merge(A, L, R, start, end):
    i = 0
    len_L = len(L)
    j = 0
    len_R = len(R)
    t = 0
    k = start
    while k <= end:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
            k = k + 1
            if i == len_L:
                t = 1
                break
        else:
            A[k] = R[j]
            j = j + 1
            k = k + 1
            if j == len_R:
                t = 2
                break
    if t == 1:
        for l in range(j, len_R):
            A[k] = R[l]
            k = k + 1
    elif t == 2:
        for l in range(i, len_L):
            A[k] = L[l]
            k = k + 1
    return A[start:end + 1]


def Merge_sort(A, start, end):
    if start == end:
        return [A[start]]
    div = int((end + start)/2)
    L = Merge_sort(A, start, div)
    R = Merge_sort(A, div + 1, end)
    Merge(A, L, R, start, end)
    return A[start: end + 1]
