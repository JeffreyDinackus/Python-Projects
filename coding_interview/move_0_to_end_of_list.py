
#any list1 you want
list1 = ['0', 0, '0', 1, 0, '0', 3, 12]


for item in list1:
    if item == 0:
        # removes the current item if it equals 0
        list1.remove(item)
        # append function always adds at end of list1
        list1.append(item)
    if item == '0':
        # removes the current item if it equals 0
        list1.remove(item)
        # append function always adds at end of list1
        list1.append(item)


print(list1)