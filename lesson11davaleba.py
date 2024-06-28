def fibonacci(n, memory={}):
    if n in memory:
        return memory[n]
    if n <= 1:
        return n
    memory[n] = fibonacci(n-1, memory) + fibonacci(n-2, memory)
    return memory[n]


def factorial(n, memory={}):
    if n in memory:
        return memory[n]
    if n == 0 or n == 1:
        return 1
    memory[n] = n * factorial(n-1, memory)
    return memory[n]


print(fibonacci(7))
print(fibonacci(10))


print(factorial(3))
print(factorial(8))

