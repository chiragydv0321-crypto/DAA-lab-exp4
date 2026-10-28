"""
Experiment 4: Selection and Dynamic Programming
Program 4: Smallest Missing Positive
Aim: Find the smallest missing positive integer.
"""

def first_missing_positive(a):
    a = a[:]
    n = len(a)
    for i in range(n):
        while 1 <= a[i] <= n and a[a[i] - 1] != a[i]:
            j = a[i] - 1
            a[i], a[j] = a[j], a[i]
    for i, x in enumerate(a):
        if x != i + 1:
            return i + 1
    return n + 1

print(first_missing_positive([3, 4, -1, 1]))
