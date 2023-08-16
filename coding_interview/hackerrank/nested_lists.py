# if __name__ == '__main__':
#     arr = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
        
#         arr.append([score,name])
        
#     sort = sorted(arr)
    
#     answer = []
#     sentinel = False
#     count = 0

#     for i in sort:
#         for x in i:
#             if sentinel == True:
#                 print(x)
#                 sentinel = False
#                 count +=1
#                 if count > 1: 
#                     break
#             if type(x) == float:
#                 if x > sort[0][0]:
#                     sentinel = True
            
#         if count > 1:
#             break




if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        arr.append([score,name])
        
    sort = sorted(arr)
    
    second_lowest_grade = None
    for i in range(1, len(sort)):
        if sort[i][0] > sort[0][0]:
            second_lowest_grade = sort[i][0]
            break
    
    for grade, name in sort:
        if grade == second_lowest_grade:
            print(name)