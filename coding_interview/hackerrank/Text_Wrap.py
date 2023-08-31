#this one was fun, I love the python docs

import textwrap

result = ""


def wrap(string, max_width):
    # count = 1
    # for y in string:
        
    #     print(y, end="")
    #     if count % 4 == 0:
    #         print()
    #     count+=1

    result = textwrap.wrap(string, max_width)
    
    realResult = ""
    for item in result:
        realResult += item+ "\n"
        
        
        
    return realResult

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)