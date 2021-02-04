def partition(A, start, end):
    pivot = A[end]
    i = start # menores que o pivot
    
    for j in range(start, end):
        if A[j] <= pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[i], A[end] = A[end], A[i]
    return i

def quick_sort(A, start=0, end=None):
    if end is None:
        end = len(A) - 1
    if start < end:
        pivot = partition(A, start, end)
        quick_sort(A, start, pivot - 1)
        quick_sort(A, pivot + 1, end)


    