if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        command = input().split()
        cmd = command[0]
        if cmd == "insert":
            index = int(command[1])
            number = int(command[2])
            arr.insert(index, number)
        elif cmd == "print":
            print(arr)
        elif cmd == "remove":
            number = int(command[1])
            arr.remove(number)
        elif cmd == "append":
            number = int(command[1])
            arr.append(number)
        elif cmd == "sort":
            arr.sort()
        elif cmd == "pop":
            arr.pop()
        elif cmd == "reverse":
            arr.reverse()
