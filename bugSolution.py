def factorial(n):
    if n < 0:
        return None  # Or raise an exception: raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

print(factorial(5))  # Output: 120
print(factorial(-1)) # Output: None 