def bubble_sort(A): # O(n^2)
    n = len(A)
    for i in range(n-1):
        for j in range(n-1):
            if A[j] > A[j+1]:
                A[j+1], A[j] = A[j], A[j+1]
    print(A)


