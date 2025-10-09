min = int(input("Enter the minimum value: "))
max = int(input("Enter the maximum value: "))

even_total = 0
odd_total = 0

for num in range(min, max + 1):
    if num % 2 == 0:
        even_total += num
    else:
        odd_total += num

print(f"The sum of even numbers between {min} and {max} is: {even_total}")
print(f"The sum of odd numbers between {min} and {max} is: {odd_total}")
