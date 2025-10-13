e = set()

print(type(e))

s = {1, 2, 3, 4, 5, 1, 2, 3,68, 4, 5}
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
s2 = {4, 5, 6, 7, 8, 9}

print (type(s))

print(s)

s.add(6)

print(s)

s.remove(3)

print(s)

print (s1.union(s2))
print (s1.intersection(s2))
