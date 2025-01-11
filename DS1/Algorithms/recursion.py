# Question 1: Factorial of a Number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = 5
print("Factorial:", factorial(number))

# Question 2: Fibonacci Sequence
def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 6
print(fibonacci(n))

# Question 3: Sum of an Array
def sum_of_an_arr(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_of_an_arr(arr[1:])

arr = [1, 2, 3, 4, 5]
print(sum_of_an_arr(arr))