def swap_case(s):
    count = 0
    answer = list(s)
    for x in answer:
        if x.islower():
            answer[count] = answer[count].upper()
            count+=1
        else:
            answer[count] = answer[count].lower()
            count+=1
    
    answer2 = "".join(answer)
    return answer2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)