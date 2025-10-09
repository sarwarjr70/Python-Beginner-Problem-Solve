def find_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = find_sum(5, 10, 15, 20)
print("The sum is:", result)
