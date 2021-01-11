import random

def selection_sort(array):
    for j in range(len(array)-1):
        min_index = j
        for i in range(j, len(array)):
            if array[i] < array[min_index]:
                min_index = i
        if array[j] > array[min_index]:
            aux = array[j] 
            array[j] = array[min_index]
            array[min_index] = aux

for i in range(1, 11):
    generated_array = random.sample(range(1, 1000), 10)
    print(f"=========   TEST {i}   =========\nGenerated List: {generated_array}\n")
    selection_sort(generated_array)
    print(f"Sorted List: {generated_array}\n")
