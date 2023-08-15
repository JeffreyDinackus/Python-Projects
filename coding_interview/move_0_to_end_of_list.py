
#any list you want
list = [0, 1, 0, 3, 12]


for item in list:
    if item == 0:
        # removes the current item if it equals 0
        list.remove(item)
        # append function always adds at end of list
        list.append(item)

print(list)