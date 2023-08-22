sample = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left = [i for i in tail if i < pivot]
    right = [i for i in tail if i > pivot]

    return quick_sort(left)+[pivot]+quick_sort(right)

print(quick_sort(sample))