# num = int(input("Enter a number: "))

# factorial = 1

# if num < 0:
#    print("factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)


n = int(input("Enter a number: "))

product = 1

for i in range(1, n + 1):
      product *= i
print(f"The factorial of {n} is: {product}")
