# Question 1: Find an Element in a Sorted Array
# arr = [10, 20, 30, 40, 50]
# target = 30
# l, r = 0, len(arr) - 1

# while l < r:
#     mid = (l + r) // 2
#     if arr[mid] == target:
#         print(mid)
#         break
#     elif arr[mid] < target:
#         l = mid + 1
#     else:
#         r = mid - 1

# Question 2: Find the First Occurrence of an Element
def first_occurrence(arr, elem):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == elem:
            result = mid
            high = mid - 1
        elif arr[mid] < elem:
            low = mid + 1
        else:
            high = mid - 1
    return result

input_array = [1, 2, 2, 2, 3]
element = 2
print("First occurrence index:", first_occurrence(input_array, element))

# Question 3: Find the Smallest Element Greater Than a Target
def smallest_greater_than_target(arr, tar):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > tar:
            result = arr[mid]
            high = mid - 1
        else:
            low = mid + 2
    return result

arr = [10, 20, 30, 40, 50]
target = 25
print(smallest_greater_than_target(arr, target))