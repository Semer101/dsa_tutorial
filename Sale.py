n, m = map(int, input().split())
lst = list(map(int, input().split()))
negatives = [x for x in lst if x < 0]
negatives.sort()
money = 0
for i in range(min(m, len(negatives))):
    money += -negatives[i]  
print(money)
