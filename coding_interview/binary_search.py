import math

array = [1,2,3,4,5,6,7,8,9,10,15,200]
# in this problem the answer is always in the array
value_to_find = 9

length = len(array)

search_factor = 0
count = 0
length_factor = length/2

found = False
search_factor = 6
while found == False:

  
    search_factor = array[int(length_factor)]

    print("len", length_factor, "sea", search_factor)
    if search_factor == value_to_find:
        found = True
    if count > 10:
        break

    print(array[int(length_factor)])
    if value_to_find > array[int(length_factor)]:
        length_factor = length_factor + math.ceil(length_factor / 2)
        print(length_factor)
        search_factor = array[int(length_factor)]



    elif value_to_find < array[int(length_factor)]:
        length_factor = int(length_factor // 2)

        search_factor = array[int(length_factor)]



    count+=1
 



print("found in", count, "tries")