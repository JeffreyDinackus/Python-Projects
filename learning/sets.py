myset = {1,2,3,4,5}

x = list(myset)
print(x)
x[1] = 0

myset = set(x)

print(myset)

# check if a number is in a set
print(1 in myset)

myset.add(6)
twoset = {2,3,4,211,3,2,43,4,34,34,34,55}
print(myset)


myset.update(twoset)

print(myset)

myset.remove(211)

print(myset)

y = myset.pop()
print(myset, y)

print(myset.union(twoset))

myset.intersection_update(twoset)
print(twoset, myset)
print(myset)
u = twoset.intersection(myset)

print(u)
del myset