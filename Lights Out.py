g = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    row = ""
    for j in range(3):
        # Count toggles: itself + neighbors
        s = g[i][j]
        if i > 0: s += g[i-1][j]
        if i < 2: s += g[i+1][j]
        if j > 0: s += g[i][j-1]
        if j < 2: s += g[i][j+1]
        
        row += str(1 if s % 2 == 0 else 0)
    print(row)
