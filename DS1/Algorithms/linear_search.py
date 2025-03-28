arr = [1, 2, 3, 2, 4, 2], element = 2
flag = 0
for i in range(len(arr)):
    if element == arr[i]:
        flag = 1
        print(i)
        break
if not flag:
    print(-1)