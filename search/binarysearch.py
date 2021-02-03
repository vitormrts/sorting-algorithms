def recursive_binary_search(A, left, right, item):
    if right < left: # base case: element isnt on array
        return -1
    mid = (left + right)//2

    if A[mid] == item: # element is on array
        return mid
    elif A[mid] > item:
        return recursive_binary_search(A, left, mid - 1, item)
    else:
        return recursive_binary_search(A, mid + 1, right, item)

def iterative_binary_search(A, item):
    left  = 0
    right = len(A)-1

    while left <= right:
        mid = (left+right)//2
        if A[mid] == item:
            return mid
        elif A[mid] > item:
            right = mid - 1
        else:
            left = mid + 1

    return -1
