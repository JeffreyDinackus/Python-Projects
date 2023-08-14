fruits = ["dragonfruit", "bananas", "memefruit"]


fruits.insert(1, "flyfruit")

print(fruits)


fruits.remove("memefruit")
print("Fake fruit! ", fruits)

fruits[-1] = "dogfruit"
fruits.append("bananas")
print(fruits)

# check for fruit and remove
for i in fruits:
    if i == "dogfruit":
        fruits.remove(i)

print(fruits)

# append multiple items
fruits2 = ["scarfruit", "heavyfruit", "babyfruit", "woodfruit"]

fruits.extend(fruits2)
# fruits += fruits2

# start to start
print(fruits[3:5])



fruits.reverse()
print(fruits)


for i in fruits:
    print(i, end=" ")

# list comprehensions

SFriendsFruits = []

for i in fruits:
    if "s" in i:
        SFriendsFruits.append(i)

print(SFriendsFruits)

AFriendFruits = [i for i in fruits if "a" in i]

print(AFriendFruits)


# length and count

print(len(fruits), fruits.count("babyfruit"))

count = 0 
for i in fruits:
    if i == "babyfruit":
        count+=1

# removing items

fruits.pop(1)

print(fruits.count("babyfruit"))


fruits.sort(reverse=True)
print(fruits)

print(fruits.index("flyfruit"))

print(fruits)