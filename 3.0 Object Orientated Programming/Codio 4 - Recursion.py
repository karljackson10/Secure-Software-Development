def factorial(n):
    """Calculate factorial recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """Calculate Fibonacci numbers"""
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

#main
#print(factorial(-6))
#print(fibonacci(3))
fibonacci_length = 10
for num in range(fibonacci_length):
    print(fibonacci(num))