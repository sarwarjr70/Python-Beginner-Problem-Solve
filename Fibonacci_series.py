# x, y = 0, 1

# while y < 50:
#     print(y)

#     x, y = y, x + y


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci Series:", end=" ")
    for i in range(terms):
        print(fibonacci(i), end=" ")

