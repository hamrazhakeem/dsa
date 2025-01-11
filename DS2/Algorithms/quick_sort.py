#in place algo
def get_pivot_place(arr, first, last):
    pivot = arr[first]
    left = first + 1
    right = last

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if right < left:
            arr[first], arr[right] = arr[right], arr[first]
            return right
        else:
            arr[left], arr[right] = arr[right], arr[left]

def quicksort(arr, first, last):
    if first < last:
        p = get_pivot_place(arr, first, last)
        quicksort(arr, first, p - 1)
        quicksort(arr, p + 1, last)

array = [5, 3, 2, 1]
quicksort(array, 0, len(array) - 1)
print(array)

#non-inplace algo
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

arr = [5, 2, 1]
print(quicksort(arr))