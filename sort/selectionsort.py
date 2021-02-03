def selection_sort(A): # O(n^2)
    n = len(A)
    for i in range(n): # percorre a lista
        min = i
        for j in range(i+1, n): # encontra o menor elemento da lista a partir de i + 1
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i] # insere o elemento na posicao correta
    return A