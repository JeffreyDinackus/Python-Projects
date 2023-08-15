x, y, z = "cat", "dog", "leprechaun"

print(z)

i = j = k = "catapult"

print(i,j,k)

def basic():
    global x 
    x = 9



basic()

print(x)
import random
x = random.random()

# random with choice of numbers, this is good

list2 = [9,10,11,12,13]

y = random.choice(list2)


print(x)

print(y)
match y:
    case 9:
        print("I like pie!")
    case 10:
        print("XD")
    case 11:
        print("Dingoes!")
    case 12:
        print("porcupine!")
    case _:
        print("ERROR")

# doesn't appear to choose the last number in the range
i = random.randrange(1, 4, 1)

print(i)

# seeds a random number, if you want to use the same random number. Maybe easier to stick the value in a variable.
# random.seed(5)

# print(random.random())

# this reorganizes the original list, it doesn't output a new list. if you set a second list to the original, it shuffled both. 


list3 = list2
random.shuffle(list2)
print(list2,list3)

# this is the solution if you want a original copy of the first list. 

list4 = []

for i in list3:
    list4.append(i)

print(list4)

# this shuffles both list2 and list3
random.shuffle(list3)

print(list4, list3, list2)


i = 0
while i < 6:
    print(i)
    i+=1
    if i == 4:
        print(i)
        continue
else:
    print("i > 6", i)

for i in range(6):
    print(i)


for i in range(1, 10, 3):
    print(i)

list5 = ["cat", "dog", "bowser"]

for i in list5:
    for x in i:
        print(x, i)

#print youngest child
def kids(*kids):
    print(kids[-1])

kids("zir", "ze", "bus station 41", "Ecks dee")

def my_function(child3, child2, child1):
    print(child3)

my_function(child3 = "dee", child2 = "mac", child1 = "dennis")


