def selection_sort(array):
    for j in range(len(array)-1):
        min_index = j
        for i in range(j, len(array)):
            if array[i] < array[min_index]:
                min_index = i   
        if array[j] > array[min_index]:
            array[j], array[min_index] = array[min_index], array[j]

if __name__ == "__main__":
    a = [4, 2, 1, 9]
    selection_sort(a)
    print(f"Sorted array: {a}")
