s = input()
lower_case = 0
upper_case = 0
for i in s:
    if i.islower():
        lower_case += 1
    else: 
        upper_case += 1
if lower_case >= upper_case:
    print(s.lower())
else:
    print(s.upper())
        
