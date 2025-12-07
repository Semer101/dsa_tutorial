n = int(input())
word = input()
extra = 0

for i in range(1, n):
    if word[i] == word[i-1]:
        extra += 1

print(extra)
