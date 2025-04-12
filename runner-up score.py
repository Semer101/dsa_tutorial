if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = sorted(arr)
    for i in range(n,0,-1):
        if arr[i-1] != arr[i-2]:
            print(arr[i-2])
            break
