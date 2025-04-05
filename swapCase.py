def swap_case(s):
    r = ""
    for i in s:
        
        if i == i.upper():
            r += i.lower()
        else:
            r += i.upper()
    return r

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
