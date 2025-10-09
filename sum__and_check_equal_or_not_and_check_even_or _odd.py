a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

sum = a + b + c


if a == b == c:
    result = sum * 3
else:
    result = sum

print("Result:", result)

if result % 2 == 0:
    print("The result is even.")
else:
    print("The result is odd.")
