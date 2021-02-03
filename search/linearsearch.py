# Complexity O(n)

def linear_search(array: list, elem):
    for index, number in enumerate(array):
        if number == elem:
            print(f"The elem {elem} is present ind array, on index {index}.")
            return index
        print(f"The elem {elem} isn't on array.")
        return -1
    
def linear_search_in(array: list, elem):
    return elem in array # this return true or false

def linear_search_index(array: list, elem):
    try:
        return array.index(elem)
    except ValueError:
        return -1


array = list(range(1, 100))

print(linear_search(array, 101))
print(linear_search(array, 1))
