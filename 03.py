# 3. Generate Fibonacci sequence up to N terms.

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci_sequence(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]