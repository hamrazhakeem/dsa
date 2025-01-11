# Question 1: Reverse a String
string = 'hello'
print(string[::-1])

# Question 2: Check if a String is a Palindrome
string = "radar"
flag = 0
for i in range(len(string) // 2):
    if string[i] != string[len(string) - i - 1]:
        print(False)
        flag = 1
        break
    
if not flag:
    print(True)

# Question 3: Count Vowels in a String
vowels = ['a', 'e', 'i', 'o', 'u']
string = "Programming"
count = 0
for i in string:
    if i in vowels:
        count += 1
print(count)