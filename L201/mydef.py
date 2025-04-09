def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True

def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4, 5]))
