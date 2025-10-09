a = int(input("Enter the First Angle Of a Triangle: "))
b = int(input("Enter the Second Angle Of a Triangle: "))
c = int(input("Enter the Third Angle Of a Triangle: "))

total = a + b + c

if total == 180:
    print("The Triangle is Valid")
else:
    print("The Triangle is Not Valid")
