if __name__ == '__main__':
    s = input()
    
    
    
    if s.isalnum == False:
        if s.isalpha == False:
            for i in range(1, 5):
                print(False)
    
    
    try:
        sentinel = False
        for i in s:
            if i.isalnum() == True:
                    print("True")
                    Sentinel = True
                    break
        
        if Sentinel == False:
            print("False")
            
        Sentinel = False
        
        for i in s:
            if i.isalpha() == True:
                    print("True")
                    Sentinel = True
                    break
        
        if Sentinel == False:
            print("False")
            
        Sentinel = False
        
        for i in s:
            if i.isdigit() == True:
                    print("True")
                    Sentinel = True
                    break
        
        if Sentinel == False:
            print("False")
            
        Sentinel = False
        
        for i in s:
            if i.islower() == True:
                    print("True")
                    Sentinel = True
                    break
        
        if Sentinel == False:
            print("False")
            
        Sentinel = False
        
        for i in s:
            if i.isupper() == True:
                    print("True")
                    Sentinel = True
                    break
        
        if Sentinel == False:
            print("False")
            
        Sentinel = False
    except:
        print("False")
        print("False")
        print("False")
        print("False")
        print("False")

    # original attempt    
    # if s.isalnum() == True:
    #     print("True")
    # else: print("False")
    # if s.isalpha() == True:
    #     print("True")
    # else: print("False")
    # if s.isdigit() == True:
    #     print("True")
    # else: print("False")
    # if s.islower() == True:
    #     print("True")
    # else: print("False")
    # if s.isupper() == True:
    #     print("True")
    # else: print("False")