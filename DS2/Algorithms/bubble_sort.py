# def sort(nums):
#     for i in range(len(nums) - 1, 0, -1):
#         swapped = False
#         for j in range(i):
#             if nums[j] < nums[j + 1]:
#                 swapped = True
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#             print(nums)
#         if not swapped:
#             break

# nums = [5, 3, 2, 7, 9]
# sort(nums)
# print(nums)

# # Use Bubble Sort to sort an array of strings alphabetically:
# def sort(str):
#     for i in range(len(str) - 1, 0, -1):
#         swapped = False
#         for j in range(i):
#             if str[j] > str[j + 1]:
#                 str[j], str[j + 1] = str[j + 1], str[j]
#                 swapped = True
#         if not swapped:
#             break

# strings = ["apple", "orange", "banana", "grape", "cherry"]
# sort(strings)
# print(strings)