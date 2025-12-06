n = input()

if n[0] != '-':
    print(n)
else:
    last = int(n[-1])
    second_last = int(n[-2])

    if last > second_last:
        result = n[:-1]
    else:
        result = n[:-2] + n[-1]


    if result == "-0":
        print(0)
    else:
        print(result)
