letter = '''Dear <|NAME|>,
     You are selected!
     Date: <|DATE|>'''

name = input("Enter Your Name: ")
date = input("Enter Date: ")
letter = (letter.replace("<|NAME|>", name).replace("<|DATE|>", date))
print(letter)

name2 = input("Enter Your Full Name: ")

print(f"Good Afternoon, {name2}")


N = "Sarwar Jahan  Moon is  a  Programmer"

print(N.find("Moon"))

print(N.replace("  ", " "))
print(N.replace("Moon", "Khan"))
print(N)


letter2 = "Dear Sarwar Jahan Moon, \n\tThis python course is nice. \nThanks!"
print(letter2)

