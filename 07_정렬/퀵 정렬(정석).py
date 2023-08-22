# 퀵 정렬
sample = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]

def quick_sort(array, start, end):
    if start >= end:
        return
    
    pivot = array[start]
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= pivot:
            left += 1
        while right > start and array[right] >= pivot:
            right -= 1
        if left > right:
            array[start], array[right] = array[right], array[start]
            break
        array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
        

quick_sort(sample, 0, len(sample)-1)
print(sample)