n = int(input())
vol = list(map(int, input().split()))
cap = list(map(int, input().split()))

total_vol = sum(vol)

cap.sort() 

if cap[-1] + cap[-2] >= total_vol:
    print("YES")
else:
    print("NO")
