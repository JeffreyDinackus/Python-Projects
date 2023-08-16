def count_substring(string, sub_string):
    
    count = 0
    flag = True
    var = 0
    position = 0
    while flag:
        
        var = string.find(sub_string,position)
        if var == -1:
            flag = False
        if var != -1:
            count+=1
        position = var + 1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)