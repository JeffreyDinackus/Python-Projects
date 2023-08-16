def mutate_string(string, position, character):
    arr = list(string)
    arr2 = arr
    arr2[position] = arr[position] = character
    str1=''
    str1 = "".join(arr2)
    return str1

    
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)