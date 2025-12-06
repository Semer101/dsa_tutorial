n = int(input())
for i in range(n):
    fir, sec, thir = input().rstrip().split()
    ans = fir[0] + sec[0] + thir[0]
    print(ans)
