def bubble_sort(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i+1], array[i] = array[i], array[i+1]


if __name__ == "__main__":
    a = [4, 2, 1, 9]
    bubble_sort(a)
    print(f"Sorted array: {a}")
