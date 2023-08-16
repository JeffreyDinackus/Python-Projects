

def split_and_join(line):
    a = line.split(" ") # a is converted to a list of strings. 
    b = "-".join(a)
    return b


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)