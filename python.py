
s = input("")
l = len(s)
i = l - 1
while i >= 0:
    print(s[i], end="")
    i = i - 1

# Check if a string is a palindrome
s = input("")
l = len(s)
i = l - 1
rev = ""
while i >= 0:
    rev = rev + s[i]
    i = i - 1
if s == rev:
    print("palindrome.")
else:
    print("not a palindrome.")

# Count vowels and consonants in a string
s = input("Enter a string: ")
vowels = 0
consonants = 0
i = 0
while i < len(s):
    if s[i].lower() in 'aeiou':
        vowels += 1
    elif s[i].isalpha():
        consonants += 1
    i = i + 1
print("Vowels:", vowels)
print("Consonants:", consonants)

# Remove spaces from a string
s = input("Enter a string: ")
no_spaces = ""
i = 0
while i < len(s):
    if s[i] != ' ':
        no_spaces += s[i]
    i = i + 1
print("String without spaces:", no_spaces)
# Count frequency of characters in a string
s = input("Enter a string: ")
i = 0
freq = {}
while i < len(s):
    if s[i] in freq:
        freq[s[i]] += 1
    else:
        freq[s[i]] = 1
    i = i + 1
for char in freq:
    print(f"Frequency of '{char}': {freq[char]}")

# Check if a number is prime
num = int(input("Enter a number: "))
if num > 1:
    i = 2
    while i < num:
        if num % i == 0:
            print(num, "is not a prime number")
            break
        i = i + 1
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
# Find the factorial of a number
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    i = 1
    while i <= num:
        factorial = factorial * i
        i = i + 1
    print("Factorial of", num, "is", factorial)

# Print the Fibonacci series up to n terms
nterms = int(input("Enter the number of terms: "))
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1

# Find the sum of digits of a given number
n= int(input("Enter a number: "))
sum = 0
while n> 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print("Sum of digits is", sum)

# Reverse the digits of a given number
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print("Reversed number is", reversed_num)


