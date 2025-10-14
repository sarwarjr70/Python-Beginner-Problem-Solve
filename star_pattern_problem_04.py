n = int(input("Enter a number: "))

# Pattern 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Pattern 1 different approach
for i in range(1, n + 1):
    print("*"* i, end="")
    print("")

#pattern 2
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print(("*"* i),end="")
    print("")

# Pattern 2 different approach
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# Pattern 3
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Pattern 3 different approach
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1),end="")
    print("")
    
# Pattern 4
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
    print("")
