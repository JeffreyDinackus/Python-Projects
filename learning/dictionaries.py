

# declaring

# {number : "how I feel about it"}
test = {1 : "First number", 2 : "Twice the fun", 3 : "3 dogs dancing", 4 : "four days until Friday", 5 : "Rhymes with fun"}

str_test = {"cats" : "meaw", "dogs" : "ruff", "giraffes" : "???", "foxes" : "RING DING DING"}

# looping

for i in test:
    print(i, test[i])

print("")
# one line
for i in test:
    print(i, test[i], end=" ")


print("\n")
# a different way, more readable

for key, value in test.items():
    print(key, value)


# type

print(type(test))
# = dict

if type(test) == dict:
    print("its a dict")


# accessing items

x = test[1]
print(x)

y = str_test["foxes"]
print(y)

print(str_test["cats"])

x = test.keys()
y = str_test.keys()
print(x, y)

print(test.values(), str_test.values())

#common mistake 

print(str_test.keys)


# convert

# to tuple

x = test.items()

print(x)

# they are linked if the original changes, prob means the tuple was referring to the original object

test[1] = "cats"

print(x)


# adding, very easy and natural

str_test["Dancers"] = "Soundtrack to the movie footloose"

str_test.update({"Dorks" : "orf"})

# get method, alternative way to access

print(str_test.get("Dancers"))
print(str_test)

#remove with pop method, like the inner workings of computers

test.pop(1)

print(test)
print("rip the homie #1")



# empty the method

test.clear()

print(test)

# delete dictionary
del test

#print(test) gives error



#copying


test2 = str_test.copy() # or .dict() similar thing

print(test2)

# nested dicts

dict2 = {"ground" : {"basement" : {"love" : "at the bottom"}}}

print(dict2)


# return the value if it exsits, otherwise create it

x = dict2.setdefault("second", "parlor")

y = dict2.setdefault("ground", "lobby")

print(x, y)