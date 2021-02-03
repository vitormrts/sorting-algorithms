def insertion_sort(A):
    n = len(A)
    for i in range(1, n): # percorre o array
        key = A[i] # essa chave sera comparada com os elementos a sua esquerda
        j = i - 1

        while j >= 0 and key <= A[j]:
            A[j+1] = A[j] # move os elementos para a direita
            j -= 1
        A[j+1] = key # posicao que o elemento precisa ser inserida
