# Question 1: Find an Element in an Array
arr = [1, 2, 3, 2, 4, 2], element = 2
flag = 0
for i in range(len(arr)):
    if element == arr[i]:
        flag = 1
        print(i)
        break
if not flag:
    print(-1)

# Question 2: Count Occurrences of an Element in an Array
arr = [10, 20, 30, 40, 50], element = 30
count = 0
for i in arr:
    if i == element:
        count += 1
print(count)

# Question 3: Find the Minimum Element in an Array
arr = [5, 3, 8, 6, 2]
smallest = arr[0]
for i in arr:
    if i < smallest:
        smallest = i
print(smallest)