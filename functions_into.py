
# This function calculates the average of three numbers entered by the user.
def avg ():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    average = (a + b + c) / 3

    print("The average is:", average)

avg()
print("thank you")
avg()
print("goodbye")
avg()
print("see you later")

# This function prints a goodbye message including the user's name.
def goodbye():
    print("This is the end of the program. Goodbye!" + name)

name = input("Enter your name: ")
goodbye()

# This function prints a goodbye message including the user's name and a custom ending message.
def goodbye( name, ending="Thank you for using our program. "):
    print("This is the end of the program. Goodbye!" + name)
    print(ending)

name2 = input("Enter your name: ")
goodbye(name)
goodbye(name2, "Have a great day! ")