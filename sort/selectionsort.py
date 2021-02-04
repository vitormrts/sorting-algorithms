def selection_sort(A): # O(n^2)
    n = len(A)
    for i in range(n-1): # percorre a lista
        min = i
        for j in range(i+1, n): # encontra o menor elemento da lista a partir de i + 1
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i] # insere o elemento na posicao correta
    return A

# 1 + (n-1)*[3 + X] = 1 + 3*(n-1) + X*(n-1) = 1 + 3*(n-1) + (n^2 + n - 2)/2
# = (1 - 3 - 1) + (3n + n/2) + (n^2/2)
# The complexity is O(n^2)