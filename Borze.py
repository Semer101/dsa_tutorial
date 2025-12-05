n = list(input())
ans = ""
i=0
while i < len(n):
    if n[i] == ".":
        ans += "0"
        i += 1
    else:
        if n[i+1] == ".":
            ans += "1"
            i += 2
        else:
            ans += "2"
            i += 2
            
print(ans)
