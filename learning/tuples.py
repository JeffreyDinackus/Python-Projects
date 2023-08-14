

#uses smooth braces

townies = ("bart", "dennis", "max", "jimmy", "stephano", "max")

# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

print(townies, len(townies))

roadies = ("hendrix",)

print(roadies)

#NOT A TUPLE

gravies = ("mustard")

print(gravies)

print(townies[:3])
print(townies[1:])

# workaround to change a tuple
y = list(townies)

y[1] = "besties"

x = tuple(y)

print(x)

townies += roadies
print(townies)

# del townies

# print(townies) ERROR

# unpacking 

(red, green, blue) = townies[4:7]

print(red,green,blue)

# * operator unpacks rest of list into this variable

(black, boron, *dark) = townies

print(black, boron, dark)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# changes number of times the entire fruit list added into new tuple
fruits2 = fruits * 3

print(fruits2)

print(fruits2.count("cherry"))