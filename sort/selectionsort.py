def selection_sort(A): # O(n^2)
    n = len(A)
    for i in range(n): # percorre a lista
        min = i
        for j in range(i+1, n): # encontra o menor elemento da lista a partir de i + 1
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i] # swap do menor elemento com o elemento atual
    return A


A = [5, 6, 4, 7, 1, 2]
selection_sort(A)
print(A)