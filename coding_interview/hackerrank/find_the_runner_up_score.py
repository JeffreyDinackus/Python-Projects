if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
    x = list(reversed(sorted(list(arr))))

    for i in x:
        if i < x[0]:
            print(i)
            break