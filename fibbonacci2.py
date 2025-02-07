def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Get user input
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Generate and print Fibonacci numbers
for num in fibonacci_generator(num_terms):
    print(num)
