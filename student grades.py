english = float(input("Enter the English grade: "))
math = float(input("Enter the Math grade: "))
science = float(input("Enter the Science grade: "))
history = float(input("Enter the History grade: "))
chemistry = float(input("Enter the Chemistry grade: "))

total = english + math + science + history + chemistry
percentage = (total / 500) * 100

print("Total Marks = %2f" %total)
print("Percentage = %2f" %percentage)

if (percentage >= 90): 
    print ('grade = A')
elif (percentage >= 80):
    print ('grade = B')
elif (percentage >= 70):
    print ('grade = C')
elif (percentage >= 60):
    print ('grade = D')
elif (percentage >= 50):
    print ('grade = E')
else:
    print ('grade = F')