def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j] = key


if __name__ == "__main__":
    a = [4, 2, 1, 9]
    insertion_sort(a)
    print(f"Sorted array: {a}")
