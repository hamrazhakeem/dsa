# Question 1: Reverse an Array
arr = [1, 2, 3, 4, 5]
print(arr[::-1])

# Question 2: Find the Largest Element in an Array
arr = [10, 25, 7, 99, 3]
larg = arr[0]
for i in arr:
    if i > larg:
        larg = i
print(larg)

# Question 3: Check if an Array Contains a Specific Element
arr = [1, 2, 3, 4, 5]
target = 8
if target in arr:
    print(True)
else:
    print(False)