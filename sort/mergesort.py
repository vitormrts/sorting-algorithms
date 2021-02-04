def merge(A, start, mid, end):
    left = A[start:mid]
    right = A[mid:end]
    top_left, top_right = 0, 0

    for k in range(start, end):
        if top_left >= len(left):
            A[k] = right[top_right]
            top_right += 1
        
        elif top_right >= len(right):
            A[k] = left[top_left]
            top_left += 1

        elif left[top_left] < right[top_right]:
            A[k] = left[top_left]
            top_left += 1
        else:
            A[k] = right[top_right]
            top_right += 1

def merge_sort(A, start=0, end=None):
    if end is None:
        end = len(A)

    if end - start > 1:
        mid = (end + start)//2
        merge_sort(A, start, mid)
        merge_sort(A, mid, end)
        merge(A, start, mid, end)
