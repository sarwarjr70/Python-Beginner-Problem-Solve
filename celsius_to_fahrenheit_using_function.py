# c/5 = f-32/9
# c = 5 *((f-32)/9)

# f = int(input("Enter temperature in Fahrenheit: "))
# c = 5 * ((f - 32) / 9)
# print("Temperature in Celsius is:", c)

def fahrenheit_to_celsius(f):
    c = 5 * ((f - 32) / 9)
    return c

f = int(input("Enter temperature in Fahrenheit: "))
c = fahrenheit_to_celsius(f)
print(f"Temperature in Celsius is: {round(c, 2)} °C")

