def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]

arr = [7, 3, 8, 5, 9]
selection_sort(arr)
print(arr)
