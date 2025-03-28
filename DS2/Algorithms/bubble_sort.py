def sort(str):
    for i in range(len(str) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if str[j] > str[j + 1]:
                str[j], str[j + 1] = str[j + 1], str[j]
                swapped = True
        if not swapped:
            break

strings = ["apple", "orange", "banana", "grape", "cherry"]
sort(strings)
print(strings)