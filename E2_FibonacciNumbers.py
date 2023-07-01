# Excercise 2: This program shows the n-th number of the Fibonacci sequence
# Also this code sums all Fibonacci numbers whose values do not exceed a given n

def fibonacci(n):
    s = 0
    if n == 1:
        s = 1
    elif n == 2:
        s = 1
    else:
        s = fibonacci(n-1) + fibonacci(n-2)
    return s

sum = 0
n = input("Input a number:")
n = int(n)

for i in range(n):
    i = i + 1
    if fibonacci(i) < n:
        sum = sum + fibonacci(i)
    else:
        quit

print(sum)
