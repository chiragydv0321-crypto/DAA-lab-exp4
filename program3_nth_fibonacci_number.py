"""
Experiment 4: Selection and Dynamic Programming
Program 3: Nth Fibonacci Number
Aim: Compute the nth Fibonacci number using dynamic programming.
"""

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci(10))
