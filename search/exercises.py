from binarysearch import iterative_binary_search

def exercise_01(n):
    A = list(range(1, n))

    left = 0
    right = len(A)-1

    while left <= right:
        print("Esse número é", end=' ')
        maior_menor = input("").lower()
        print('que', end=' ')
        num = int(input(""))

        if  maior_menor == 'maior':
            left = num + 1
        else:
            right = num - 1



exercise_01(5)