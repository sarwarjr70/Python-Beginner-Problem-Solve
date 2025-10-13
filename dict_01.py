marks = {
    "sarwar" : 95,
    "rahim"  : 85, 
    "karim"  : 75,
    "jamal"  : 65,
    "salim"  : 55
}

print(marks)

print(type(marks))
print(len(marks))
print(marks["sarwar"])

print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.get("karim"))
print(marks.get("carim")) # None

marks.update({"jamal": 70})

print(marks)

marks.update({"anwar": 90})
print(marks)
